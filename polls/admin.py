from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
  model=Choice
  extra=3

# admin.site.register(Poll)
class PollAdmin(admin.ModelAdmin):
  #fields = ['pub_date','question']
  fieldsets = [
    (None,               {'fields': ['question']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('question','pub_date','was_published_today')
  list_filter = ['pub_date']
  search_fields = ['question']
  date_hierarchy = 'pub_date'

admin.site.register(Poll,PollAdmin)



#admin.site.register(Choice)
