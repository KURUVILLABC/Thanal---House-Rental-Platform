"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    ##################### ADMIN ################################
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_house_type_add', views.admin_house_type_add, name='admin_house_type_add'),
    path('admin_house_type_view', views.admin_house_type_view, name='admin_house_type_view'),
    path('admin_house_type_delete', views.admin_house_type_delete, name='admin_house_type_delete'),
    path('admin_house_type_edit', views.admin_house_type_edit, name='admin_house_type_edit'),

    path('admin_user_details_view', views.admin_user_details_view, name='admin_user_details_view'),
    path('admin_user_details_delete', views.admin_user_details_delete, name='admin_user_details_delete'),
    path('admin_user_docs_view', views.admin_user_docs_view, name='admin_user_docs_view'),


    path('admin_owner_details_pending_view', views.admin_owner_details_pending_view, name='admin_owner_details_pending_view'),
    path('admin_owner_details_delete', views.admin_owner_details_delete, name='admin_owner_details_delete'),
    path('admin_owner_details_view', views.admin_owner_details_view, name='admin_owner_details_view'),
    path('admin_owner_details_register_update', views.admin_owner_details_register_update, name='admin_owner_details_register_update'),

    path('admin_house_details_pending_view', views.admin_house_details_pending_view, name='admin_house_details_pending_view'),
    path('admin_house_details_register_update', views.admin_house_details_register_update, name='admin_house_details_register_update'),

    path('admin_house_search', views.admin_house_search, name='admin_house_search'),


    path('owner_house_pic_add', views.owner_house_pic_add, name='owner_house_pic_add'),
    path('owner_house_pic_delete', views.owner_house_pic_delete, name='owner_house_pic_delete'),
    path('owner_house_pic_view', views.owner_house_pic_view, name='owner_house_pic_view'),

    ##################################### OWNER ##############################
    path('owner_login', views.owner_login_check, name='owner_login'),
    path('owner_logout', views.owner_logout, name='owner_logout'),
    path('owner_home', views.owner_home, name='owner_home'),
    path('owner_details_add', views.owner_details_add, name='owner_details_add'),
    path('owner_changepassword', views.owner_changepassword, name='owner_changepassword'),
    path('owner_profile_view', views.owner_profile_view, name='owner_profile_view'),

    path('owner_house_details_add', views.owner_house_details_add, name='owner_house_details_add'),
    path('owner_house_details_view', views.owner_house_details_view, name='owner_house_details_view'),
    path('owner_house_details_delete', views.owner_house_details_delete, name='owner_house_details_delete'),
    path('owner_house_details_edit', views.owner_house_details_edit, name='owner_house_details_edit'),
    path('owner_house_details_pending_view', views.owner_house_details_pending_view, name='owner_house_details_pending_view'),
    path('owner_house_details_rejected_view', views.owner_house_details_rejected_view, name='owner_house_details_rejected_view'),

    path('owner_house_request_view', views.owner_house_request_view, name='owner_house_request_view'),
    path('owner_house_request_view2', views.owner_house_request_view2, name='owner_house_request_view2'),
    path('owner_user_docs_view', views.owner_user_docs_view, name='owner_user_docs_view'),
    path('owner_house_request_update', views.owner_house_request_update, name='owner_house_request_update'),

    path('owner_house_messages_view', views.owner_house_messages_view, name='owner_house_messages_view'),
    path('owner_house_messages_add', views.owner_house_messages_add, name='owner_house_messages_add'),

    path('owner_house_agreement_add', views.owner_house_agreement_add, name='owner_house_agreement_add'),
    path('owner_house_agreement_pending_view', views.owner_house_agreement_pending_view, name='owner_house_agreement_pending_view'),
    path('owner_house_agreement_active_view', views.owner_house_agreement_active_view, name='owner_house_agreement_active_view'),
    path('owner_house_agreement_report_view', views.owner_house_agreement_report_view, name='owner_house_agreement_report_view'),

    path('owner_transaction_details_view', views.owner_transaction_details_view, name='owner_transaction_details_view'),

    path('owner_user_details_view', views.owner_user_details_view, name='owner_user_details_view'),

    ##################### USER #########################################
    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_details_update', views.user_details_update, name='user_details_update'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('user_docs_view', views.user_docs_view, name='user_docs_view'),
    path('user_docs_delete', views.user_docs_delete, name='user_docs_delete'),
    path('user_docs_add', views.user_docs_add, name='user_docs_add'),

    path('user_house_search', views.user_house_search, name='user_house_search'),
    path('user_house_pic_view', views.user_house_pic_view, name='user_house_pic_view'),

    path('user_feedback_all_view', views.user_feedback_all_view, name='user_feedback_all_view'),
    path('user_feedback_add', views.user_feedback_add, name='user_feedback_add'),
    path('user_feedback_view', views.user_feedback_view, name='user_feedback_view'),
    path('user_feedback_delete', views.user_feedback_delete, name='user_feedback_delete'),

    path('user_house_request_add', views.user_house_request_add, name='user_house_request_add'),
    path('user_house_request_delete', views.user_house_request_delete, name='user_house_request_delete'),
    path('user_house_request_view', views.user_house_request_view, name='user_house_request_view'),
    path('user_house_request_report_view', views.user_house_request_report_view, name='user_house_request_report_view'),

    path('user_house_messages_add', views.user_house_messages_add, name='user_house_messages_add'),
    path('user_house_messages_view', views.user_house_messages_view, name='user_house_messages_view'),

    path('user_house_agreement_pending_view', views.user_house_agreement_pending_view, name='user_house_agreement_pending_view'),
    path('user_house_agreement_report_view', views.user_house_agreement_report_view, name='user_house_agreement_report_view'),
    path('user_house_agreement_active_view', views.user_house_agreement_active_view, name='user_house_agreement_active_view'),


    path('user_agreement_payment_add', views.user_agreement_payment_add, name='user_agreement_payment_add'),
    path('user_rent_payment_add', views.user_rent_payment_add, name='user_rent_payment_add'),
    path('user_transaction_details_view', views.user_transaction_details_view, name='user_transaction_details_view'),
    path('user_transaction_details_house_view', views.user_transaction_details_house_view, name='user_transaction_details_house_view'),

    path('user_house_pool_advertisement_add', views.user_house_pool_advertisement_add, name='user_house_pool_advertisement_add'),
    path('user_house_pool_advertisement_view', views.user_house_pool_advertisement_view, name='user_house_pool_advertisement_view'),

    path('user_house_pool_advertisement_all_view', views.user_house_pool_advertisement_all_view, name='user_house_pool_advertisement_all_view'),

    path('user_house_pooling_request_add', views.user_house_pooling_request_add, name='user_house_pooling_request_add'),
    path('user_house_pooling_request_report_view', views.user_house_pooling_request_report_view, name='user_house_pooling_request_report_view'),
    path('user_house_pooling_request_pending_view', views.user_house_pooling_request_pending_view, name='user_house_pooling_request_pending_view'),
    path('user_house_pooling_request_view', views.user_house_pooling_request_view, name='user_house_pooling_request_view'),
    path('user_house_pooling_request_update', views.user_house_pooling_request_update, name='user_house_pooling_request_update'),

    path('user_notifications_view', views.user_notifications_view, name='user_notifications_view'),

]
