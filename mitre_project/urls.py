from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path

from adversary_techniques.views import get_subtechniques, LikelyAdversaryGroupsView

from techniques.views import search_tactics

from sub_techniques.views import search_techniques

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_tactics/', search_tactics, name='search_tactics'),
    path('search_techniques/', search_techniques, name='search_techniques'),
    path('admin/get_subtechniques/', get_subtechniques, name='get_subtechniques'),
    path('likely-groups', LikelyAdversaryGroupsView.as_view(), name='likely-groups')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
