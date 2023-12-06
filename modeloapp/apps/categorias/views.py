from django.shortcuts import render

# Create your views here.

def add_categoria(request):
    template_name = 'categorias/add_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('categorias:list_categorias')
    form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_categorias(request):
    template_name = 'categorias/list_categorias.html'
    categories = Categoria.objects.filter()
    context = {
        'categorias': categorias
    }
    return render(request, template_name, context)

def edit_categoria(request, id_categoria):
    template_name = 'categorias/add_categoria.html'
    context ={}
    category = get_object_or_404(Categoria, id=id_categoria)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categorias)
        if form.is_valid():
            form.save()
            return redirect('categorias:list_categorias')
    form = CategoriaForm(instance=categorias)
    context['form'] = form
    return render(request, template_name, context)

def delete_categoria(request, id_categoria):
    Categoria = Categoria.objects.get(id=id_categoria)
    Categoria.delete()
    return redirect('categorias:list_categorias')