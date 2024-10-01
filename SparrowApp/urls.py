from django.urls import path
from SparrowApp import views
urlpatterns= [
    path('home/',views.home,name='home'),
    path('add_category/',views.add_category,name='add_category'),
    path('add_product/',views.add_product,name='add_product'),
    path('save_category/',views.save_category,name='save_category'),
    path('save_product/',views.save_product,name='save_product'),
    path('category_details/',views.category_details,name='category_details'),
    path('product_details/',views.product_details,name='product_details'),
    path('edit_category/<int:category_id>',views.edit_category,name='edit_category'),
    path('edit_product/<int:pro_id>',views.edit_product,name='edit_product'),
    path('update_category/<int:category_id>',views.update_category,name='update_category'),
    path('update_product/<int:pro_id>',views.update_product,name='update_product'),
    path('delete_category/<int:category_id>',views.delete_category,name='delete_category'),
    path('delete_product/<int:pro_id>',views.delete_product,name='delete_product'),
    path('admin_loginpage/',views.admin_loginpage,name='admin_loginpage'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('contactdetails/',views.contactdetails,name='contactdetails'),
    path('user_login_data/',views.user_login_data,name='user_login_data'),
    path('deletecontactmessage/<int:contact_id>/',views.deletecontactmessage,name='deletecontactmessage'),
    path('delete_user/<int:user_id>/',views.delete_user,name='delete_user'),

]