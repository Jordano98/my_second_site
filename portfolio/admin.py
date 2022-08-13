from django.contrib import admin

from portfolio.models import Pro_Category,Pro_Gallery,Project

class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('pro_name','client','project_date','project_url','title','created_date')
    list_filter = ('pro_name','project_date')
    search_fields = ['title','content']

admin.site.register(Project, ProjectAdmin)

admin.site.register(Pro_Category)
admin.site.register(Pro_Gallery)

# Register your models here.
