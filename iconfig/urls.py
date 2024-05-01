from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    path("", include("store.urls")),
    # path("cart/", include("cart.urls")),
    # path("checkout/", include("checkout.urls")),
    # path("account/", include("account.urls")),
    # path("search/", include("search.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
