from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("get_user_id",)#("user__id", "user__first_name", "user__last_name", "user__email")

    @admin.display(ordering='user__id', description='id')
    def get_user_id(self, obj):
        return (obj.user.id, obj.user.first_name, obj.user.last_name)




admin.site.register(Profile, ProfileAdmin)
# Register your models here.
