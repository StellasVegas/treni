Заготовочки

#Последние пять строк:
	from django.http import HttpResponse

	from polls.models import Question


	def index(request):
	    latest_question_list = Question.objects.order_by('-pub_date')[:5]
	    output = ', '.join([p.question_text for p in latest_question_list])
	    return HttpResponse(output)



### Искючение
from django.http import Http404
from django.shortcuts import render

from polls.models import Question
# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'question': question})

#get_object_or_404
     question = get_object_or_404(Question, pk=question_id)



# Login requared
     from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

class ProtectedView(TemplateView):
    template_name = 'secret.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProtectedView, self).dispatch(*args, **kwargs)