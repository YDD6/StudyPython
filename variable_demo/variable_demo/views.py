from django.shortcuts import render


class Person(object):
    def __init__(self, username):
        self.username = username


def index(request):
    p = Person('cxk')

    # context = {
    #     'person': {
    #         'username': 'ydd'
    #     }
    # }
    # context = {
    #     'persons':{
    #         'username':'ydd',
    #         'age':'21'
    #     }
    #
    # }
    context = {
        'comments': ['zyr你是傻逼吧'],
        'books': [
            {
                'name': 'python从入门到入土',
                'author': '哈哈',
                'price': '200'
            },
            {
                'name': 'mysql从入门到入土',
                'author': 'houhou',
                'price': '100'
            },
            {
                'name': 'java从入门到入土',
                'author': 'huhu',
                'price': '500'
            },
            {
                'name': 'script从入门到入土',
                'author': 'hahu',
                'price': '600'
            },
            {
                'name': 'c++从入门到入土',
                'author': 'heihei',
                'price': '300'
            },

        ]
    }
    return render(request, 'index.html', context=context)
