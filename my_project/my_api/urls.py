from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('auth/', include("my_api.api_auth.urls")),
    path('home/', include("my_api.api_home.urls")),
    path('schema/', get_schema_view(title="my_api", description="Full API", version="1.0.0"), name='openapi-schema'),
    # path('docs/', include_docs_urls(title="my_api")),
]
