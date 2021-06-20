from django.core.exceptions import ValidationError
from django.forms import ModelForm
from datetime import date
from .models import Brick, Manual, Set


class BrickModelForm(ModelForm):
    class Meta:
        model = Brick

        fields = ['id', 'name', 'color', 'type', 'image', 'sets']

    def clean_color(self):
        data = self.cleaned_data['color']
        if data[0] != '#' or len(data) > 7 or len(data) <= 0:
            raise ValidationError('Neplatný formát barvy, platný formát: #123456')
        return data


class ManualModelForm(ModelForm):
    class Meta:
        model = Manual

        fields = ['id', 'name', 'number_of_pages', 'image', 'set']

    def clean_number_of_pages(self):
        data = self.cleaned_data['number_of_pages']
        if data <= 0:
            raise ValidationError('Neplatný počet stran, musí být větší než nula')
        return data


class SetModelForm(ModelForm):
    class Meta:
        model = Set

        fields = ['id', 'name', 'year', 'number_of_pieces', 'price', 'image']

    def clean_number_of_pieces(self):
        data = self.cleaned_data['number_of_pieces']
        if data <= 0:
            raise ValidationError('Neplatný počet dílků, musí být větší než nula')
        return data

    def clean_price(self):
        data = self.cleaned_data['price']
        if data <= 0:
            raise ValidationError('Neplatný cena, cena nemůže být záporná')
        return data

    def clean_year(self):
        data = self.cleaned_data['year']
        print(date.today().year)
        if data > date.today().year:
            raise ValidationError('Neplatný rok, rok nemůže přesáhnout ten letošní')
        return data

