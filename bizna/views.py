from django.views import generic

from .models import Company, Events
from .forms import CompanyCreateForm

# Company Classes
class IndexView(generic.TemplateView):
    template_name = 'index.html'

class CompanyCreateView(generic.CreateView):
    model = Company
    form_class = CompanyCreateForm
    template_name = 'company_form'
    
    def form_valid(self, form):
        if form.is_valid():
            company = form.save(commit=False)
            company.created_by = self.request.user
            company.save()
        return super(CompanyCreateView, self).form_valid(form)
    
class KampuniListView(generic.ListView):
    model = Company
    template_name = 'company_list'
    
    def get_queryset(self):
        return Company.objects.all()
    
# Events Classes

class EventCreateView(generic.CreateView):
    model = Events
    template_name = 'event_form'
    
class EventListView(generic.ListView):
    model = Events
    template_name = 'event_list'
    
    def get_queryset(self):
        return Events.objects.order_by(Company)
    