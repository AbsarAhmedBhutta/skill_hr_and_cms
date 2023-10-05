from django.contrib import admin
from django.urls import path
from core.settings import DEBUG
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Skill Evokers"  # Change 'Django Administration' to 'Skill Evokers'
admin.site.site_title = "Skill Admin Portal"  # Change the title of the admin portal
admin.site.index_title = "Welcome to Skill Evokers Portal"  # Change the index title

urlpatterns = [
    path('admin/', admin.site.urls),
]
#
if DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)