from django.urls  import path
from .views import PheWas_List

urlpatterns = [
    path("phewas/", PheWas_List),
]