from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=16,unique=True)
    #user_group = models.ManyToManyField('UserGroup')
    chat_group = models.ManyToManyField('ChatGroup',blank=True)
    friends = models.ManyToManyField('self',blank=True,related_name='user_friends')
    online = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

class ChatGroup(models.Model):
    group_name = models.CharField(max_length=16,unique=True)
    founder = models.ForeignKey(UserProfile)
    members = models.ManyToManyField('UserProfile',related_name='group_members')
    admins = models.ManyToManyField('UserProfile',related_name='group_admins')
    members_limit = models.IntegerField(default=200)

    def __unicode__(self):
        return self.group_name

class ChatRecord(models.Model):
    user = models.ForeignKey(UserProfile,related_name='user_record')
    to_user = models.ForeignKey(UserProfile,related_name='to_user_record')
    send_type = models.CharField(max_length=20)
    record_time = models.CharField(max_length=100)
    msg_data = models.CharField(max_length=100)
    msg_img = models.ImageField(blank=True,upload_to=os.path.join(BASE_DIR,'statics','imgs'))

    def __str__(self):
        return self.msg_data

class SengImg(models.Model):
    user = models.ForeignKey(UserProfile)
    to_user = models.ForeignKey(UserProfile,related_name='img_to_user')
    file_name = models.CharField(max_length=100,default = 'files')
    msg_img = models.FileField(upload_to=os.path.join(BASE_DIR,'statics','files'),blank=True)
    add_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.file_name

class Confirm(models.Model):
    user = models.ForeignKey(UserProfile)
    add_user = models.ForeignKey(UserProfile,related_name='confirm_add_user')
    type = models.CharField(max_length=20)
    is_new = models.BooleanField(default=True)
    status  = models.BooleanField(default=False)

    def __str__(self):
        return self.type