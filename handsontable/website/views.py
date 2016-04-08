from django.views.generic import TemplateView


class Website(TemplateView):
  template_name = 'index.html'

  def get_context_data(self, **kwargs):
    user = self.request.user
    context = super(Website, self).get_context_data(**kwargs)
    context['title'] = 'Euprime Handsontable interface'
    context['user'] = 'euprime'
    context['security_logout'] = ''
    return context

