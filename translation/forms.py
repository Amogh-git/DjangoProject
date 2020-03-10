from django import forms


class InputForm(forms.Form):
    inputText = forms.CharField(label='enter input here...', max_length=500, widget=forms.Textarea(
        attrs={'rows': 10, 'cols': 50, 'placeholder': '   input goes here...', 'id': 'box1', 'name': 'pin'}))

    # outputtext = forms.CharField(label='मराठी अनुवाद्', max_length=500, widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'placeholder': 'मराठी अनुवाद्'}))
    class Meta:
        fields = "__all__"
