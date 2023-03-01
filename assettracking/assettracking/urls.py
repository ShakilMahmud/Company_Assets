
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Redirect Route to asset_app urls....
    path('', include('asset_app.urls')),
]
