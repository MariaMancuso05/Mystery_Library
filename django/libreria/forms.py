from django import forms
from .models import CartaFittizia, Profilo

class ProfiloForm(forms.ModelForm):
        class Meta:
            model = Profilo
            fields = ['nome', 'cognome', 'email', 'data_di_nascita', 'bio']
            widgets = {
            'data_di_nascita': forms.DateInput(attrs={'type': 'date'}),
        }
class CartaFittiziaForm(forms.ModelForm):
    class Meta:
        model = CartaFittizia
        fields = ['titolare_della_carta', 'numero_della_carta', 'data_di_scadenza', 'cvv']
        widgets = {
            'titolare_della_carta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome e cognome del titolare'}),
            'numero_della_carta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numero carta (16 cifre)', 'maxlength': '16'}),
            'data_di_scadenza': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/YY', 'maxlength': '5'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVV (3 cifre)', 'maxlength': '3'})
        }
        
    def clean_numero_della_carta(self):
        numero = self.cleaned_data.get('numero_della_carta')
        if not numero.isdigit() or len(numero) != 16:
            raise forms.ValidationError("Il numero della carta deve contenere esattamente 16 cifre numeriche.")
        return numero
        
    def clean_cvv(self):
        cvv = self.cleaned_data.get('cvv')
        if not cvv.isdigit() or len(cvv) != 3:
            raise forms.ValidationError("Il CVV deve contenere esattamente 3 cifre numeriche.")
        return cvv
        
    def clean_data_di_scadenza(self):
        scadenza = self.cleaned_data.get('data_di_scadenza')
        if len(scadenza) != 5 or scadenza[2] != '/':
            raise forms.ValidationError("La data di scadenza deve essere nel formato MM/YY.")
        try:
            mese = int(scadenza[:2])
            anno = int(scadenza[3:])
            if mese < 1 or mese > 12:
                raise forms.ValidationError("Il mese deve essere compreso tra 01 e 12.")
        except ValueError:
            raise forms.ValidationError("Formato data non valido. Usa MM/YY.")
        return scadenza
    
