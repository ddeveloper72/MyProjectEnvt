from django import forms


# add a new task from
class InsertTaskForm(forms.Form):
    task_name = forms.CharField()
    category_name = forms.CharField()
    task_description = forms.CharField()
    due_date = forms.DateField()
    is_urgent = forms.CharField()
    # created_date = forms.DateField(required=True)


# add a new category from
class InsertCategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50, required=True)
    category_description = forms.CharField(
        widget=forms.Textarea, required=True)
