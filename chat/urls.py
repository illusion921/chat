"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from web_chat import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.Index),
    url(r'^login/',views.Login,name='login'),
    url(r'^quit/',views.Quit,name='quit'),
    url(r'^register/',views.Register,name='register'),
    url(r'^upload/$',views.Upload,name='upload'),
    url(r'^get_msg/$',views.GetMsg,name='get_msg'),
    url(r'^send_img/$',views.SendImg,name='send_img'),
    url(r'^search/$',views.Search,name='search'),
    url(r'^add/$',views.AddFriend,name='add_fri'),
    url(r'^record/$',views.Record,name='chat_record'),
    url(r'^msg_img/$',views.ChatImg,name='imgs'),
    url(r'^chatgroup/$',views.ChatGroup,name='group'),
    url(r'^chgpwd/$',views.ChgPwd,name='chgpwd'),
    url(r'^confirm/$',views.Confirm,name='confirm'),
    url(r'^addsignal/$',views.AddSignal,name='add_signal'),
    url(r'^refuse/$',views.Refuse,name='refuse'),
    url(r'^del_user/$',views.DelUser,name='del_user'),
    #url(r'^create/$',views.,name='group'),
]
