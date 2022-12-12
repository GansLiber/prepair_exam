from django.contrib import admin
from django.urls import path
from new_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:type_slave>', views.get_number),
    path('<str:type_slave>', views.get_type_slave),
]
