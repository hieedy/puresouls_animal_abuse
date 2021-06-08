from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    def __str__(self):
        return self.first_name

class myreview(models.Model):
    user_email=models.EmailField()
    subject=models.CharField(max_length=30)
    review=models.TextField()
    def __str__(self):
        return self.subject

class myhelp(models.Model):
    user_email=models.EmailField()
    problem=models.CharField(max_length=30)
    details=models.TextField()
    def __str__(self):
        return self.problem

class myregister(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=30)
    confirm_password=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class mycontactus(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=30)
    suggestion=models.TextField()
    def __str__(self):
        return self.name

class mydoctors(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=10)
    specialition=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    profile_image=models.ImageField( null=True)
   
   
    def __str__(self):
        return self.name

class mycreditcard(models.Model):
    card_owner=models.CharField(max_length=30)
    card_number=models.IntegerField()
    expiration_date=models.DateField(max_length=10)
    cvv_code=models.IntegerField()
    
    def __str__(self):
        return self.card_owner    

class myuser(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=10)
    dob = models.DateField(null =True , blank = True)
    state=models.CharField(max_length=10)
    password = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 6)
    profile_image=models.ImageField( null=True)
   
   
    def __str__(self):
        return self.name        

class myhospital(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    address=models.TextField()
    city=models.CharField(max_length=10)
    specialization=models.CharField(max_length=10)
    opening_hours=models.CharField(max_length=10)
    profile_image=models.ImageField( null=True)
    
   
    def __str__(self):
        return self.name

class mylaws(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
          
    url=models.URLField()          
    def __str__(self):
        return self.title

class myvaccination(models.Model):
    name=models.CharField(max_length=30)
    approx_price=models.IntegerField()
   
    def __str__(self):
        return self.name


class myexpertise(models.Model):
    expert_In=models.CharField(max_length=20)
    doc_id = models.ForeignKey(mydoctors, on_delete=models.CASCADE)

    def __str__(self):
        return self.expert_In

class mybookappointment(models.Model):
    doc_id = models.ForeignKey(mydoctors, on_delete=models.CASCADE)
    user_id = models.ForeignKey(myuser, on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    message = models.TextField(blank =True, null=True)

    status_choices = { ('A', 'Approved'), ('NA', 'Not Approved'), ('P', 'Pending')}
    app_status = models.CharField(max_length =2 , choices=status_choices, default='P' )

    def __str__(self):
        return self.user_id.email

class myreport(models.Model):
   
    subject=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    user_id = models.ForeignKey(myuser, on_delete=models.CASCADE)


    def __str__(self):
        return self.subject

class myngos(models.Model): 
   
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    description=models.TextField()
    website=models.URLField()
    opening_hours=models.CharField(max_length=10)
    profile_image=models.ImageField( null=True)
    

    def __str__(self):
        return self.name



  



class myAnimal_category(models.Model):
    name=models.CharField(max_length=30)

     
    def __str__(self):
        return self.name

class myAnimal_Disease(models.Model):
    Disease_name=models.CharField(max_length=30)
    category_id=models.ForeignKey(myAnimal_category, on_delete=models.CASCADE)
   

     
    def __str__(self):
        return self.Disease_name        

class mysymptoms(models.Model):
    
    disease_id = models.ForeignKey(myAnimal_Disease, on_delete=models.CASCADE)
    symptom_detail=models.TextField()


     
    def __str__(self):
        return self.disease_id.Disease_name 




        











