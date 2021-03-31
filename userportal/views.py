from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Doc_Detail,Private_Doc, Contact


# Create your views here.
def index(request):
	return render(request, "index.html")

def handlesignup(request):
	if request.method == 'POST':
 		# get parameters
 		username = request.POST['email']
 		email = request.POST['email']
 		fname = request.POST['firstname']
 		lname = request.POST['lastname']
 		pass1 = request.POST['passwd']

 		# Create user
 		myuser = User.objects.create_user(username, email, pass1)
 		myuser.first_name = fname
 		myuser.last_name = lname
 		myuser.save()
 		messages.success(request,"your account has been created successfully.")
 		return redirect('/login/')

def handlesignin(request):
	if request.method == 'POST':
		loginusername = request.POST['username']
		loginpassword = request.POST['password']

		user = authenticate(username=loginusername, password=loginpassword)

		if user is not None:
			login(request,user)
			messages.success(request,"Successfully logged In.")
			return redirect('/first/')
		else:
			messages.error(request,"Invalid credentials, Please try again.")
			return redirect('/login/')
	return render(request, 'login.html')

def handlelogout(request):
	logout(request)
	messages.success(request,"Successfully logged out.")
	return redirect('/')

def first(request):
	return render(request, "first.html")


def docadd(request):
	if request.method == 'POST':
		doc_t = request.POST.get('doc_t', '')
		doc_cat = request.POST.get('doc_cat', '')
		doc_tech = request.POST.get('doc_tech', '')
		doc_file = request.FILES['document']
		# print(doc_cat)
		extension = str(doc_file).split(".")
		# print(extension)
		# print(type(extension[1]))
		if doc_cat == extension[1]:
			doc = Doc_Detail(doc_user=request.user, doc_category=doc_cat, doc_title=doc_t, doc_tech=doc_tech, doc=doc_file)
			doc.save()
			yes = "yes"
			return render(request, "first.html",{'yes':yes, 'msg':"Uploaded"})
		else:
			yes = "no"
			return render(request, "first.html",{ 'yes':yes, 'msg':"Selected Type and Document Type are Different!"})

	else:
		return HttpResponse('<h1>Go Home :)</h1>')

def p_docadd(request):
	if request.method == 'POST':
		doc_t = request.POST.get('doc_t', '')
		doc_cat = request.POST.get('doc_cat', '')
		doc_tech = request.POST.get('doc_tech', '')
		doc_pass = request.POST.get('pass','')
		doc_file = request.FILES['document']
		# print(doc_cat)
		extension = str(doc_file).split(".")
		# print(extension)
		# print(type(extension[1]))
		if doc_cat == extension[1]:
			doc = Private_Doc(pdoc_user=request.user, pdoc_category=doc_cat, pdoc_title=doc_t, pdoc_tech=doc_tech, pdoc_pass=doc_pass, pdoc=doc_file)
			doc.save()
			yes = "yes"
			return render(request, "first.html",{'yes':yes, 'msg':"Uploaded"})
		else:
			yes = "no"
			return render(request, "first.html",{ 'yes':yes, 'msg':"Selected Type and Document Type are Different!"})

	else:
		return HttpResponse('<h1>Go Home :)</h1>')

def doc1(request):
	doc = Doc_Detail.objects.all()
	doc2 = Private_Doc.objects.all()
	return render(request, 'doc1.html', {'doc1' : doc, 'doc2': doc2})

def doc_access(request, pid):
	p_doc = Private_Doc.objects.filter(p_id=pid)
	doc = Doc_Detail.objects.all()
	doc2 = Private_Doc.objects.all()

	if request.method == "POST":
		password = request.POST.get('pass3', '')

		if p_doc[0].pdoc_pass == password:
			yes = "yes"
			return render(request, 'doc1.html', {
				'doc1' : doc,
				'doc2': doc2,
				'yes':yes,
				'msg' : 'Congrats, Now you can access Your Document..'
				})
		else:
			yes = "no"
			return render(request, 'doc1.html', {
				'doc1' : doc,
				'doc2': doc2,
				'yes':yes,
				'msg' : 'Sorry, Password not match...'
				})
	else:
		return HttpResponse("<h1>Go Home :)</h1>")

def about(request):
	return render(request, 'about.html')

def doc2(request):
	doc = Doc_Detail.objects.filter(doc_user = request.user)
	doc2 = Private_Doc.objects.filter(pdoc_user = request.user)
	return render(request, 'doc2.html', {'doc1' : doc, 'doc2': doc2})

def document(request):
	l1 = Doc_Detail.objects.all()
	return render(request, 'document.html', {
		'list1' : l1
		})

def contact(request):
	if request.method == "POST":
		fname = request.POST.get('fname', '')
		lname = request.POST.get('lname', '')
		cmail = request.POST.get('cemail', '')
		cmsg = request.POST.get('msg', '')

		con = Contact(c_first_name=fname, c_last_name=lname, c_email=cmail, c_msg=cmsg)
		con.save()
		yes = "yes"
		return render(request, 'contact.html', {
			'yes' : yes,
			'msg' : 'Thank you for your details...'
			})
	else:
		return render(request, 'contact.html')

def doc_delete(request, docid):
	doc = Doc_Detail.objects.filter(doc_user = request.user)
	doc2 = Private_Doc.objects.filter(pdoc_user = request.user)
	pub_doc = Doc_Detail.objects.filter(doc_id=docid)
	pub_doc.delete()
	yes = "yes"
	return render(request, "doc2.html", {
		'doc1' : doc,
		'doc2': doc2,
		'yes' : yes,
		'msg' : "Public Document Deleted Successfully..."
		})

def pdoc_delete(request, pdocid):
	doc = Doc_Detail.objects.filter(doc_user = request.user)
	doc2 = Private_Doc.objects.filter(pdoc_user = request.user)
	pdoc = Private_Doc.objects.filter(p_id=pdocid)
	pdoc.delete()
	yes = "yes"
	return render(request, "doc2.html", {
		'doc1' : doc,
		'doc2': doc2,
		'yes' : yes,
		'msg' : 'Private Document Deleted Successfully...'
		})
