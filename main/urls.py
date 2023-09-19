from django.urls import path
from main.views import index, add_product, show_products_json, show_product_xml, show_product_json_by_id, show_product_xml_by_id
from django.conf.urls.static import static
from inventory_app.settings import STATIC_URL, STATIC_ROOT

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('add-product/', add_product, name='add_product'),
    path('json/', show_products_json, name='show_products_json'),
    path('xml/', show_product_xml, name='show_product_xml'),
    path('json/<int:id>/',
         show_product_json_by_id, name='show_product_json_by_id'),
    path('xml/<int:id>/',
         show_product_xml_by_id, name='show_product_xml_by_id'),
]
