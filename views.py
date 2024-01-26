from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        unmessage = request.POST['unmessage']

        send_mail(
            message_name, #user name
            message_email, # message subject
            unmessage, # messages
            message_email, # from email
            ['chikkiammu941@gmail.com'], # To email

        )

        return render(request,'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html' ,{})

