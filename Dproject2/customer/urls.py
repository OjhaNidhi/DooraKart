from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import sendOtp,verifyOtp

app_name = 'customer'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('subcategories/', views.subcategories, name = 'subcategories'),
    path('helper/', views.helper, name = 'helper'),
    path('home/<str:category>/', views.products, name = 'products'),
    re_path(r'price/$', views.get_price, name='price'),
    path('api/send_otp',sendOtp.as_view()),
    path('api/verify_otp',verifyOtp.as_view()),
    # re_path(r'filter/$', views.filter, name='filter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
