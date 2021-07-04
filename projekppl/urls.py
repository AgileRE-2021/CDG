"""projekppl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.splash, name='splash' ),
    path('home', views.home, name='home' ),
    path('user_manual',views.manual, name='manual'),

# ==== crud ====
#add proyek
    path('tambah_proyek', views.tambah_proyek),
    path('ganti_proyek/<int:id>', views.ganti_proyek),
    path('destroy_proyek/<int:id>', views.destroy_proyek),
#add proses
    path('translasi/<int:id>', views.translasi, name='translasi_proses'),
    path('tambah_proses/<int:id>', views.tambah_proses, name='tambah_proses'),
    path('ganti_proses/<int:id>', views.ganti_proses),
    path('destroy_proses/<int:id>', views.destroy_proses),
    path('upload_bpmn/<int:id>', views.upload_bpmn),
#add database
    path('database/<int:id>', views.database),
    path('upload_database/<int:id>', views.upload_database),

#hasildonlot
    path('hasil/<int:id>', views.hasil, name='hasil'),
    path('hasil', views.hasilall, name='hasilall'),

#donlot
    path('download/<int:id>', views.download, name='download'),
    path('download-png/<int:id>', views.downloadpng, name='downloadpng'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)