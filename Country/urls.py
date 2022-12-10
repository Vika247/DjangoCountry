from django.urls import path
from MainApp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('countries-list/', views.countries_list, name="countries-list"),
    path('country/<str:id>', views.country, name="country"),
    path('countries/<str:buc>', views.countries_buc, name="countries_buc"),
    path('lenguages/', views.lenguages, name="lenguages"),
    path('lenguag/<str:len>', views.lenguag, name="lenguag"),
]
