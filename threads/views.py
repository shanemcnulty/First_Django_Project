from django.shortcuts import render, get_object_or_404
from models import Subject, Thread, Posts, PollSubject
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
import arrow
from django import template
from django.forms import formset_factory
from threads.forms import ThreadForm, PollForm, PollSubjectForm, PostForm


def forum(request):
    return render(request, 'forum.html', {'subjects': Subject.objects.all()})


def threads(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'threads.html', {'subject': subject})


@login_required
def new_thread(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    poll_subject_formset = formset_factory(PollSubjectForm, extra=3)
    if request.method == "POST":
        thread_form = ThreadForm(request.POST)
        post_form = PostForm(request.POST)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset(request.POST)
        if thread_form.is_valid() and post_form.is_valid() and poll_form.is_valid() and poll_subject_formset.is_valid():
            thread = thread_form.save(False)
            thread.subject = subject
            thread.user = request.user
            thread.save()

            post = post_form.save(False)
            post.user = request.user
            post.thread = thread
            post.save()

            poll = poll_form.save(False)
            poll.thread = thread
            poll.save()

            for subject_form in poll_subject_formset:
                subject = subject_form.save(False)
                subject.poll = poll
                subject.save()

        messages.success(request, "You have created a new thread!")

        return redirect(reverse('thread', args={thread.pk}))

    else:
        thread_form = ThreadForm()
        post_form = PostForm(request.POST)
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset()

    args = {
        'thread_form': thread_form,
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
    }

    args.update(csrf(request))

    return render(request, 'thread_form.html', args)


def thread(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_}
    args.update(csrf(request))
    return render(request, 'thread.html', args)


@login_required
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm()

    args = {
        'form': form,
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Posts, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, "Your have updated your thread!")

            return redirect(reverse('thread', args={thread.pk}))
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'form_action': reverse('edit_post', kwargs={"thread_id": thread.id,
                                                    "post_id": post.id}),
        'button_text': 'Update Post'
    }
    args.update(csrf(request))

    return render(request, 'post_form.html', args)


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    thread_id = post.thread.id
    post.delete()

    messages.success(request, "Your post was deleted!")

    return redirect(reverse('thread', args={thread_id}))


register = template.Library()


@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()

    return total_posts


@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()


@register.simple_tag
def last_posted_user_name(thread):
    posts = thread.posts.all().order_by('created_at')
    return posts.first().user.username


@login_required
def thread_vote(request, thread_id, subject_id):
    thread = Thread.objects.get(id=thread_id)

    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You already voted on this! ... your not trying to cheat are you?")
        return redirect(reverse('thread', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)

    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('thread', args={thread_id}))


@register.simple_tag
def user_vote_button(thread, subject, user):
    vote = thread.poll.votes.filter(user_id=user.id).first()

    if not vote:
        if user.is_authenticated():
            link = """
            <div class="col-md-3 btn-vote">
            <a href="%s" class="btn btn-default btn-sm">
                Add my vote!
            </a>
            </div>""" % reverse('cast_vote', kwargs={'thread_id': thread.id, 'subject_id': subject.id})

            return link

    return ""
