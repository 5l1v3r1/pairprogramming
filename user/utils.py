from .models import User
from github import Github
import string
import random


def user_exists(user_name):

    try:
        user = User.objects.get(user_name=user_name)
    except (KeyError, User.DoesNotExist):
        return False
    return True


def create_user(user_name, github_token):

    user = User.objects.create(user_name=user_name)
    user.save()
    return


def login_user(user_name, password):

    git = None
    if user_exists(user_name):
        user = User.objects.get(user_name=user_name)
        github_token = user.user_github_token
        git = Github(github_token)
    else:
        git = Github(user_name, password)
        print(git.oauth_scopes)
        create_user(user_name, "token")

    return
