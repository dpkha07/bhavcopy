from django.urls import path
from . import views

urlpatterns = [
    path('extract_ohlc/', views.extract_ohlc, name='extract_ohlc'),
    path('equity_list/', views.equity_list, name='equity_list'),
    path('download_csv/', views.download_csv, name='download_csv'),
    path('update_equity/', views.update_equity, name='update_equity'),
    path('delete_equity/', views.delete_equity, name='delete_equity'),
]