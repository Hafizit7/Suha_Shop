from .models import Catagory

def catagory(request):
    g_cate = Catagory.objects.filter(pretn_catagory=None)
   

    context = {
        'g_cate':g_cate
        
    }
    return context