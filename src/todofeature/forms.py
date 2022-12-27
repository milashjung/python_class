from django import forms
from todofeature.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        #exclude = ("image",) 

    def clean_field(self):
        name = self.cleaned_data.get["name"]
        if name.isdigit():
             raise forms.ValidationError("Name can not be number")
        return name
            
        


