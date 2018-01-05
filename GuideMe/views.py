
from django.views import generic


class indexView(generic.ListView):
    template_name = 'index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return ""



