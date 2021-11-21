from django.template import loader
from django.http import HttpResponse
from petitioner_app.models import VehRegister, VehDeregister, VehReregister, Application


# Create your views here.
def landing(request):
    template = loader.get_template('clerk_app/landing_page.html')
    return HttpResponse(template.render({}, request))


def myissues(request):

    current_user_id = request.user.id
    my_issues = Application.objects.filter(clerk=current_user_id)
    template = loader.get_template('clerk_app/my_issues.html')

    vehregister_applications = []
    vehderegister_applications = []
    vehreregister_applications = []

    for issue in my_issues:
        if issue.vehregister_form is not None:
            vehregister_applications.append(issue)
        elif issue.vehderegister_form is not None:
            vehderegister_applications.append(issue)
        elif issue.vehreregister_form is not None:
            vehreregister_applications.append(issue)

    context = {
        'vehregister_applications': vehregister_applications,
        'vehderegister_applications': vehderegister_applications,
        'vehreregister_applications': vehreregister_applications,
    }

    return HttpResponse(template.render(context, request))


def singleissue(request, form_type, form_id):

    template = loader.get_template('clerk_app/singleissue.html')

    if form_type == "vehregister":
        form = VehRegister.objects.filter(id=form_id)

        context = {
            'form_type': "vehregister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
    elif form_type == "vehderegister":
        form = VehDeregister.objects.filter(id=form_id)

        context = {
            'form_type': "vehderegister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
    elif form_type == "vehreregister":
        form = VehReregister.objects.filter(id=form_id)

        context = {
            'form_type': "vehreregister",
            'form': form[0],
        }
        return HttpResponse(template.render(context, request))
