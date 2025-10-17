from django.contrib import admin
from project_app.models import *

# Register your models here.
admin.site.register([UserModel,ProjectModel])