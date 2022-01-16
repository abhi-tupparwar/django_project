from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

SchemaView = get_schema_view(
    openapi.Info(
        title="Your App API",
        default_version="v1",
        description="For the Android app and web app.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="abhitupparwar@gmail/com"),
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'swagger-ui/', staff_member_required(SchemaView.with_ui('swagger', cache_timeout=0)),
        name='schema-swagger-ui'
    ),
    path('', include('apps.urls')),  # entry point to other project app urls
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
