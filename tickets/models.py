from django.db import models
from django.forms import ModelForm
from django.forms.widgets import HiddenInput

class Business(models.Model):
    website = models.CharField(max_length=500,null=True,blank=True)
    name = models.CharField(max_length=250,unique=True)
    category = models.CharField(max_length=250)
    tel = models.CharField(max_length=250,null=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True,null=True)
    class Meta:
        ordering = ['-last_modified']        
    def __unicode__(self):
        return "%s, %s" % (self.name, self.category)

class Ticket(models.Model):
    business = models.ForeignKey(Business)
    what = models.TextField(max_length=500)
    date = models.DateTimeField('when',auto_now_add=True)
    cost = models.CharField(max_length=7,blank=True,default='0')
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return "%s: %s" % (self.business.name , self.date.strftime("%b %d, %I:%M %p"))
    def save(self , *args, **kwargs):
        super(Ticket, self).save(*args, **kwargs)
        self.business.save() # update the last_modified field

class Contact(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,null=True,blank=True)
    tel = models.CharField(max_length=250,null=True,blank=True)
    last_modified = models.DateTimeField(auto_now=True,blank=True,null=True)
    class Meta:
        ordering = ['-last_modified']
    def __unicode__(self):
        if self.email:
            return "%s: %s<%s>" % (self.business.name , self.name , self.email)
        else:
            return "%s: %s" % (self.business.name , self.name)
    def save(self , *args, **kwargs):
        super(Contact, self).save(*args, **kwargs)
        self.business.save() # update the last_modified field

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        
class TicketForm(ModelForm):
    class Meta:
        model = Ticket
    def __init__(self, *args, **kwargs):
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['business'].widget = HiddenInput()
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['business'].widget = HiddenInput()
