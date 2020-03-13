from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
  if request.method == 'POST':
    company_id = request.POST['company_id']
    company = request.POST['company']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    header = request.POST['header']
    message = request.POST['message']
    user_id = request.POST['user_id']
    company_email = request.POST['company_email']

  if request.user.is_authenticated:
    user_id = request.user.id
    has_contacted = Contact.objects.all().filter(company_id=company_id, user_id=user_id)

    contact = Contact(company=company, company_id=company_id, name=name, email=email, phone=phone, header=header, message=message, user_id=user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property company Inquiry',
    #   'There has been an inquiry for ' + company + '. Sign into the admin panel for more info',
    #   'traversy.brad@gmail.com',
    #   [company_email, realtor_email, 'techguyinfo@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/catalog/company/'+company_id)