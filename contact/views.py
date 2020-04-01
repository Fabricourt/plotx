from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact, Contactk, Contactchurch
from .forms import ContactkForm, ContactForm
from django.contrib.auth.decorators import login_required
from towns.models import Town
from . import models


def contactk(request):
    towns = Town.objects.order_by('name').filter(is_published=True)
    template = "contact/contactk.html"
    if request.method == "POST":
        form =ContactkForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent')
            return redirect('contactk')
      
    else:
        form = ContactkForm()
    
    context ={
        'form': form,
        'towns':towns
    }
    return render(request, template, context)
   


def contact(request):
  if request.method == 'POST':
    business_id = request.POST['business_id']
    business = request.POST['business']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    header = request.POST['header']
    message = request.POST['message']
    user_id = request.POST['user_id']
    business_email = request.POST['business_email']

  if request.user.is_authenticated:
    user_id = request.user.id
    has_contacted = Contact.objects.all().filter(business_id=business_id, user_id=user_id)

    contact = Contact(business=business, business_id=business_id, name=name, email=email, phone=phone, header=header, message=message, user_id=user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property business Inquiry',
    #   'There has been an inquiry for ' + business + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [business_email, realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/companys/business/'+business_id)

  
def Churchcontact(request):
  if request.method == 'POST':
    church_id = request.POST['church_id']
    church = request.POST['church']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    header = request.POST['header']
    message = request.POST['message']
    user_id = request.POST['user_id']
    church_email = request.POST['church_email']

  if request.user.is_authenticated:
    user_id = request.user.id
    has_contacted = Contactchurch.objects.all().filter(church_id=church_id, user_id=user_id)

    contactchurch = Contactchurch(church=church, church_id=church_id, name=name, email=email, phone=phone, header=header, message=message, user_id=user_id )

    contactchurch.save()

    # Send email
    # send_mail(
    #   'Property business Inquiry',
    #   'There has been an inquiry for ' + business + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [business_email, realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your message has been recieved')
    return redirect('/churches/church/'+church_id)

  