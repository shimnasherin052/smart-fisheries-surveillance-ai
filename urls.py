"""Fisheries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, pa
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login_get/',views.login_get),
    path('login_post/',views.login_post),
    path('forgot_passwordget/',views.forgot_passwordget),
    path('forgot_passwordpost/',views.forgot_passwordpost),

    path('adminhome/',views.adminhome),
    path('authority_get/',views.authority_get),
    path('authority_post/',views.authority_post),
    path('addnotification_get/',views.addnotification_get),
    path('viewnotification_get/',views.viewnotification_get),
    path('addnotification_post/',views.addnotification_post),
    path('deletenotification_get/<id>',views.deletenotification_get),
    path('add_rescueteam_get/',views.add_rescueteam_get),
    path('add_rescueteam_post/',views.add_rescueteam_post),
    path('editauthority_get/<id>',views.editauthority_get),
    path('editauthority_post/',views.editauthority_post),
    path('editrescueteam_get/<id>',views.editrescueteam_get),
    path('editrescueteam_post/',views.editrescueteam_post),
    path('viewalert_get/',views.viewalert_get),
    path('viewauthority_get/',views.viewauthority_get),
    path('viewcomplaint_get/',views.viewcomplaint_get),
    path('sendreply_get/<id>',views.sendreply_get),
    path('sendreply_post/',views.sendreply_post),
    path('viewrescue_get/',views.viewrescue_get),
    path('delete_rescue/<id>',views.delete_rescue),
    path('viewuser_get/',views.viewuser_get),
    path('deleteauthority_get/<id>',views.deleteauthority_get),
    path('change_password_post/',views.change_password_post),
    path('change_password_get/',views.change_password_get),
    path('loginpage_get/',views.loginpage_get),


    # A U T H O R I T Y--------------------------
    path('authority_index_get/',views.authority_index_get),
    path('authority_addzone_get/',views.authority_addzone_get),
    path('authority_addzone_post/',views.authority_addzone_post),
    path('authority_delete_zone/<id>',views.authority_delete_zone),
    path('authority_editzone_get/<id>',views.authority_editzone_get),
    path('authority_editzone_post/',views.authority_editzone_post),
    path('authority_viewzone_get/',views.authority_viewzone_get),
    path('authority_viewalert_get/',views.authority_viewalert_get),
    path('authority_viewhelprequest_get/',views.authority_viewhelprequest_get),
    path('authority_viewnotification_get/',views.authority_viewnotification_get),
    path('authority_viewprofile_get/',views.authority_viewprofile_get),
    path('authority_addbanschedule_get/',views.authority_addbanschedule_get),
    path('authority_addbanschedule_post/',views.authority_addbanschedule_post),
    path('banschedule_delete/<id>',views.banschedule_delete),
    path('authority_editbanschedule_get/<id>',views.authority_editbanschedule_get),
    path('authority_editbanschedule_post/',views.authority_editbanschedule_post),
    path('authority_viewbanschedule/',views.authority_viewbanschedule),
    path('authority_viewrescueteam_get/',views.authority_viewrescueteam_get),
    path('authority_addboat_owners/',views.authority_addboat_owners),
    path('authority_viewboatowners/',views.authority_viewboatowners),
    path('authority_addboat_ownersget/',views.authority_addboat_ownersget),
    path('authority_editboat_ownersget/<id>',views.authority_editboat_ownersget),
    path('authority_editboat_owners/',views.authority_editboat_owners),
    path('delete_boatowner/<id>',views.delete_boatowner),

#     A N D R O I D---------------------------

    path('app_login/', views.app_login),
    path('user_signup/', views.user_signup),
    path('user_viewprofile/', views.user_viewprofile),
    path('user_editprofile/', views.user_editprofile),
    path('user_viewzones/', views.user_viewzones),
    path('user_viewbanschedule/', views.user_viewbanschedule),
    path('user_viewalert/', views.user_viewalert),
    path('user_viewrescueteam/', views.user_viewrescueteam),
    path('user_sendhelp_request/', views.user_sendhelp_request),
    path('user_viewhelpStatus/', views.user_viewhelpStatus),
    path('userviewnotification/', views.userviewnotification),
    path('view_fine/', views.view_fine),
    path('userchange_password/', views.userchange_password),
    path('boatowners/', views.boatowners),


    path('rescueviewprofile/', views.rescueviewprofile),
    path('rescue_viewzones/', views.rescue_viewzones),
    path('rescue_viewbanschedule/', views.rescue_viewbanschedule),
    path('rescue_viewalert/', views.rescue_viewalert),
    path('rescue_viewhelprequest/', views.rescue_viewhelprequest),
    path('rescueviewnotification/', views.rescueviewnotification),
    path('view_notification/', views.get_new_notifications),
    path('banzonealert_/', views.banzonealert_),
    path('update_status/', views.update_status),
    path('forgot_password/', views.forgot_password),
    path('forgotpassword_post/', views.forgotpassword_post),
    path('android_forget_password_post/', views.android_forget_password_post),
    path('help_update_status/', views.help_update_status),
    path('user_viewprofilehome_page/', views.user_viewprofilehome_page),
    path('rescueviewprofilehome_page/', views.rescueviewprofilehome_page),
    path('view_reply/', views.view_reply),
    path('user_sendcomplaint/', views.user_sendcomplaint),
    path('auth_change_password_post/', views.auth_change_password_post),
    path('auth_change_password_get/', views.auth_change_password_get),
    path('authority_viewnotification_get/', views.authority_viewnotification_get),
    path('rescue_update_all_alerts/', views.rescue_update_all_alerts),
    path('fetchcount/', views.fetchcount),



]
