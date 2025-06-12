from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.shortcuts import redirect

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('polls:index')),  # Redirect root URL to polls index
]

# Only include the debug toolbar in development mode
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
