from django.shortcuts import render,redirect
from django.utils import timezone
from .forms import BookForms,ModelBookForms,SearchForm
#render the class names
from newhome.models import Book
from django.contrib import messages
#from .forms1 import BookForms


#from newhome.models import Book
# Create your views here.

def form_view(request):
    msg=''
    if request.method =='POST':
        form=BookForms(request.POST)
        if form.is_valid():
            book=Book.objects.create(
                name=form.cleaned_data.get('name'),
                book_author=form.cleaned_data.get('author')
            )
            book.save()
            msg='Book Added Successfully!!!'
        else:
            msg=form.errors
    else:
        form=BookForms()
    return render(request,'forms.html',{"msg":msg, "forms":form})


def model_view(request):
    msg=''
    if request.method =='POST':
        form=ModelBookForms(request.POST)
        if form.is_valid():
            form.save()
            msg ='Book Added Successfully!!!'
        else:
            msg=form.errors
    else:
        form=ModelBookForms()
    return render(request,'forms.html',{"msg":msg,"form":form})

def html_form(request):
    value=''
    if request.method=='POST':
        value=request.POST.get('name')
        return render(request,'values.html',{'value':value})
    else:
        return render(request,'design.html')

def booksearch(request):
    if request.method== 'POST':
        form= SearchForm(request.POST)
        if form.is_valid():
            q=form.cleaned_data.get('q')
            #book = Book.objects.filter(name__contains=q, purchase_date__lte=timezone.now)
            book = Book.objects.filter(name__contains=q)
            form =None
            return render(request,'showtables.html',{'book':book,'form':SearchForm()})
    else:
            form=SearchForm
            book=Book.objects.all()
    return render(request,'showtables.html',{'book':book,'form':form})


def deletebook(request,id):
    print('id',id)
    book.delete()
    messages.success(request,'Deleted'+str(id)+'Successfully!!')
    return redirect("/")


def editbook(request):
    book = Book.objects.get(id = id)
    if request.method=="POST":
        form= ModelBookForms(requst.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book updated Successfully!!!')
            return redirect("/")
        else:
            form= ModelBookForms(instance = book)
    return render(request,"editbook.html",{'form':form})
    
    
    
    #form=CustomForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    


"""def newform_view(request):
    form=BookForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    context={
        "head":"Book form created here using python",
        "forms":form,
        
        #"books":book
    }
    return render(request,'newforms.html',context)


def form1_view(request):
    form1=BookForms()
    #book=Book.Objects.all()
    #book=Book.Objects.filter(name='',purchase_date='')
    context={
        "head":"Book form created here using python",
        "forms":form1,
        
        #"books":book
    }
    return render(request,'forms1.html',context)"""

