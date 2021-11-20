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
