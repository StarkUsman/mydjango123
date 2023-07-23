from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} already exists")
        return data
    
        
    


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("Cleaned data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "new123":
    #         raise forms.ValidationError('This title is already taken')
    #     print("Title", title)
    #     return title
    
    def clean(self):
            data = self.cleaned_data 
            print("All data:", data) 
            title = data.get('title')
            content = data.get("title")
            if title.lower().strip() == "new123":
                self.add_error("title", "This title is taken")
                # raise forms.ValidationError('This title is already taken')
            if "new123" in content or "new123" in title.lower():
                self.add_error("content", "new123 can't be in cotent") # field error, specific to field
                raise forms.ValidationError("new123 is not allowed") #non field error, for entire form
            return data        