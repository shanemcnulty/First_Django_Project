from django.shortcuts import render
from django.contrib import messages
from .forms import ContactView


def contact(request):
    if request.method == 'POST':
        form = ContactView(request.POST)
        if form.is_valid():
            our_form = form.save(commit=False)
            our_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent. Thank you.')
            return render(request, 'index.html')
    else:
        form = ContactView()
    return render(request, 'contact.html', {'form': form})
