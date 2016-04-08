from django.contrib import admin
from userinfo.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('owner', 'email')
    fields = ('owner',)
    list_filter = ('owner',)
    search_fields = ('owner__username',)
    readonly_fields = ('owner', 'email')

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

