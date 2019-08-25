from django.shortcuts import render
from django.views.generic.edit import UpdateView, View
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
import datetime


# class UserUpdate(UpdateView):
# 	model = User
# 	fields = [
# 	'name'
# 	]
# 	template_name = 'settings.html'

# 	def dispatch(self, request, *args, **kwargs):
#         handler = super(UserUpdate, self).dispatch(request, *args, **kwargs)
#         if self.object.submitted_by != self.request.user:
#             return HttpResponseForbidden("You didn't create this item.")
#         return handler

#     def form_valid(self, form):
#        user = form.save()
#        user.date_edited =  datetime.date.today()
#        user.save()
#        return HttpResponseRedirect(reverse_lazy(''))

# # class SettingsView(TemplateView)
# # 	model = User
# # 	template_name = 'settings.html'

# # 	def get_context_data(self, **kwargs):
# #         context = super().get_context_data(**kwargs)
# #         context['user_info'] = User.objects.all()[:5]
# #         return context
