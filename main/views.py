from django.contrib.sites import requests
from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, View
from main.forms import ContactForm
from scripts.get_doggo import GetDoggo
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings
from main.models import Contact
from requests import post
from django.core.exceptions import PermissionDenied


class HomePageView(TemplateView):
    template_name = "home.html"


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
        form = ContactForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        subject = "Website Inquiry"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())

        sitekey = '581108a4-3780-41c2-85dd-1d81a197cf6b'
        token = request.POST.get('h-captcha-response')
        response = post("https://hcaptcha.com/siteverify", {'secret': settings.HCAPTCHA_SECRET_KEY, 'response': token,
                                                            'sitekey': sitekey},
                        timeout=10)

        contact = Contact(name=form.cleaned_data['name'],
                          email=form.cleaned_data['email'],
                          message=form.cleaned_data['message'])
        print(response.status_code)
        response_json = response.json()
        print("here is the response json", response_json)

        if response_json['success']:
            contact.save()
        else:
            nope = "<div> Nope </div>"
            return render(request, 'nope.html', {'nope': nope})

        doggo = GetDoggo.get_doggo("https://random.dog/woof?filter=mp4,webm")
        return render(request, "thanks.html", {'doggo': doggo})


class NopePageView(TemplateView):
    template_name = "nope.html"
