from django import forms

class FileForm(forms.Form):
    file = forms.FileField()
    split = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ex. [10,20,30]', 'style': 'width: 200px;', 'class': 'form-control'}),label="What timestamps would you like to split at?")