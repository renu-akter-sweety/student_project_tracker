from django.contrib import admin
from django.urls import path
from project_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", signuppage, name="sign_upurl"),
    path("base/", basepage, name="baseurl"),
    path("log_in/", loginpage, name="log_inurl"),
    path("log_out/", log_outpage, name="log_outurl"),
    path("addproject/", addproject, name="addprojecturl"),
    path("edit/<int:id>/", editproject, name="editprojecturl"),
    path("delete/<int:id>/", deleteproject, name="deleteprojecturl"),
    path("log_out/", log_outpage, name="log_outurl"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

