from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

"""
    Base view for admin viewsactions.
    Decorator for viewsactions that checks that the user is logged in and is a staff
    member, redirecting to the login page if necessary.
    Look in Python3\Lib\site-packages\django\contrib\admin\viewsactions\decorators.py
            Python3\Lib\site-packages\django\contrib\auth\decorators.py
            Python3\Lib\site-packages\django\contrib\admindocs\viewsactions.py
"""
class BaseAdminView(View, LoginRequiredMixin, PermissionRequiredMixin):
    @method_decorator(staff_member_required(login_url='loginadmin'))
    def dispatch(self, request, *args, **kwargs):
        return super(BaseAdminView, self).dispatch(request, *args, **kwargs)