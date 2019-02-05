from django.shortcuts import render, get_object_or_404
from capdb.models import Jurisdiction, Court, Reporter
from collections import OrderedDict


def view_jurisdiction(request, jurisdiction_id):
    jurisdiction = get_object_or_404(Jurisdiction, pk=jurisdiction_id)
    fields = _get_fields(jurisdiction)
    return render(request, "view_metadata.html", {
        'fields': fields,
        'type': 'jurisdiction',
        'title': jurisdiction.name
    })


def view_reporter(request, reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    fields = _get_fields(reporter)
    return render(request, "view_metadata.html", {
        'fields': fields,
        'type': 'reporter',
        'title': reporter.short_name
    })


def view_court(request, court_id):
    court = get_object_or_404(Court, pk=court_id)
    fields = _get_fields(court)

    return render(request, "view_metadata.html", {
        'fields': fields,
        'type': 'court',
        'title': court.name_abbreviation
    })


def search(request):
    return render(request, "search.html")


def _get_fields(object):
    fields = OrderedDict()
    for field in object._meta.get_fields():
        print(field.name, field.get_internal_type())
        if field.get_internal_type() == "ManyToManyField" or field.get_internal_type() == "ForeignKey":
            continue
        try:
            fields[field.name.replace("_", " ").title()] = getattr(object, field.name)
        except AttributeError as e:
            print(e)
    return fields
