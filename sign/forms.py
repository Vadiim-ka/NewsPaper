from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BasicSignupFoRM(SignupForm):

    def save(self, request):
        user = super(BasicSignupFoRM, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user
