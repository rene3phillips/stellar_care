from django import forms
from .models import Billing

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['appointment', 'total_amount', 'payment_status', 'date_billed', 'due_date', 'notes']

    # Override __init__ to set the initial value of total_amount
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.total_amount is not None:
            self.fields['total_amount'].initial = f"{self.instance.total_amount:.2f}"