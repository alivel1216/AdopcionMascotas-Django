"""Posts forms."""
#Django 
from django import forms

#models
from posts.models import Post


MASCOT_CATEGORY = [
    ('PERRO','Perro'),
    ('GATO','Gato'),
]
    
class PostForm(forms.ModelForm):
    """Post model form."""
    class Meta:
        """Form setting."""
        model = Post
        fields = ('user','profile', 'title','photo', 'category', 'description')
        """widgets = {
            #'user':forms.TextInput(attrs={'class':'form-control mr-3'}),
            'profile':forms.TextInput(attrs={'class':'form-control mr-3'}),
            'title':forms.TextInput(attrs={'class':'form-control mr-3'}),
            'photo':forms.ImageField(attrs={'class':'form-control mr-3'}),
            'category': forms.RadioSelect(choices=MASCOT_CATEGORY,attrs={'class':'form-control mr-3'} ),
            'description': forms.RadioSelect(choices=MASCOT_CATEGORY,attrs={'class':'form-control mr-3'} ),
        }"""