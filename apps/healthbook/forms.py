from django import forms

from apps.healthbook.models import Contact, Feedback


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '例：鈴木太郎'}), label=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': '例：abc123@gmail.com'}), label=False)
    feedback = forms.TextField(widget=forms.Textarea(attrs={'placeholder': '言いたいことはここに'}), label=False)

    class Meta:
        model = Contact
        fields = ['name', 'email', 'feedback']


CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

USING_CHOICES = (
    ("1日以下", "1日以下"),
    ("3日間", "3日間"),
    ("1週間以内", "1週間以内"),
    ("2週間以内", "2週間以内"),
    ("1ヵ月以上", "1ヵ月以上"),
)


class FeedbackForm(forms.ModelForm):
    hb_content = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hb_design = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hb_change = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hb_feedback = forms.TextField(widget=forms.Textarea(attrs=()), label=False)

    vs_content = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    vs_design = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    vs_change = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    vs_feedback = forms.TextField(widget=forms.Textarea(attrs=()), label=False)

    fr_design = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    fr_use = forms.ChoiceField(choices=USING_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    fr_opinion = forms.TextField(widget=forms.Textarea(attrs=()), label=False)
    fr_change = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    fr_feedback = forms.TextField(widget=forms.Textarea(attrs=()), label=False)

    ct_design = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    ct_use = forms.ChoiceField(choices=USING_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    ct_opinion = forms.TextField(widget=forms.Textarea(attrs=()), label=False)
    ct_change = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    ct_feedback = forms.TextField(widget=forms.Textarea(attrs=()), label=False)

    hg_design = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hg_use = forms.ChoiceField(choices=USING_CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hg_opinion = forms.TextField(widget=forms.Textarea(attrs=()), label=False)
    hg_change = forms.ChoiceField(choices=CHOICES, label="", initial='', widget=forms.Select(), required=True)
    hg_feedback = forms.TextField(widget=forms.Textarea(attrs=()), label=False)

    class Meta:
        model = Feedback
        fields = ['hb_content', 'hb_design', 'hb_change', 'hb_feedback',
                  'vs_content', 'vs_design', 'vs_change', 'vs_feedback',
                  'fr_design', 'fr_use', 'fr_opinion', 'fr_change', 'fr_feedback',
                  'ct_design', 'ct_use', 'ct_opinion', 'ct_change', 'ct_feedback',
                  'hg_design', 'hg_use', 'hg_opinion', 'hg_change', 'hg_feedback']
