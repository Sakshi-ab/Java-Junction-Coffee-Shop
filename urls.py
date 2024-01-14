from django.contrib import admin
from django.urls import path
from javajunctionapp import views
from django.conf import settings
from django.conf.urls.static import static
from .views import view_orders
from .views import view_order_status
urlpatterns = [
    path('create',views.create),
    path('dashboard',views.dashboard, name='dashboard'),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('', views.index, name='index'),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('about.html', views.about, name='about'),
    path('place_order/<pid>', views.place_order, name='place_order'),
    path('view_orders/', view_orders, name='view_orders'),
    path('view_order_status/', view_order_status, name='view_order_status'),
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)