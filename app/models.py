from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=500,verbose_name="Name")
    age = models.CharField(max_length=600,verbose_name="Age")
    phone = models.CharField(max_length=600,verbose_name="Phone")
    job = models.CharField(max_length=600,verbose_name="Job")
    salary = models.CharField(max_length=500,verbose_name="Salary")
    address = models.CharField(max_length=600,verbose_name="Address")
    about = models.CharField(max_length=600,verbose_name="About")
    contact_time = models.CharField(max_length=600,verbose_name="Contact Time")
    aim = models.CharField(max_length=600,verbose_name="Aim")
    def __str__(self):
        return self.name
    class Meta:
        db_table = "Ishchilar"
        verbose_name = "Ishchi "
        verbose_name_plural = "Ishchilar "
class Work(models.Model):
    company = models.CharField(max_length=600,verbose_name="Company name")
    job = models.CharField(max_length=600,verbose_name="Job")
    phone = models.CharField(max_length=600,verbose_name="Phone")
    salary = models.CharField(max_length=600,verbose_name="Salary")
    address = models.CharField(max_length=600,verbose_name="Address")
    contact_time = models.CharField(max_length=600,verbose_name='Contact Time')
    work_time = models.CharField(max_length=600,verbose_name="Work time")
    requirements = models.CharField(max_length=600,verbose_name="Requirements")
    def __str__(self):
        return self.company
    class Meta:
        db_table = "Ish beruvchilar "
        verbose_name = 'Ish beruvchi '
        verbose_name_plural = "Ish beruvchilar "

class TelegramBotUser(models.Model):
    telegram_id = models.CharField(max_length=500,verbose_name="Telegram ID")
    language = models.CharField(max_length=10,default='uz',verbose_name='System Language')

