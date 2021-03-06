"""Users app admin classes."""
#Django
from django.contrib.auth.admin import UserAdmin as baseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
#Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number','picture')
    search_fields = ('user__email',
    'user__first_name',
    'user__last_name',
    'phone_number'
    )
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'create',    
        'modified'
    )

    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),)
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography')
            )
        }),
        ('Metadata',{
            'fields': (('create','modified'),),
        })
    )

    readonly_fields = ('create','modified',)

class ProfileInLine(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Profile
    can_delete = False
    verbose_name = 'profiles'

class UserAdmin(baseUserAdmin):
    """Profile admin to base user admin."""

    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

class Report(baseUserAdmin):
    list_display = ('report')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)