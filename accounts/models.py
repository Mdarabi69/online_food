from django.db import models
from django.contrib.auth.models import  AbstractUser


class CustomUser(AbstractUser):
    CUSTOMER = 1
    RESTURANT = 2
    ROLE_CHOISE = (
        (CUSTOMER, 'Customer'),
        (RESTURANT, 'Resturant'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOISE, blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True, verbose_name='ایمیل')
    username = models.CharField(max_length=50, unique=True, verbose_name='نام کاربری')
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural='کاربران'


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='کاربر')
    profile_image = models.ImageField(upload_to='user/profile',verbose_name='عکس پروفایل')
    city = models.CharField(max_length=100,null=True, blank=True,verbose_name='شهر')
    addres = models.CharField(max_length=100, null=True, blank=True,verbose_name='آدرس')
    phone_number = models.CharField(max_length=12, null=True, blank=True,verbose_name='شماره موبایل')

    def __str__(self) -> str:
        return f'User Profile For - {self.user.email}'
    
    class Meta:
        verbose_name = 'اطلاهات کاربر'
        verbose_name_plural='اطلاعات کاربران'