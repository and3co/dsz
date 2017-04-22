from django.db import models

# Create your models here.

class AreaDevice(models.Model):
    AREA_DEVICE = (
        ('A', 'Area'),
        ('D', 'Device'),
    )
    parent = models.ForeignKey('self', blank=True, null=True)
    a_d = models.CharField(max_length=1, choices=AREA_DEVICE)
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    description = models.CharField(max_length=250)
    manufacturer = models.CharField(max_length=60)
    dtype = models.CharField(max_length=60)
    prod_date = models.DateField(max_length=60)
    serial_number = models.CharField(max_length=50)
    tag_name = models.CharField(max_length=20) 
    def __str__(self):
        return self.name   

class Dev_attr(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=40)
    unit = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Dev_attr_float(models.Model):
    device = models.ForeignKey(AreaDevice)
    attr = models.ForeignKey(Dev_attr)
    value = models.FloatField()
    def __str__(self):
        return ", ".join([self.attr.name, self.value, self.attr.unit])

class Dev_attr_char(models.Model):
    device = models.ForeignKey(AreaDevice)
    attr = models.ForeignKey(Dev_attr)
    value = models.CharField(max_length=100)
    def __str__(self):
        return ", ".join([self.attr.name, self.value, self.attr.unit])

#TODO file csatolmánynak még kell