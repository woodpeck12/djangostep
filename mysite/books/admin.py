from django.contrib import admin

# Register your models here.
from .models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title','publisher','publication_date')
	list_filter = ('publication_date',)
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	fields = ('title','publisher','authors','publication_date')  #woodpeck..can change order of field of edit page
	filter_horizontal = ('authors',) ##woodpeck - to provide multiple selction easier(many to many only is the best)
	raw_id_fields = ('publisher',) ##woodpeck - for foreign key to show easier to edit/select

admin.site.register(Publisher)  ##woodpeck - just default
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)