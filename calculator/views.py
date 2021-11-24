from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    context = {
        'recipe': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        }
    }
    if 'servings' in request.GET:
        servings = abs(int(request.GET.get('servings')))
        context = {
            'recipe': {
                'яйца, шт': 2 * servings,
                'молоко, л': 0.1 * servings,
                'соль, ч.л.': 0.5 * servings,
            }
        }
        return render(request, 'calculator/index.html', context)
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = {
        'recipe': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        }
    }
    if 'servings' in request.GET:
        servings = abs(int(request.GET.get('servings')))
        context = {
            'recipe': {
                    'макароны, г': 0.3 * servings,
                    'сыр, г': 0.05 * servings,
            }
        }
        return render(request, 'calculator/index.html', context)
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {
        'recipe': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        }
    }
    if 'servings' in request.GET:
        servings = abs(int(request.GET.get('servings')))
        context = {
            'recipe': {
                'хлеб, ломтик': 1 * servings,
                'колбаса, ломтик': 1 * servings,
                'сыр, ломтик': 1 * servings,
                'помидор, ломтик': 1 * servings,
            }
        }
        return render(request, 'calculator/index.html', context)
    return render(request, 'calculator/index.html', context)



