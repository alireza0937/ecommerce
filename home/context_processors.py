from category.models import Category


def all_categories():
    links = Category.objects.all()
    return dict(links=links)
