from django.contrib import admin
from tickets.models import Ticket
from tickets.models import Contact
from tickets.models import Business

admin.site.register(Ticket)
admin.site.register(Contact)
admin.site.register(Business)
