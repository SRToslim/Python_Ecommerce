from .models import Currency


def default(request):
    currencies = Currency.objects.all()

    return {
        'currencies': currencies,
    }
