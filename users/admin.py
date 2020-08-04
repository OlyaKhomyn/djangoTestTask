from django.contrib import admin
from django import forms
from users.models import User
from django.urls import path
from django.shortcuts import redirect
from users.csv_parser import parse


class CsvUploadForm(forms.Form):
    csv_file = forms.FileField()


class CsvUploadAdmin(admin.ModelAdmin):

    change_list_template = 'csv_form.html'

    def get_urls(self):
        urls = super().get_urls()
        additional_urls = [
            path("upload-csv/", self.upload_csv),
        ]
        return additional_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra = extra_context or {}
        extra["csv_upload_form"] = CsvUploadForm()
        return super(CsvUploadAdmin, self).changelist_view(request, extra_context=extra)

    def upload_csv(self, request):
        if request.method == "POST":
            if request.FILES['csv_file'].name.endswith('csv'):
                file = request.FILES['csv_file']
                parse(file)
            else:
                self.message_user(
                    request,
                    "Incorrect file type: {}".format(
                        request.FILES['csv_file'].name.split(".")[1]
                    )
                )
        return redirect("..")


@admin.register(User)
class UserAdmin(CsvUploadAdmin):
    pass
