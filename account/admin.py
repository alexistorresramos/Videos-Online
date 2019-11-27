from django.contrib import admin

# Register your models here.
from .models import Destination2, Book, Category, Videos_sold, Sales_Factor
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, News_Type, UserProfile, Country

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.

admin.site.register(Destination2)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Videos_sold)
admin.site.register(Sales_Factor)
admin.site.register(News_Type)
admin.site.register(UserProfile)
admin.site.register(Country)
