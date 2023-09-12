from django.urls import path
from main.views import index
from django.conf.urls.static import static
from inventory_app.settings import STATIC_URL, STATIC_ROOT

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
] + static(STATIC_URL, document_root=STATIC_ROOT) 