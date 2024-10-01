from django.urls import path
from frontendApp import views

urlpatterns=[
    path('webindex',views.webindex,name='webindex'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('save_contact_message/',views.save_contact_message,name='save_contact_message'),
    path('productlist/',views.productlist,name='productlist'),
    path('filtered_products/<cat_name>',views.filtered_products,name='filtered_products'),
    path('single_product/<int:pro_id>/',views.single_product,name='single_product'),
    path('',views.login_page,name='login_page'),
    path('save_user_signup',views.save_user_signup,name='save_user_signup'),
    path('user_login',views.user_login,name='user_login'),
    path('logout_user',views.logout_user,name='logout_user'),
    path('addtocart',views.addtocart,name='addtocart'),
    path('cartpage/',views.cartpage,name='cartpage'),
    path('deletecartitem/<int:dataid>/',views.deletecartitem,name='deletecartitem'),
    path('checkout',views.checkout,name='checkout'),
    path('save_checkout_data',views.save_checkout_data,name='save_checkout_data'),
    path('payment',views.payment,name='payment'),
]