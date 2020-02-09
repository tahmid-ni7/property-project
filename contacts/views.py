from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check user if already made an inquiry
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already make an inquiry for this property.')
                return redirect('/listings/' + listing_id)

        contact = Contact(listing_id=listing_id, listing=listing, name=name, email=email,phone=phone,
                          message=message, user_id=user_id)
        contact.save()

        # SEND MAIL
        # send_mail(
        #     'Property: '+listing+' have an inquiry.',
        #     'An user send an inquiry about your property. Please send feedback to the user.',
        #     'tahmid.umn@gmail.com',
        #     [realtor_email],
        #     fail_silently=False,
        # )

        messages.success(request, 'Your message has been submitted successfully, a realtor will get back you soon.')
        return redirect('/listings/'+listing_id)
