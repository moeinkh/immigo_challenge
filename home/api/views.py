from .serializers import ItemSerializers
from ..models import Item
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

def get_api():
    url = 'https://feeds.npr.org/1004/feed.json'
    response = requests.get(url)
    data = response.json()['items'][:5]
    return data        

class ItemList(APIView):
    serializer_class = ItemSerializers

    def get(self, request):
        """
            retrieving a list of posts
        """
        data = get_api()
        for d in data:
            if not Item.objects.filter(id=d['id']).exists():
                Item.objects.create(id=d['id'], 
                url=d['url'],
                title=d['title'],
                summary=d['summary'],
                date_published=d['date_published'],
                author=d['author']['name'],
                )

        items = Item.objects.all()
        serializer = ItemSerializers(items, many=True)
        return Response(serializer.data)