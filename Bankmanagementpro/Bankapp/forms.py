from django import forms
from Bankapp.models import Bank

class BankForm(forms.ModelForm):
	class Meta:
		model=Bank
		fields='__all__'