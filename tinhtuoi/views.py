from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from datetime import date
from .models import Calculate, GenDoc
# from transformers import GPT2Tokenizer, GPT2LMHeadModel

def statistic():
  right = Calculate.objects.filter(status=True).count()
  wrong = Calculate.objects.filter(status=False).count()
  total = Calculate.objects.count()

  return {
    'right': right,
    'wrong': wrong,
    'total': total
  }

def index(request):
    return render(request, 'tinhtuoi/index.html', statistic())

def calculate(request):
    year = request.POST['year']
    today = date.today()
    result = today.year - int(year)
    f = Calculate(status=None)
    f.save()
    return redirect('index', {**statistic(), 'tuoi': result})

def feedback(request):
    if request.POST['feedback'] is not None:
        f = Calculate(status=request.POST['feedback'])
        f.save()
    return HttpResponseRedirect(reverse('tinhtuoi:index'))

# def gen_doc(request):
#     tokenizer = GPT2Tokenizer.from_pretrained('NlpHUST/gpt2-vietnamese')
#     model = GPT2LMHeadModel.from_pretrained('NlpHUST/gpt2-vietnamese')

#     text = request.POST['sentence']
#     doc = GenDoc(text=text)
#     doc.save()
#     input_ids = tokenizer.encode(text, return_tensors='pt')
#     max_length = 100

#     sample_outputs = model.generate(input_ids,pad_token_id=tokenizer.eos_token_id,
#                                       do_sample=True,
#                                       max_length=max_length,
#                                       min_length=max_length,
#                                       top_k=40,
#                                       num_beams=5,
#                                       early_stopping=True,
#                                       no_repeat_ngram_size=2,
#                                       num_return_sequences=1)

#     return render(request, 'tinhtuoi/index.html', {**statistic(), 'doc': tokenizer.decode(sample_outputs[0].tolist())})                              
