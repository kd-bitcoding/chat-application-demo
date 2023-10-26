# importing models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email, *args, **kwargs):
        """
        Creates and saves a User with the given email and other info.
        """

        # Value Validation
        if not email:
            raise ValueError("User must have an email..!")
        if not kwargs.get('password'):
            raise ValueError("User must have a password..!")
        
        # Getting Values
        password = kwargs.get('password')
        isActive = kwargs.get('active', True) if kwargs.get('active', True) not in ['', None] else True
        isStaff = kwargs.get('staff', False) if kwargs.get('staff', False) not in ['', None] else False
        isAdmin = kwargs.get('admin', False) if kwargs.get('admin', False) not in ['', None] else False

        # Creating User
        userObj = self.model(
            email = self.normalize_email(email)
        )
        userObj.set_password(password) # Change Password
        userObj.active = isActive
        userObj.staff = isStaff
        userObj.admin = isAdmin
        userObj.save(using=self._db)
        return userObj
    
    def create_staffuser(self, email, password=None):
        """
        Creates and saves a staff user with the given email and password.
        """
        userObj = self.create_user(email, password=password, staff=True)
        return userObj
    
    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        userObj = self.create_user(email=email, password=password, staff=True, admin=True)
        return userObj


# Custom User Model
class User(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique=True) # Will be used in place of username
    active = models.BooleanField(default=True) # can login to system
    staff = models.BooleanField(default=False) # staff user
    admin = models.BooleanField(default=False) # super user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_email(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin