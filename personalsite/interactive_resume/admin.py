from django.contrib import admin

from . import models



class ContactAdmin(admin.ModelAdmin):
    list_display = (['contact_service_name'])

class EducationAdmin(admin.ModelAdmin):
    list_display = (['school_name'])

class JobHistoryInfoInline(admin.TabularInline):
    model = models.JobHistoryInfo
    extra = 0

class JobHistoryAdmin(admin.ModelAdmin):
    list_display = (['employer_name', 'position_title', 'start_date', 'end_date'])

    inlines = [JobHistoryInfoInline]

class ProfileAdmin(admin.ModelAdmin):
    list_display = (['name'])

class ProjectAdmin(admin.ModelAdmin):
    list_display = (['project_title'])

class SkillAdmin(admin.ModelAdmin):
    list_display = (['skill_name'])

class ToolAdmin(admin.ModelAdmin):
    list_display = (['tool_name'])



admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.Education, EducationAdmin)
admin.site.register(models.JobHistory, JobHistoryAdmin)
admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Skill, SkillAdmin)
admin.site.register(models.Tool, ToolAdmin)
