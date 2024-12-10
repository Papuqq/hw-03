from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .models import Post, PostCategory
from .tasks import generation_and_sending_mail


@receiver(m2m_changed, sender=PostCategory)
def product_created(instance, action, **kwargs):
    if action != 'post_add':
        return
    generation_and_sending_mail.delay(instance.pk)
