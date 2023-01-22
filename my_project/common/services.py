def get_model_form(form, model, **kwargs):
    if model.objects.filter(**kwargs).exists():
        user_profile = model.objects.get(**kwargs)
        return form(instance=user_profile)
    else:
        return None


def post_model_form(form, model, request, **kwargs):
    if model.objects.filter(**kwargs).exists():
        user_profile = model.objects.get(**kwargs)
        return form(request.POST, request.FILES, instance=user_profile)
    else:
        return None

