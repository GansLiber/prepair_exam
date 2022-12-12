from django.urls import path, include

urlpatterns = [
    path('slaves/', include('new_app.urls')),
]