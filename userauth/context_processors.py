from .models import User, Profile


def default(request):
    user = User.objects.all()
    profile = Profile.objects.all()

    return {
        'profile': profile,
    }
