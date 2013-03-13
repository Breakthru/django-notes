# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import *
from django.shortcuts import redirect

@login_required
def home(request, id):
    if id:
        business = get_object_or_404(Business, pk=id)
        tickets_list =  Ticket.objects.filter(business=business)
        contacts_list = Contact.objects.filter(business=business)    
        ticket_form = TicketForm(initial={'business' : business.pk})
        contact_form = ContactForm(initial={'business' : business.pk})
        context = RequestContext(request, {'business' : business , 'tickets_list' : tickets_list, 'contacts_list' : contacts_list, 'ticket_form' : ticket_form, 'contact_form' : contact_form})
        return render_to_response('index.html', context)
    else:
        business_list = Business.objects.all()
        business_form = BusinessForm()
        context = RequestContext(request, {'business_list' : business_list , 'business_form' : business_form})
        return render_to_response('index.html', context)    

@login_required
def add_item(request,item):
    items = {'ticket':Ticket, 'business':Business, 'contact':Contact}
    items_form = {'ticket':TicketForm, 'business':BusinessForm, 'contact':ContactForm}
    if not items.has_key(item):
        return redirect('/')
    if request.method == 'POST':
        form = items_form[item](request.POST)
        if form.is_valid():
            instance,created = items[item].objects.get_or_create(**form.cleaned_data)
            if created:
                print "successfully created "+item
            else:
                print "instance already exist"
        else:
            print "form not valid"
            return redirect('/')        
        if item=="business":
            return redirect('/')
        else:
            return redirect('/'+str(instance.business.id))
    # this view should not be accessed with method GET
    return redirect('/')

@login_required
def edit_item(request,item,id):
    items = {'ticket':Ticket, 'business':Business, 'contact':Contact}
    items_form = {'ticket':TicketForm, 'business':BusinessForm, 'contact':ContactForm}
    if items.has_key(item):
        instance = get_object_or_404(items[item], pk=id)
    else:
        return redirect('/')
    form = items_form[item](request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        if item=='business':
            return redirect('/')
        else:
            return redirect('/'+str(instance.business.id))
    context = RequestContext(request, { 'f' : form, 'id' : id , 'item' : item[0].upper()+item[1:]})
    return render_to_response('edit_item.html', context)

@login_required
def delete_item(request,item,id):
    items = {'ticket':Ticket, 'business':Business, 'contact':Contact}
    if items.has_key(item):
        instance = get_object_or_404(items[item], pk=id)
    else:
        return redirect('/')
    if request.method == "GET":
        item=item[0].upper()+item[1:] # capitalise first letter
        context = RequestContext(request, {'item' : item, 'item_desc' : instance, 'id' : instance.id})
        return render_to_response('delete_item.html', context)
    elif request.method == "POST":
        instance.delete()
        if item=="business":
            return redirect('/')
        else:
            return redirect('/'+str(instance.business.id))

    
