from django.urls import path
from main.views import index, create_product_flutter, register, create_ajax, delete, login_user, increment, decrement, logout_user, add_product, show_products_json, show_product_xml, show_product_json_by_id, show_product_xml_by_id

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
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment/<int:id>/', increment, name='increment'),
    path('decrement/<int:id>/', decrement, name='decrement'),
    path('delete/<int:id>/', delete, name='delete'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter')
]
