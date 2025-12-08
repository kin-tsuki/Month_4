from django import forms
from posts.models import Post


class PostCreateForm(forms.Form):
    image = forms.ImageField(required=False)
    title = forms.CharField(max_length=255, required=False)
    content = forms.CharField(max_length=1000, required=False)

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if not title or not content:
            raise forms.ValidationError("Title and content are required")
        if title.lower() == content.lower():
            raise forms.ValidationError("Title and content must be different")
        return cleaned_data
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("Title is required")
        if title.lower() == 'javascript':
            raise forms.ValidationError("Javascript is not allowed") 
        if len(title)< 3:
            raise forms.ValidationError("Title must be at least 3 characters")
        return title
    

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "title", "content"]

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if not title or not content:
            raise forms.ValidationError("Title and content are required")
        if title.lower() == content.lower():
            raise forms.ValidationError("Title and content must be different")
        return cleaned_data
    
    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("Title is required")
        if title.lower() == 'javascript':
            raise forms.ValidationError("Javascript is not allowed") 
        if len(title)< 3:
            raise forms.ValidationError("Title must be at least 3 characters")
        return title
    
class CommentForm(forms.Form):
    text = forms.CharField(max_length=1000)

    def clean_text(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        if not text:
            raise forms.ValidationError("The comment field is empty.")
        
        forbidden_words = ['javascript', 'python', 'pycharm', 'vscode']
        for word in forbidden_words:
            if word in text.lower():
                raise forms.ValidationError("Your comment contains unallowed words") 
            
        if len(text) < 2:
            raise forms.ValidationError("Comment must be at least 2 characters")
        return text

