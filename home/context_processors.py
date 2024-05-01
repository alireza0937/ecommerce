from category.models import Category


def all_categories(request):
    links = Category.objects.all()
    return dict(links=links)