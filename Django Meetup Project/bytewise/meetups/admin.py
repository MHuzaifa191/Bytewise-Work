from django.contrib import admin

from .models import Meetup
from .models import Location
from .models import Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ("title", "date",)
    list_filter = ('date', 'location')
    prepopulated_fields = {
        'slug' : ('title', )
    }


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)
