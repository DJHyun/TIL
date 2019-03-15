from django.shortcuts import render, redirect
from .models import Movie, Score


# Create your views here.
def movies_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    scores = movie.score_set.all()
    print(scores)
    return render(request, 'movies/detail.html', {'movie': movie, 'scores': scores})


def movie_delete(request, movie_id):
    movie = Movie.objects.get(id=movie_id).delete()
    return redirect('movies:movies_list')


def create_score(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    print(movie)
    if request.method == "POST":
        score = Score()
        score.content = request.POST.get('content')
        score.score = request.POST.get('score')
        score.movie_id = movie
        print(score.score)
        score.save()

    return redirect('movies:movie_detail', movie_id)


def delete_score(request, movie_id, score_id):
    score = Score.objects.get(id=score_id).delete()
    return redirect('movies:movie_detail', movie_id)
