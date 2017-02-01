from __future__ import unicode_literals

from django.db import models
from django.contrib import messages
import bcrypt


# Create your models here.

class UserManager(models.Manager):
    def register(self, request):
        # get the values from the form

        is_valid = True

        if len(request.POST['first_name']) == 0:
            messages.error(request, "First Name is required");
            is_valid = False;

        if len(request.POST['email']) == 0:
            messages.error(request, "E-mail is required")
            is_valid = False

        email_match = User.objects.filter(email=request.POST['email'])

        if len(email_match) > 0:
            messages.error(request, "That email is already in use")
            is_valid = False;

        if request.POST['password'] != request.POST['password_confirm']:
            messages.error(request, "The passwords don't match")
            is_valid = False

        if not is_valid:
            return False


        hashed = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt())

        new_user = User(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            pwhash = hashed,
        )
        new_user.save()

        request.session["logged_in_user"] = new_user.id

        return True
    def login(self, request):
        # validation


        # does the user exist?
        users = User.objects.filter(email=request.POST['email'])

        if len(users) == 0:
            messages.error(request, "That user does not exist");
            return False

        user = users[0]

        hashed3 = bcrypt.hashpw(request.POST['password'].encode('utf-8'),user.pwhash.encode('utf-8'))

        if hashed3 != user.pwhash:
            messages.error(request, "That password is incorrect");
            return False

        request.session["logged_in_user"] = user.id

        return True

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    pwhash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
