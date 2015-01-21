from django.contrib import admin
from joins.models import Join


class JoinAdmin(admin.ModelAdmin):
    list_display = ('email', 'ref_id', 'friends', 'ip_address', 'timestamp', 'updated')


class JoinFriendsAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Join, JoinAdmin)