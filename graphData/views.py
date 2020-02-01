from django.shortcuts import render, redirect, get_object_or_404
from .models import GraphData, Category
from .forms import CategoryForm, GraphDataForm
from django.contrib.auth.decorators import login_required


def top(request):
    datas = GraphData.objects.all().order_by('studyDay')
    params = {
        'datas': datas
    }
    return render(request, 'top.html', params)


@login_required
def index(request):
    graphData = GraphData.objects.order_by('studyDay')
    return render(request, 'graphData/index.html', {'graphData': graphData})


@login_required
def delete(request, id):
    graphData = get_object_or_404(GraphData, pk=id)
    graphData.delete()
    return redirect('graphData:index')


@login_required
def graphData_category(request, category):
    category = Category.objects.get(title=category)
    graphData = GraphData.objects.filter(category=category).order_by('title')
    params = {'graphData': graphData, 'category': category}
    return render(request, 'graphData/index.html', params)


@login_required
def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('graphData:index')
    else:
        form = CategoryForm
    return render(request, 'graphData/new_category.html', {'form': form})


@login_required
def new_graphData(request):
    if request.method == 'POST':
        form = GraphDataForm(request.POST)
        if form.is_valid():
            graphData = form.save(commit=False)
            graphData.user = request.user
            form.save()
            return redirect('graphData:index')
    else:
        form = GraphDataForm
    return render(request, 'graphData/new_graphData.html', {'form': form})
