from django.contrib import admin

# Register your models here.


admin.site.site_header = 'Boat'

admin.site.site_title = 'Boat'

admin.site.index_title = 'Boat'


# Register your models here.
from users.models import Cargo_Card, TC_Card, Tonnage_Card


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


admin.site.register(Cargo_Card)
admin.site.register(TC_Card)
admin.site.register(Tonnage_Card)