from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Usuario vacio, debe ingresar nombre de usuario")
        user=self.model(username=username)
        user.set_password(password)
        user.save(using=self._db) 
        return user
    
    def create_superuser(self, username, password):
        user=self.create_user(username=username, password=password)
        user.is_admin=True
        user.save(using=self._db)
        return user

class Empleados(PermissionsMixin,AbstractBaseUser):
  idEmpleados=models.AutoField(primary_key=True)
  NomEmpleado=models.CharField('nomEpleado',max_length=80,unique=True)
  CelEmpleado=models.IntegerField('celEmpleado',max_length=20)
  CCEmpleado=models.IntegerField('ccEmpleado',max_length=20)
  RolEmpleado=models.CharField('rolEmpleado',max_length=20)
  StatusEmpleado=models.CharField('statusEmpleado',max_length=20) 
  username=models.CharField('Username',max_length=100,unique=True)
  password=models.CharField('Password',max_length=100)

  def save(self,**kwargs):
    some_salt="asdasASDsadasd"
    self.password=make_password(self.password,some_salt)
    super().save(**kwargs)


  objects=UserManager()
  USERNAME_FIELD="username"
