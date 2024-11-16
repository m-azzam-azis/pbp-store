from django.urls import path
from main.views import show_main, create_shop_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_shop_item, delete_shop_item
from main.views import add_shop_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    
    path('create-shop-entry', create_shop_entry, name='create_shop_entry'),
    
    path('xml/', show_xml, name='show_xml'),

    path('json/', show_json, name='show_json'),

    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    
    path('register', register, name='register'),
    
    path('login', login_user, name='login'),
    
    path('logout', logout_user, name='logout'),
    
    path('edit-shop-item/<uuid:id>', edit_shop_item, name='edit_shop_item'),
    
    path('delete-shop-item/<uuid:id>', delete_shop_item, name='delete_shop_item'),
    
    path('add-shop-entry-ajax', add_shop_entry_ajax, name='add_shop_entry_ajax'),    


    
]