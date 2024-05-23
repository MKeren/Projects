from django import forms


class TranscriptUploadForm(forms.Form):
    file = forms.FileField()


                