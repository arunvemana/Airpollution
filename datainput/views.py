from django.shortcuts import render
from django.views.generic import TemplateView
from datainput.forms import UserInputData
import csv
# Create your views here.


class HomeView(TemplateView):
    template_name = 'datainput/forminput.html'

    def get(self, request):
        form = UserInputData()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = UserInputData(request.POST)
        if form.is_valid():
            firstPara = form.cleaned_data['no2']
            secondPara = form.cleaned_data['co2']
            thridPara = form.cleaned_data['zn']
            fourthPara = form.cleaned_data['h']
            text = str(firstPara) + ' ' + str(secondPara) +' ' +str(thridPara) + ' ' + str(fourthPara)
            with open('datainput/DataInput.csv', "a") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=form.cleaned_data.keys())
                writer.writerow(form.cleaned_data)
            form = UserInputData()

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)

