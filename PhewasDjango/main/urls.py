from django.urls  import path
from .views import PheWas_List ,PheWas_List_2

urlpatterns = [
    path("phewas/", PheWas_List),
    path("phewas2/", PheWas_List_2),
]