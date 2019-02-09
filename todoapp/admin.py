from django.contrib import admin

from .models import Todo, UserRegister, User

admin.site.register(Todo)
admin.site.register(UserRegister)
admin.site.register(User)