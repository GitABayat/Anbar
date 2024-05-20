from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):    
    Name = models.CharField(max_length=120, default='***', blank=False, null=False, verbose_name=_('نام انبار'))
    Status = models.BooleanField(default=True, verbose_name=_('وضعیت'))
    Desc = models.CharField(max_length=500, default='***', blank=True, null=True, verbose_name=_('توضیحات'))
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ایجاد کننده'), null=True, blank=True)
    Create_UName  = models.CharField(max_length=120, default='--', verbose_name=_('نام کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'Store'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
        )

    def __str__(self):
        return str(self.Name)  


class GoodsAndServices(models.Model):    
    Name = models.CharField(max_length=120, default='***', blank=False, null=False, verbose_name=_('نام کروه/کالا'))
    Status = models.BooleanField(default=True, verbose_name=_('وضعیت'))
    Desc = models.CharField(max_length=500, default='***', blank=True, null=True, verbose_name=_('توضیحات'))
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ایجاد کننده'), null=True, blank=True)
    Create_UName  = models.CharField(max_length=120, default='--', verbose_name=_('نام کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'GoodsAndServices'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
        )

    def __str__(self):
        return str(self.Name)  


class CustomersGroup(models.Model):    
    Name = models.CharField(max_length=120, default='***', blank=False, null=False, verbose_name=_('نام کروه'))
    Status = models.BooleanField(default=True, verbose_name=_('وضعیت'))
    Desc = models.CharField(max_length=500, default='***', blank=True, null=True, verbose_name=_('توضیحات'))
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ایجاد کننده'), null=True, blank=True)
    Create_UName  = models.CharField(max_length=120, default='--', verbose_name=_('نام کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'CustomersGroup'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
        )

    def __str__(self):
        return str(self.Name)  


class Customers(models.Model):    
    Group = models.ForeignKey(CustomersGroup, on_delete=models.PROTECT, related_name='CGroup', null=False, blank=False)
    Name = models.CharField(max_length=120, default='***', blank=False, null=False, verbose_name=_('نام کروه'))
    Family = models.CharField(max_length=120, default='***', blank=False, null=False, verbose_name=_('نام کروه'))
    Status = models.BooleanField(default=True, verbose_name=_('وضعیت'))
    Desc = models.CharField(max_length=500, default='***', blank=True, null=True, verbose_name=_('توضیحات'))
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ایجاد کننده'), null=True, blank=True)
    Create_UName  = models.CharField(max_length=120, default='--', verbose_name=_('نام کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'Customers'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
        )

    def __str__(self):
        return str(self.Name)  


class Recept(models.Model):  
    Rec_Type = [
        (0, 'رسید'),
        (1, 'حواله'),
    ]
    Sto = models.ForeignKey(Store, on_delete=models.PROTECT, related_name='Store', null=False, blank=False)
    GoAndSer = models.ForeignKey(GoodsAndServices, on_delete=models.PROTECT, related_name='GoASe', null=False, blank=False)
    Custom = models.ForeignKey(Customers, on_delete=models.PROTECT, related_name='Customer', null=False, blank=False)
    Count = models.IntegerField(default=0, blank=False, null=False, verbose_name=_('مبلغ'))
    Type = models.IntegerField(default=0, choices=Rec_Type, blank=True, null=True, verbose_name=_('نوع فرم'))
    Desc = models.CharField(max_length=500, default='***', blank=True, null=True, verbose_name=_('توضیحات'))
    Create_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Update_Date = models.DateTimeField(auto_now=True, null=True, blank=True)
    Create_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ایجاد کننده'), null=True, blank=True)
    Create_UName  = models.CharField(max_length=120, default='--', verbose_name=_('نام کاربر ایجاد کننده'), null=True, blank=True)
    Update_Uid = models.IntegerField(default=0, verbose_name=_('کاربر ویرایش کننده'), null=True, blank=True)

    class Meta:
        ordering = ['id']
        db_table = 'Recept'
        permissions = (
            ('can_read_private_section', 'administrator'),
            ('SubAdmin', 'SubAdmin'),
        )

    def __str__(self):
        return str(self.Custom)  

