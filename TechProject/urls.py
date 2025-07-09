from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import ckeditor_upload
from Blog.views.article import ask_ai

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ask-ai/", ask_ai, name="ask_ai"),
    path("ckeditor/upload/", ckeditor_upload.upload, name="ckeditor_upload"),
    path("ckeditor/browse/", ckeditor_upload.browse, name="ckeditor_browse"),
    path("", include("Blog.urls.article"), name="home"),
    path("", include("users.urls.auth")),
    path("", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler403 = "core.views.permission_denied_view"
handler404 = "core.views.page_not_found_view"
handler500 = "core.views.server_error_view"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
