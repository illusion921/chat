from django.contrib import admin
import models
# Register your models here.



admin.site.register(models.UserProfile)
admin.site.register(models.ChatGroup)
#admin.site.register(models.UserGroup)
admin.site.register(models.ChatRecord)
admin.site.register(models.SengImg)
admin.site.register(models.Confirm)