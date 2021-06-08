from django.shortcuts import redirect
from django.shortcuts import render
from myapp.models import myreview
from myapp.models import myhelp
from myapp.models import myregister
from myapp.models import mycontactus
from myapp.models import myuser
from myapp.models import mydoctors
from myapp.models import myhospital
from myapp.models import myngos
from myapp.models import myreport
from myapp.models import mylaws
from myapp.models import myAnimal_category
from myapp.models import myAnimal_Disease
from myapp.models import mysymptoms
from myapp.models import mybookappointment
from puresouls import settings
from django.core.mail import send_mail
from newsapi import NewsApiClient
from django.core.paginator import Paginator



# Create your views here.
def home(request):
    return render(request,'form.html',{})
def aboutus(request):
    return render(request,'aboutus.html',{})
def contactus(request):
    if request.method=='POST':
        post=mycontactus()
        post.name= request.POST.get('name')
        post.email= request.POST.get('mail')
        post.subject= request.POST.get('sub')
        post.suggestion= request.POST.get('sug')
        post.save()
        return render(request,'contactus.html',{})
    else:
        return render(request,'contactus.html',{})

        
       
        
             
def footer(request):
    return render(request,'footer.html',{})
def forgotpassword(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        if myuser.objects.filter(email = em).exists():
            usr = myuser.objects.get(email = em)

            subject = 'Password'
            message  = 'Hello Password is '+usr.password
            
            email_from = settings.EMAIL_HOST_USER
            recepient_list = [usr.email, ]
            try: 
                send_mail(subject,message , email_from , recepient_list)
                res = "Your Password is sent successfully to your mail"
            except Exception as E:
                print(E)  
                res="There is some technical error"  
            
            return render(request, 'forgotpassword.html', {'res':res})
      

        else:
            res = 'This email does not exist'
            
            return render(request, 'forgotpassword.html', {'res':res})
    
   
    return render(request,'forgotpassword.html',{}) 
def index1(request):
    return render(request,'index1.html',{})
def login(request):
    if request.method=='POST':
        formpost=True

        email=request.POST.get('mail')   
        password=request.POST.get('npwd')  
        errormessage=""
        expert = myuser.objects.filter(email=email , password=password)
        k=len(expert)
        if k>0:
            print("valid credentials ")
            request.session['email']=email
            
            return redirect('/profile')
           
        
        else:
            print("invalid credentials")
            errormessage="invalid credentials"
            return render(request,'login.html',{'formpost':formpost})
    else:
        formpost=False
        return render(request,'login.html',{'formpost':formpost})      


def FAQ(request):
    return render(request,'FAQ.html',{})
def recoverpassword(request):
    return render(request,'recoverpassword.html',{})

def test(request):
    user = User.objects.filter()

    user[0].set_password('puresouls')
    user[0].save()


    return 

    
def register(request):
    if request.method=='POST':
    
        name= request.POST.get('nme')
        email= request.POST.get('mail')
        password= request.POST.get('npwd')
        confirm_password= request.POST.get('cpwd')

        if myuser.objects.filter(email = email, password = password).exists():
            return render(request,'register.html',{'result': False})

        else:
            if password != confirm_password:
                 return render(request,'register.html',{'result': False})
            else:
                
                #create object
                user = myuser()
                user.name= name
                user.email = email
                user.password = password
                user.save()
                return render(request, 'register.html', {'result':True})
    
        return render(request,'register.html',{})
    else:
       return render(request,'register.html',{})
        
def review(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    if request.method=='POST':
        post=myreview()
        post.user_email=request.session['email']
        post.subject= request.POST.get('subject')
        post.review= request.POST.get('message')
        post.save()
        return render(request,'review.html',{})
    else:
        return render(request,'review.html',{})

def profile(request):
    if not request.session.has_key('email'):
        return redirect('/login')


    userdetail = myuser.objects.get(email = request.session['email'])
    
    return render(request,'profile.html',{'user':userdetail})

def help(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    if request.method=='POST':
        post=myhelp()
        post.user_email=request.session['email']
        post.problem= request.POST.get('subject')
        post.details= request.POST.get('message')
        post.save()
        return render(request,'help.html',{})
    else:
        return render(request,'help.html',{})
   
def header(request):
    return render(request,'header.html',{})
def blog(request):
    return render(request,'blog.html',{})
def changepassword(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    if request.method=='POST':
        reg=myuser.objects.get(email=request.session['email'])
        password=request.POST.get('old')
        newpwd=request.POST.get('npwd')
        confirmpwd=request.POST.get('cpwd')
        if(newpwd==confirmpwd):
            p=reg.password
            if(password==p):
                reg.password=newpwd
                reg.save()
                rest="password changed"
                print("password updated")
                return render(request,'changepassword.html',{'rest':rest})
            else:
                print("password not updated")
                res="invalid current password"    
                return render(request,'changepassword.html',{'rest':res})
        else:
            res="confirm password and new password dont match"
            return render(request,'changepassword.html',{'rest':res})

    return render(request,'changepassword.html',{})

def editprofile(request):
    if not request.session.has_key('email'):
        return redirect('/login')

    if request.method == 'POST':
        type_form = request.POST.get('type')
        if type_form == '1':
            image = request.FILES.get('image')
            email = request.session.get('email')

            us = myuser.objects.get(email = email)
            us.profile_image = image
            us.save()
        elif type_form == '2':

            name=request.POST.get('fn')       
            email=request.POST.get('email')
            mobile=request.POST.get('phn')
            city=request.POST.get('city')
            state=request.POST.get('state')
            gender=request.POST.get('gen')
            dob=request.POST.get('dob')        
            address=request.POST.get('address')
            
            email=request.session.get("email")
            us=myuser.objects.get(email=email)

            us.Name = name
            us.mobile=mobile 
            us.city=city
            us.state=state
            us.gender=gender
            us.dob=dob
            us.address=address

            us.save()

       

    email_id = request.session.get('email')
    us = myuser.objects.get(email = email_id )

    if us.dob:
        date_string = us.dob.strftime("%Y-%m-%d")
        return render(request,'editprofile.html',{'user_data': us, 'dob':date_string})
        

    return render(request,'editprofile.html',{'user_data': us})


   
def base(request):
    return render(request,'base.html',{})

def doctors(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    cur_user = myuser.objects.get(email = request.session.get('email'))

    doctors = mydoctors.objects.filter(city__iexact = cur_user.city)

    all_doctors_city = mydoctors.objects.all().values('city').distinct()

    selected_city = cur_user.city

    if request.method == 'POST':
        city = request.POST.get('filter_city')

        doctors = mydoctors.objects.filter(city__iexact = city)
        selected_city = city




    return render(request,'doctors.html',{'doctors': doctors, 'doctors_cities': all_doctors_city, 'selected_city':selected_city })   






def creditcard(request):
    return render(request,'creditcard.html',{})

def doctorprofile(request ,doc_id):

    if not request.session.has_key('email'):
        return redirect('/login')
    
    doctorprofile=mydoctors.objects.get(id = doc_id)

    return render(request,'doctorprofile.html',{'doctor':doctorprofile})    


def logout(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    del request.session['email']
    return redirect('/login')    

def dashboard(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    return render(request,'dashboard.html',{})

def get_data_from_api(page_number):
    # Init
    newsapi = NewsApiClient(api_key='a58528989d6b478b976921ae936d55ae')  

    all_articles = newsapi.get_everything(q="Animals",
                                        page = page_number,
                                      language='en',
                                      sort_by='relevancy'
                                      )


    articles = all_articles['articles']
    return articles

def news(request, page_number = 1):
    if not request.session.has_key('email'):
        return redirect('/login')

    articles =  get_data_from_api(page_number)
    
    return render(request,'news.html',{'articles': articles, 'page_number': page_number})    

def hospital(request, id=None):
    if not request.session.has_key('email'):
        return redirect('/login')

    if id == None:
        hospitals = myhospital.objects.all() 
        return render(request,'hospital.html',{'hospitals':hospitals})    
    else:
        h = myhospital.objects.get(id = id)
        hospitals = myhospital.objects.all() 
        return render(request,'hospital.html',{'hospitals':hospitals, 'hos': h})    
    
    
    cur_user = myuser.objects.get(email = request.session.get('email'))

    hospital = myhospital.objects.filter(city__iexact = cur_user.city)

    all_hospital_city = myhospital.objects.all().values('city').distinct()

    selected_city = cur_user.city

    if request.method == 'POST':
        city = request.POST.get('filter_city')

        doctors = mydoctors.objects.filter(city__iexact = city)
        selected_city = city




    return render(request,'hospital.html',{'hospital': hospital, 'hospital_cities': all_hospital_city, 'selected_city':selected_city })   

def ngos(request , id=None):
    if not request.session.has_key('email'):
        return redirect('/login')

    if id == None:
        ngo = myngos.objects.all() 
        return render(request,'ngos.html',{'ngos':ngo})    
    else:
        n = myngos.objects.get(id = id)
        ngos = myngos.objects.all() 
        return render(request,'ngos.html',{'ngos':ngos, 'ngo': n})   
    
def bookappointment(request, doc_id):
    if not request.session.has_key('email'):
        return redirect('/login')


    result = None
    if request.method == 'POST':
        date_of_appointment = request.POST.get('date_of_appointment')
        time_of_appointment  = request.POST.get('time')

        book_appointment  = mybookappointment()
        book_appointment.date =  date_of_appointment
        book_appointment.time =  time_of_appointment
        book_appointment.doc_id = mydoctors.objects.get(id = doc_id)
        book_appointment.user_id = myuser.objects.get(email = request.session.get('email'))
        book_appointment.is_approved = False
        book_appointment.save()
        result = True

        print(date_of_appointment, time_of_appointment, doc_id)



    us = myuser.objects.get(email = request.session.get('email'))
    
    return render(request,'bookappointment.html',{'user':us, 'result':result}) 

def laws(request):
    
    if not request.session.has_key('email'):
        return redirect('/login')
    
    laws = mylaws.objects.all()
    return render(request,'laws.html',{'laws':laws}) 
  
def donate(request):
    return render(request,'donate.html',{})    

def report(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    if request.method=='POST':
        post=myreport()
        post.user_email=request.session['email']
        post.subject= request.POST.get('subject')
        post.description= request.POST.get('message')
        post.date= request.POST.get('dob')
        post.time= request.POST.get('time')
        post.user_id=myuser.objects.get(email = request.session.get('email'))

        post.save()
        return render(request,'report.html',{})
    else:
        return render(request,'report.html',{})

def listofappointment(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    

    current_user = myuser.objects.get(email = request.session.get('email'))
    list_of_appointments = mybookappointment.objects.filter(user_id = current_user )


    return render(request,'listofappointment.html',{'appointments': list_of_appointments})  
def get_symptoms(category_id):
    categ = myAnimal_category.objects.get(id = int(category_id))
    diseases = myAnimal_Disease.objects.filter(category_id = categ)

    symptom_names = []

    for d in diseases:
        sym = mysymptoms.objects.filter(disease_id = d)
        for s in sym:
            if s.symptom_detail.strip() not in symptom_names:
                symptom_names.append(s.symptom_detail.strip())

    return symptom_names

def Animal_category(request):
    if not request.session.has_key('email'):
        return redirect('/login')
    
    animals = myAnimal_category.objects.all()

    if request.method =='POST':
        form_type = request.POST.get('type')

        if(form_type == "1"):
            category_id = request.POST.get('category')
            symptom_names =  get_symptoms(category_id)   
            category_name = myAnimal_category.objects.get(id = category_id).name
            print(category_name)
            return render(request,'Animal_category.html',{'animals':animals, 'symptoms':symptom_names, 'categ_id':category_id, 'selected_category' : category_name })


        elif form_type == "2":
            category_id = request.POST.get('category')
            symptoms = request.POST.getlist('symptoms')
            category_name = myAnimal_category.objects.get(id = category_id).name
            diseases = []

            for s in symptoms:
                dis = mysymptoms.objects.filter(symptom_detail = s)
                for d  in dis:
                    if d.disease_id not in diseases and d.disease_id.category_id == myAnimal_category.objects.get(id = int(category_id)):
                        diseases.append(d.disease_id)
            

           
            symptom_names =  get_symptoms(category_id)
            return render(request,'Animal_category.html',{'animals':animals, 'symptoms':symptom_names, 'diseases':diseases,'categ_id':category_id,'selected_category' : category_name })
          
    
       
    return render(request,'Animal_category.html',{'animals':animals })    

def lawsdetails(request ,law_id):

    if not request.session.has_key('email'):
        return redirect('/login')
    
    lawsdetails=mylaws.objects.get(id = law_id)

    return render(request,'lawsdetails.html',{'law':lawsdetails})    

def Animal_Disease(request):
    return render(request,'Animal_Disease.html',{})    

def symptoms(request):
    return render(request,'symptoms.html',{})    
 
def analysis(request):
    return render(request,'analysis.html',{})   

def dynamic(request):
    return render(request,'dynamic.html',{})    

def poultry(request):
    return render(request,'poultry.html',{})  

def poultry1(request):
    return render(request,'poultry1.html',{})    
def poultry2(request):
    return render(request,'poultry2.html',{})    
def poultry3(request):
    return render(request,'poultry3.html',{})    
def poultry4(request):
    return render(request,'poultry4.html',{})    
def poultry5(request):
    return render(request,'poultry5.html',{})    


def animalslaughter(request):
    return render(request,'animalslaughter.html',{})
def animalslaughter1(request):
    return render(request,'animalslaughter1.html',{})    
def animalslaughter2(request):
    return render(request,'animalslaughter2.html',{})    
def animalslaughter3(request):
    return render(request,'animalslaughter3.html',{})    
def animalslaughter4(request):
    return render(request,'animalslaughter4.html',{})    
def animalslaughter5(request):
    return render(request,'animalslaughter5.html',{})    
def animalslaughter6(request):
    return render(request,'animalslaughter6.html',{})    
def animalslaughter7(request):
    return render(request,'animalslaughter7.html',{})    
def animalslaughter8(request):
    return render(request,'animalslaughter8.html',{})    
    
def seafoodproduction(request):
    return render(request,'seafoodproduction.html',{})
def seafoodproduction1(request):
    return render(request,'seafoodproduction1.html',{})    
def seafoodproduction2(request):
    return render(request,'seafoodproduction2.html',{})    
def seafoodproduction3(request):
    return render(request,'seafoodproduction3.html',{})    
def seafoodproduction4(request):
    return render(request,'seafoodproduction4.html',{})    
def seafoodproduction5(request):
    return render(request,'seafoodproduction5.html',{})    
def seafoodproduction6(request):
    return render(request,'seafoodproduction6.html',{})    
def seafoodproduction7(request):
    return render(request,'seafoodproduction7.html',{})    
def seafoodproduction8(request):
    return render(request,'seafoodproduction8.html',{})    
                            
def animaltesting(request):
    return render(request,'animaltesting.html',{})    
def animaltesting1(request):
    return render(request,'animaltesting1.html',{})                                
def animaltesting2(request):
    return render(request,'animaltesting2.html',{})        
def animaltesting3(request):
    return render(request,'animaltesting3.html',{})        
def animaltesting4(request):
    return render(request,'animaltesting4.html',{})     
def animaltesting5(request):
    return render(request,'animaltesting5.html',{})           
        








