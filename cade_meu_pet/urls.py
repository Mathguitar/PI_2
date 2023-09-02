from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cade_meu_pet import views

urlpatterns = [
    path('', views.index),
    path('encontrados/', views.encontrados, name='encontrados'),
    path('perdidos/', views.perdidos, name='perdidos'),
    path('envio_sucesso/', views.envio_sucesso, name='envio_sucesso'),
    path('form_error/', views.form_error, name='form_error'),
    path('lista_encontrados/', views.lista_encontrados, name='lista_encontrados'),
    path('lista_perdidos/', views.lista_perdidos, name='lista_perdidos'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
