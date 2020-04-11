from django.http import HttpResponseBadRequest

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)
    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

def listID_requeired(f):
    def wrap(request, *args, **kwargs):
        if request.POST.get('listid'):
            return f(request, *args, **kwargs)
        return HttpResponseBadRequest()
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap