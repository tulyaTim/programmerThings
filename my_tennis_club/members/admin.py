from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstName", "lastName", "joined_date")
    prepopulated_fields = {"slug": ("firstName", "lastName")}

admin.site.register(Member, MemberAdmin)