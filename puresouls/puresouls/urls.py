"""puresouls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('FAQ/',views.FAQ,name='FAQ'),
    path('index1/',views.index1, name='index'),
    path('footer/',views.footer,),
    path('help/',views.help,name='help'),
    path('review/',views.review,name='review'),
    path('profile/',views.profile,name='profile'),
    path('header/',views.header,name='sidebar'),
    path('blog/',views.blog,name='blog'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('recoverpassword/',views.recoverpassword,name='recoverpassword'),
    path('base/',views.base,name='base'),
   
    path('logout/',views.logout,name='logout'),
    path('animaltesting/',views.animaltesting,name='animaltesting'),
    path('animaltesting1/',views.animaltesting1,name='animaltesting1'),
    path('animaltesting2/',views.animaltesting2,name='animaltesting2'),
    path('animaltesting3/',views.animaltesting3,name='animaltesting3'),
    path('animaltesting4/',views.animaltesting4,name='animaltesting4'),
    path('animaltesting5/',views.animaltesting5,name='animaltesting5'),

    path('seafoodproduction/',views.seafoodproduction,name='seafoodproduction'),
    path('seafoodproduction1/',views.seafoodproduction1,name='seafoodproduction1'),
    path('seafoodproduction2/',views.seafoodproduction2,name='seafoodproduction2'),
    path('seafoodproduction3/',views.seafoodproduction3,name='seafoodproduction3'),
    path('seafoodproduction4/',views.seafoodproduction4,name='seafoodproduction4'),
    path('seafoodproduction5/',views.seafoodproduction5,name='seafoodproduction5'),
    path('seafoodproduction6/',views.seafoodproduction6,name='seafoodproduction6'),
    path('seafoodproduction7/',views.seafoodproduction7,name='seafoodproduction7'),
    path('seafoodproduction8/',views.seafoodproduction8,name='seafoodproduction8'),

    path('animalslaughter/',views.animalslaughter,name='animalslaughter'),
    path('animalslaughter1/',views.animalslaughter1,name='animalslaughter1'),
    path('animalslaughter2/',views.animalslaughter2,name='animalslaughter2'),
    path('animalslaughter3/',views.animalslaughter3,name='animalslaughter3'),
    path('animalslaughter4/',views.animalslaughter4,name='animalslaughter4'),
    path('animalslaughter5/',views.animalslaughter5,name='animalslaughter5'),
    path('animalslaughter6/',views.animalslaughter6,name='animalslaughter6'),
    path('animalslaughter7/',views.animalslaughter7,name='animalslaughter7'),
    path('animalslaughter8/',views.animalslaughter8,name='animalslaughter8'),
    path('poultry/',views.poultry,name='poultry'),
    path('poultry1/',views.poultry1,name='poultry1'),
    path('poultry2/',views.poultry2,name='poultry2'),
    path('poultry3/',views.poultry3,name='poultry3'),
    path('poultry4/',views.poultry4,name='poultry4'),
    path('poultry5/',views.poultry5,name='poultry5'),
   
   
    path('dashboard/',views.dashboard,name='dashboard'),
    path('doctors/',views.doctors,name='doctors'),
    path('analysis/',views.analysis,name='analysis'),
    path('dynamic/',views.dynamic,name='dynamic'),
    path('listofappointment/',views.listofappointment,name='listofappointment'),
    path('bookappointment/<int:doc_id>',views.bookappointment,name='bookappointment'),
    path('laws/',views.laws,name='laws'),
    path('lawsdetails/<int:law_id>',views.lawsdetails,name='lawsdetails'),
    path('Animal_Disease/',views.Animal_Disease,name='Animal_Disease'),
    path('Animal_category/',views.Animal_category,name='Animal_category'),
    path('symptoms/',views.symptoms,name='symptoms'),
    path('donate/',views.donate,name='donate'),
    path('creditcard/',views.creditcard,name='creditcard'),
    path('hospital/',views.hospital,name='hospital'),
    path('hospital/<int:id>',views.hospital,name='hospital_id'),
   
    path('ngos/',views.ngos,name='ngos'),
    path('ngos/<int:id>',views.ngos,name='ngos_id'),
    
    path('report/',views.report,name='report'),
    path('doctorprofile/<int:doc_id>',views.doctorprofile,name='doctorprofile'),
    path('lawsdetails/<int:law_id>',views.lawsdetails,name='lawsdetails'),
    path('test/', views.test, name='test'),
    path('news/', views.news, name='news'),
    path('news/<int:page_number>', views.news, name='news')     
         
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
