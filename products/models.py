from paypal.standard.ipn.signals import subscription_signup, subscription_cancel
from django.contrib.auth.models import AbstractUser
import arrow


def subscription_created(sender, **kwargs):
    ipn_obj = sender

    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]

    purchase = Purchase.objects.create(magazine_id=magazine_id,
                                       user_id=user_id,
                                       subscription_end=arrow.now().replace(weeks=+ 4).datetime)


subscription_signup.connect(subscription_created)


def subscription_was_cancelled(sender, **kwargs):
    ipn_obj = sender

    magazine_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]

    purchase = Purchase.objects.get(user_id=user_id, magazine_id=magazine_id)
    purchase.subscription_end = arrow.now()
    purchase.save()


subscription_cancel.connect(subscription_was_cancelled)
