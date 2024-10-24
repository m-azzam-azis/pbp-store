from django.forms import ModelForm
from main.models import ShopEntry
from django.utils.html import strip_tags

class ShopEntryForm(ModelForm):
    class Meta:
        model = ShopEntry
        fields = ["name", "price", "description", "sold", "rating"]
        
        def clean_name(self):
            name = self.cleaned_data["name"]
            return strip_tags(name)
        
        def clean_price(self):
            price = self.cleaned_data["price"]
            return strip_tags(price)
        def clean_description(self):
            description = self.cleaned_data["description"]
            return strip_tags(description)
        def clean_sold(self):
            sold = self.cleaned_data["sold"]
            return strip_tags(sold)
        def clean_rating(self):
            rating = self.cleaned_data["rating"]
            return strip_tags(rating)