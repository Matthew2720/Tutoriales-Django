from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label="Escribe tu nombre",max_length=10,help_text="Maximo 10 caracteres")
    url = forms.URLField(label="Tu sitio web",required=False,initial="http://")
    comment = forms.CharField()
    
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre: ",max_length=50,widget=forms.TextInput(attrs={'class' : 'input'}))
    email = forms.EmailField(label="Email: ", max_length=50)
    message = forms.CharField(label="Mensaje: ")