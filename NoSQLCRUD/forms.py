from django import forms


# add a new task from
class InsertTaskForm(forms.Form):
    task_name = forms.CharField(max_length=50, required=True)
    category_name = forms.CharField(max_length=50, required=True)
    task_description = forms.CharField(widget=forms.Textarea, required=True)
    due_date = forms.DateField(required=True)
    is_urgent = forms.BooleanField(required=False)


# add a new category from
class InsertCategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50, required=True)
    category_description = forms.CharField(widget=forms.Textarea, required=True)
