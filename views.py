from django.shorcuts import render, redirect
from django.http import HttpResponse
from .models import MovieInfo

def index(request):
	return render(request, "MovieReview/index.html",{'MovieName':['Life of pie', 'Hulk', 'Avengers']})

def AddMovie(request):
	return(request,"MovieReview/add_movie.html")

def add_movie_form_submission(request):
	print("Form is submitted")

	movie_name = request.POST["movie_name"]
	phone_number = request.POST["phone_number"]
	email= request.POST["email"]
	pic=request.POST["pic"]
	video=request.POST["video"]
    option=request.POST["option"]

    if request.method == 'POST' and request.FILES['pic']:
        myfile = request.FILES['pic']
        fs = FileSystemStorage()
        filename = fs.save(pic.name, pic)
        uploaded_file_url = fs.url(filename)
        
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

	movie_info = MovieInfo(movie_name=movie_name, phone_number=phone_number,
		email=email,pic=pic,video=video,option=option
        uploaded_file_url=uploaded_file_url,form=form)
    movie_info.save()
	
    return render(request, "MovieReview/add_movie.html")
'''
def simple_upload(request):
    if request.method == 'POST' and request.FILES['pic']:
        myfile = request.FILES['pic']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, "MovieReview/add_movie.html")
'''
'''
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })
'''