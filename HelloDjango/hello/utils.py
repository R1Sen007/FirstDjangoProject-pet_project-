from django.contrib.auth.mixins import AccessMixin


class OwnerPermissionsRequiredMixin(AccessMixin):
    
    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().is_owner(self.request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)