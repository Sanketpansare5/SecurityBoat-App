from django.contrib import admin
from .models import Bookings, Users
from email.message import EmailMessage
import smtplib

def send_mail(subject, body, to):
	msg= EmailMessage()
	msg.set_content(body)
	msg['subject'] = subject
	msg['to'] = to
	msg['from'] = 'mailtoinformupdates@gmail.com'

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.starttls()
	server.login('mailtoinformupdates@gmail.com','mlokxanziwciigyw')
	server.send_message(msg)
	server.quit()

class BookingsAdmin(admin.ModelAdmin):
    list_display=('booked_by','department','event_name','event_type','event_date','event_slot','status')
    list_editable=('status',)

    def save_model(self, request, obj, form, change):
        if change and obj.status:
            event_name=obj.event_name
            event_date=obj.event_date
            event_time=obj.event_slot
            to=obj.email
            booked_by=obj.booked_by
            body=f"""Dear {booked_by},

We are pleased to inform you that your request to book the auditorium for the {event_name} on {event_date} during the {event_time} has been approved by the administration. We appreciate your patience throughout the approval process.

Please find below the confirmation details for your booking:

Event Name: {event_name}
Event Date: {event_date}
Event Time: {event_time}

We hope your event is a success, and we are confident that the auditorium will provide a suitable and comfortable venue for your needs. If you have any further questions or require additional assistance, please feel free to contact us.

Thank you for choosing our auditorium, and we look forward to hosting your event.

Best regards,
Admin"""
            subject="Auditorium Booking Request Approved"
            
            send_mail(subject, body, to)

        super().save_model(request, obj, form, change)

# Register your models here.

admin.site.register(Bookings,BookingsAdmin)
admin.site.register(Users)
