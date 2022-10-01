from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, View
from main.forms import ContactForm
from scripts.get_doggo import GetDoggo
from .models import Email, Contact
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


class HomePageView(TemplateView):
    template_name = "home.html"

    ## would like to eventually have it so that it will put random doggo pic in the thank you page
    ## Need to figure out how to wrangle httpresponse for that.
    # dog_pic = GetDoggo.get_doggo("https://random.dog/woof")
    # print("here is the result", dog_pic)


class ThanksPageView(TemplateView):
    template_name = "thanks.html"


class DeviceWorkView(TemplateView):
    template_name = "tech-services/troubleshooting.html"


class AccountMgmtView(TemplateView):
    template_name = "tech-services/accounts-mgmt.html"


class TutoringView(TemplateView):
    template_name = "tech-services/tutoring.html"


class WebsiteWorkView(TemplateView):
    template_name = "tech-services/website-work.html"


class ContactView(View):
    template_name = "contact.html"

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "Website Inquiry"
                body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        form = ContactForm()
        return render(request, "thanks.html", {'form': form})
