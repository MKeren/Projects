from django import forms
from .models import (
    AreaElectiveCourse_Computer_OldCatalog,
    AreaElectiveCourse_Computer_Newcatalog,
    AreaElectiveCourse_civil_OldCatalog,
    AreaElectiveCourse_Civil_Newcatalog,
    AreaElectiveCourse_EE_OldCatalog,
    AreaElectiveCourse_EE_Newcatalog,
    AreaElectiveCourse_AI_Catalog,
    AreaElectiveCourse_Software_Newcatalog,
    AreaElectiveCourse_Software_Oldcatalog
)

# Map department and catalog to the appropriate model
model_mapping = {
    'Computer': {
        'old': AreaElectiveCourse_Computer_OldCatalog,
        'new': AreaElectiveCourse_Computer_Newcatalog,
    },
    'Civil': {
        'old': AreaElectiveCourse_civil_OldCatalog,
        'new': AreaElectiveCourse_Civil_Newcatalog,
    },
    'EE': {
        'old': AreaElectiveCourse_EE_OldCatalog,
        'new': AreaElectiveCourse_EE_Newcatalog,
    },
    'AI': {
        'new': AreaElectiveCourse_AI_Catalog,
    },
    'Software': {
        'old': AreaElectiveCourse_Software_Oldcatalog,
        'new': AreaElectiveCourse_Software_Newcatalog,
    }
}


class TranscriptUploadForm(forms.Form):
    file = forms.FileField()


class DynamicAreaElectiveCourseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        # Capture department and catalog from kwargs
        department = kwargs.pop('department', None)
        catalog = kwargs.pop('catalog', None)
        
        # Dynamically set the model for the form based on department and catalog
        if department and catalog:
            try:
                self.Meta.model = model_mapping[department][catalog]
            except KeyError:
                raise ValueError("Invalid department or catalog selection")
        
        super().__init__(*args, **kwargs)

    class Meta:
        model = None  # This will be dynamically set in the __init__ method
        fields = ['course_code', 'title', 'category', 'hours_lecture', 'hours_tutorial', 'hours_lab', 'total_credits', 'ects_credit']
