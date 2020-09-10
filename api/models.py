from django.db import models
from django.core.mail import send_mail
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.dispatch import receiver


class Movie(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='movie_user')
    title = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=255, blank=True)
    year = models.DateTimeField()

    def __str__(self):
        return self.title


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintxt_msg = "{}?token={}".format(reverse('api:password_reset:reset-password-request'), reset_password_token.key)
    send_mail(
        "Password reset for {title}".format(title="Nexis Systems"),
        email_plaintxt_msg,
        "noreply@nexis.co.za",
        ['todayy06@gmail.com']
    )
