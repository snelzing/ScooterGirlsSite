from django.shortcuts import render, redirect,reverse
from django.views.generic import TemplateView, View
from main.forms import InputForm
from scripts.get_doggo import GetDoggo
from .models import Email, Contact


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

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        form = InputForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = InputForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})
        name = form.cleaned_data['name']
        email_str = form.cleaned_data['email']
        print(name, email_str)
        email, created = Email.objects.get_or_create(email__iexact=email_str, defaults={'email': email_str})
        print(email)
        Contact.objects.create(email=email, name=name)
        return redirect('thanks')
