from django.db.models.signals import pre_save, post_save, pre_delete, post_delete, pre_init, post_init
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.core.signals import request_started, request_finished, got_request_exception



@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwagrs):
    print("......................")
    print("Loged-in signal... run intro...")
    print("sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'kwargs: {kwagrs} ')


@receiver(user_logged_out, sender = User)
def login_out(sender, request, user, **kwagrs):
    print("......................")
    print("Loged-out signal... run intro...")
    print("sender:", sender)
    print("Request:", request)
    print("User:", user)
    print(f'kwargs: {kwagrs} ')


@receiver(user_login_failed)
def login_failed(sender, request, credentials, **kwagrs):
    print("......................")
    print("Loged-failed signal... ")
    print("sender:", sender)
    print("Credentials:", credentials)
    print("Request:", request)
    print(f'kwargs: {kwagrs} ')



@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):
    print(".............")
    print("pre save signal")
    print("sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs: {kwargs}')


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print(".............")
        print("post save signal")
        print("New Record")
        print("sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'Kwargs: {kwargs}')
    else:
        print("post save signal")
        print("Update")
        print("sender:", sender)
        print("Instance:", instance)
        print("Created:", created)
        print(f'Kwargs: {kwargs}')


@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):
    print(".....................")
    print("pre delete signal...")
    print("Sender:", sender)
    print("instance:", instance)
    print(f'kwargs: {kwargs}')


@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print(".....................")
    print("post delete...")
    print("Sender:", sender)
    print("instance:", instance)
    print(f'kwargs: {kwargs}')


@receiver(pre_init, sender=User)
def at_beginning_init(sender, *args, **kwargs):
    print(".....................")
    print("pre init signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')


@receiver(post_init, sender=User)
def at_ending_init(sender, *args, **kwargs):
    print(".....................")
    print("post init signal...")
    print("Sender:", sender)
    print(f'Args: {args}')
    print(f'kwargs: {kwargs}')


@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):
    print("..................")
    print("At Beginning Request.....")
    print('sender:', sender)
    print('Environ:', environ)
    print(f'Kwargs: {kwargs}')


@receiver(request_finished)
def at_ending_request(sender, **kwargs):
    print("..................")
    print("At Ending Request.....")
    print('sender:', sender)
    print(f'Kwargs: {kwargs}')


@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print("..................")
    print("At Request Exception.....")
    print('sender:', sender)
    print('request:', request)
    print(f'Kwargs: {kwargs}')


