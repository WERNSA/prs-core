from django.db import models
from users.models import Roles 
from django.utils import timezone
from django.contrib.auth.models import User
from catalogs.models import Routes, PokeTypes, States

# Create your models here.

class Gyms(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=150, null=False, blank=True, unique=True)
    address = models.EmailField(max_length=150, null=True, blank=True, unique=True)
    phone = models.PositiveIntegerField(verbose_name = 'Phone', unique=False, null=True, blank=True)
    # img = models.ImageField(upload_to ='uploads/')
    disabled = models.BooleanField(default=False, null=False, blank=False)
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date', null = True)
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)
    
    #ForeingnKeys
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)

    def __srt__(self):
        return self.name

class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=30, null=False)
    mail = models.EmailField(max_length=150, null=False, blank=True)
    phone = models.PositiveIntegerField(verbose_name = 'Phone', unique=True, null=False, blank=True)
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date')
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)
    
    #ForeingnKeys
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    gym = models.ForeignKey(Gyms, on_delete=models.CASCADE)
    
    def __srt__(self):
        return self.name

class Trainers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    trainerCode = models.CharField(max_length=30)
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date')
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)
    
    def __srt__(self):
        return self.user.name

class Pokemons(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    trainerCode= models.CharField(max_length=30)
    colour = models.CharField(max_length=30)
    pokedexNumber = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    experience = models.PositiveIntegerField(verbose_name = 'Experience', unique=False, null=True, blank=True)    
    age = models.DateField(null=False, editable=False)
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date')
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)


    #ForeingnKeys
    pokeType = models.ForeignKey(PokeTypes, on_delete=models.CASCADE)
    
    def __srt__(self):
        return self.name

class Observations(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)
    date = models.DateTimeField(verbose_name = 'Date', auto_now=True) 
    pokemon = models.PositiveIntegerField(unique=False, null=True, blank=True) #this var only use in future  
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date')
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)
    
    def __srt__(self):
        return self.description

class Reserves(models.Model):
    id = models.AutoField(primary_key=True)
    rentalDateTime = models.DateTimeField(verbose_name = 'Rental Date', auto_now=True) 
    returnDateTime = models.DateTimeField(verbose_name = 'Return Date', auto_now=True) 
    experienceInitial = models.PositiveIntegerField(verbose_name = 'Experience Initial', unique=False, null=True, blank=True)    
    experienceFinal = models.PositiveIntegerField(verbose_name = 'Experience Final', unique=False, null=True, blank=True)    
    insertAt = models.DateTimeField(default=timezone.now, verbose_name = 'Create Date', editable=False)
    updateAt = models.DateTimeField(verbose_name = 'Update Date')
    insertUs = models.CharField(verbose_name='User Create', max_length=50, null = True, blank = True)
    updateUs = models.CharField(verbose_name='User Update', max_length=50, null = True, blank = True)

    #ForeingnKeys
    route = models.ForeignKey(Routes, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemons, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    userCreate = models.ForeignKey(Users, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observations, on_delete=models.CASCADE)
    
    def __srt__(self):
        return self.rentalDateTime
