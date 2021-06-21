from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

# url patterns
app_name = "tasks"

urlpatterns = [
    path("", index, name="index"),
    path("tasks/", tasks, name="task"),
    path("add/", add, name="add"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)