from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	path('', views.index, name="indexpage"),
	path('first/', views.first, name='Afterlogin'),
	path('docadd/', views.docadd, name='publicdocadd'),
	path('pdocadd/', views.p_docadd, name='privatedocadd'),
	path('doc_access/<int:pid>/', views.doc_access, name='doc_access'),
	path('about/', views.about, name='about'),
	path('doc2/', views.doc2, name='document'),
	path('document/', views.document, name='document'),
	path('contact/', views.contact, name='contact'),
	path('signup/', views.handlesignup, name='signup'),
	path('login/', views.handlesignin, name='login'),
	path('logout/', views.handlelogout, name='logout'),
	path('doc1/', views.doc1, name='all_docs'),
	path('del/<int:docid>/', views.doc_delete, name="doc_delete"),
	path('pdel/<int:pdocid>/', views.pdoc_delete, name="pdoc_delete"),

	path('reset_password/', 
		auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
		name='reset_password'),

	path('reset_password_sent/', 
		auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
		name='password_reset_done'),
	
	path('reset/<uidb64>/<token>/', 
		auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
		name='password_reset_confirm'),
	
	path('reset_password_complete/', 
		auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
		name='password_reset_complete'),

]
