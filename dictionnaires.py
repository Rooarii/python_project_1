from django.http import Http404

class Article():
    Articles = [{'id':1, 'titre': 'Premier Article', 'Commentaire': 'Téléphone Iphone'},
                {'id':2, 'titre': 'Deuxième Article', 'Commentaire': 'Téléphone Samsung'},
                {'id':3, 'titre': 'Troisième Article', 'Commentaire': 'Téléphone HTC'},
                {'id':4, 'titre': 'Quatrième Article', 'Commentaire': 'Téléphone SONY'},
                {'id':5, 'titre': 'Cinquième Article', 'Commentaire': 'Ecouteur Radio'},
    ]

    @classmethod
    def all(cls):
        return cls.Articles

    @classmethod
    def find(cls, id):
        try:
            return cls.Articles[int(id) -1]
        except :
            raise Http404('Page Not Found erreur 404')