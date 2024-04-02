from .models import Gender


def gender_and_categories(request):
    return {
        "genders": Gender.objects.all().prefetch_related('categories')
    }