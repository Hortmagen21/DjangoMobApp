import my_auth.models as auth_models
from.forms import ProfileForm
import common.services as common_services


def get_profile_form(request):
    data = {
        "user": request.user
    }
    return common_services.get_model_form(form=ProfileForm, model=auth_models.Profile, **data)


def post_profile_form(request):
    data = {
        "user": request.user
    }
    return common_services.post_model_form(form=ProfileForm, model=auth_models.Profile, request=request, **data)

