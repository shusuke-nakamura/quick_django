from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
import random
from datetime import datetime
from django.db.models import Q
from django.db.models import Count

def index(request):
    return HttpResponse('こんにちは、世界！')

def temp(request):
    context = {
        'msg': 'こんにちは、世界!'
    }
    return render(request, 'main/temp.html', context)

def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html', {
        'books': books
    })

def iftag(request):
    return render(request, 'main/iftag.html', {
        'random': random.randint(0, 100)
    })
    
def yesno(request):
    return render(request, 'main/yesno.html', {
        'flag': True
    })

def firstof(request):
    return render(request, 'main/firstof.html', {
        #'a': 'おはようございます。',
        #'b': 'こんにちは',
        #'c': 'こんばんは',
    })

def forloop(request):
    return render(request, 'main/forloop.html', {
        'weeks': ['月','火','水','木','金','土','日']
    })

def forempty(request):
    return render(request, 'main/forempty.html', {
        # 'members': ['鈴木三郎', '佐藤洋子', '山田次郎']
        'members': []
    })
    
def fortag(request):
    return render(request, 'main/fortag.html')

def ifchanged(request):
    return render(request, 'main/ifchanged.html', {
        'schedule': [
            (10, 'A企画反省会'),
            (10, 'B書籍脱稿'),
            (15, 'WINGS定例会議'),
            (30, 'C企画打ち合わせ')
        ]
    })
    
def regroup(request):
    return render(request, 'main/regroup.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23'},
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13'},
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06'},
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28'},
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07'},
        ]
    })
    
def cycle(request):
    return render(request, 'main/cycle.html', {
        'members': [
            {'name': '鈴木三郎', 'sex': '男', 'birth': '1980-12-23'},
            {'name': '山田次郎', 'sex': '男', 'birth': '1978-10-13'},
            {'name': '佐藤健司', 'sex': '男', 'birth': '1976-04-06'},
            {'name': '山本花子', 'sex': '女', 'birth': '1981-07-28'},
            {'name': '田中久美', 'sex': '女', 'birth': '1980-09-07'},
        ]
    })
    
def escape(request):
    return render(request, 'main/escape.html', {
        'msg': '''<img src="https://wings.msn.to/image/wings.jpg" title="ロゴ" />
            <p>WINGSへようこそ</p>'''
    })
    
def temptag(request):
    return render(request, 'main/temptag.html')

def verbatim(request):
    return render(request, 'main/verbatim.html')

def master(request):
    return render(request, 'main/master.html', {
        'msg': 'こんにちは、世界！',
    })

def include(request):
    return render(request, 'main/include.html', {
        'name': '鈴木',
        'current': datetime.now(),
    })
    
def static(request):
    return render(request, 'main/static.html')

def strformat(request):
    return render(request, 'main/strformat.html', {
      'data1': None,
      'data2': 'WINGS\nWww INtegrated Guide on Server-architecture',
      'data3': 'https://wings.msn.to/',
      'data4': [ 'い', 'ろ', 'は', 'に', 'ほ', 'へ' ],
      'data5': 987.654,
      'data6': 'hello django'
    })
    
def slice(request):
    return render(request, 'main/slice.html', {
        'data': ['い', 'ろ', 'は', 'に', 'ほ', 'へ']
    })

def lists(request):
    return render(request, 'main/lists.html', {
        'data': [ 'いろは歌', [ 'い', 'ろ', 'は', 'に', 'ほ', 'へ','と' ] ]
    })
    
def date_time(request):
    return render(request, 'main/date_time.html', {
        'today': datetime.now()
    })

def filter(request):
    books = Book.objects.filter(publisher='翔泳社', price='2800')
    return render(request, 'main/book_list.html', {
        'books': books
    })
    
def exclude(request):
    books = Book.objects.exclude(publisher='翔泳社')
    return render(request, 'main/book_list.html', {
        'books': books
    })
    
def get(request):
    book = Book.objects.get(pk=1)
    return render(request, 'main/book_detail.html', {
        'book': book
    })

def filter_or(request):
    # books = Book.objects.filter(publisher='翔泳社').filter(price__gte=2800)
    # books = Book.objects.filter(Q(publisher='翔泳社') | Q(price__gte = 2800))
    books = Book.objects.filter(~Q(publisher='翔泳社') & (Q(published__year=2018) | Q(published__year=2020)))
    return render(request, 'main/book_list.html', {
        'books': books
    })

def filter_other(request):
    books = Book.objects.order_by('publisher', '-published')
    return render(request, 'main/book_list.html', {
        'books': books
    })
    
def groupby(request):
    return render(request, 'main/groupby.html', {
        'groups': Book.objects.values('publisher').annotate(pub_count=Count('publisher')).order_by('-pub_count')
    })

def union(request):
    b1 = Book.objects.filter(publisher='翔泳社')
    b2 = Book.objects.filter(publisher='技術評論社')
    return render(request, 'main/book_list.html', {
        'books': b1.union(b2)
    })

def raw(request):
    books = Book.objects.raw(
        'SELECT * FROM main_book WHERE publisher = %s', ['翔泳社']
    )
    return render(request, 'main/book_list.html', {
        'books': books
    })

def rel(request):
    return render(request, 'main/rel.html', {
        'book': Book.objects.get(pk=1)
    })

def rel2(request):
    return render(request, 'main/rel2.html', {
        'books': Book.objects.all()
    })
    
def route_param(request, id=1):
    return HttpResponse(f'id値: {id}')

def search(request, keywd):
    return HttpResponse(f'パラメータ: {keywd}')

def req_query(request):
    return HttpResponse(f'id値: {request.GET["id"]}')

def req_header(request):
    return HttpResponse(f'Use-Agent： {request.headers["User-Agent"]}')
