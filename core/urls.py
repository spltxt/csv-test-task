from django.urls import path
from core.views import create_upload, ProductList

app_name = 'core'

urlpatterns = [
    path('upload/', create_upload, name='upload'),
    path('product_list/', ProductList.as_view(), name='products')
]