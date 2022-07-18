from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.hashers import check_password




User=get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            user=User.objects.get(Q(username=username) | Q(email=username) | Q(phone=username))
        except User.DoesNotExist:
            #User().set_password(password)
            return  None
        if user and check_password(user, user.password):
            return user
        # if user.check_password(password) and self.user_can_authenticate(user):
        #     return user
        else:
            return None