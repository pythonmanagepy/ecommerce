from django.shortcuts import render
from secondapp.models import Contact,Category,Register_table,Addproduct,Cout,placeOrder
from django.contrib.auth.models import User

# Create your views here.
def index(request):
	return render(request,"index.html")

def home(request):
	cat=Category.objects.all()
	dic={
	'cat':cat,
	}
	return render(request,"home.html",dic)

def about(request):
	return render(request,"about.html")

def contact(request):
	if request.method=="POST":
		name=request.POST["name"]
		con = request.POST["contact"]
		sub=request.POST["subject"]
		msz=request.POST["message"]

		data=Contact(name=name,contact=con,subject=sub,message=msz)
		data.save()
		res="Thanks for your feedback"
		return render(request,"contact.html",{"status":res})


	return render(request,"contact.html")

def register(request):
	if request.method=="POST":
		fname=request.POST["first"]
		lname=request.POST["last"]
		usr=request.POST["uname"]
		pwd=request.POST["password"]
		ut=request.POST["utype"]
		pn=request.POST["phone"]

		print(request.POST)
		usr=User.objects.create_superuser(pn,usr,pwd)
		usr.first_name=fname
		usr.last_name=lname
		usr.save()

		reg=Register_table(user=usr,contact_no=pn)
		reg.save()

	return render(request,"register.html")

def check_user(request):
	return HttpResponse("hello")

def allprod(request,pk):
	c=Category.objects.get(id=pk)
	p=Addproduct.objects.all()
	context={
	'p':p,
	'c':c,
	}


	return render(request,"allproduct.html",context)

def oneproduct(request,pk):
	qs=Addproduct.objects.get(product_id=pk)
	context={
	'qs':qs,
	}
	return render(request,"singleproduct.html",context)

def cfout(request):
	if request.method=="POST":
		name=request.POST["valtest"]
		text=request.POST["text"]
		reg=Cout(value_cart=name,item=text)
		reg.save()
	return render(request,"about.html")

def placeorder(request):

	if request.method=="POST":
		name=request.POST["name"]
		con = request.POST["contact"]
		add=request.POST["add"]
		namei=request.POST["valtest"]
		
		reg=placeOrder(name=name,contact=con,add=add,item=namei)
		reg.save()
	return render(request,"placeorder.html")






