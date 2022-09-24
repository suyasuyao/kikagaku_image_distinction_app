from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.index, name='index'),
    path('input_form/', views.input_form, name='input_form'),
    path('result/', views.result, name='result'),
    path('history/', views.history, name='history'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'), # 追加

    path('', views.image_upload, name='image_upload'),
    path('img_url/', views.image_upload, name='image_upload'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)