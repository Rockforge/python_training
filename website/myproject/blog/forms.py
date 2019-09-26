from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=30)
    comments = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(required=False)
    upload = forms.FileField(required=False)

    # Override method
    def clean(self):
        # Call the clean function of the parent
        super().clean()
        # self.data.get('hello') # access unclean data
        # cleaned_data is a dictionary
        if 'shit' in self.cleaned_data.get('comments'):
            self._errors['comments'] = self.error_class(['No bad words'])

        # always return self.cleaned_data
        return self.cleaned_data
