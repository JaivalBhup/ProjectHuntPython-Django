
from django.contrib import admin
from django.urls import path, include
from products import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('account/', include('account.urls'), name='account'),
    path('project/', include('products.urls'), name='products'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
