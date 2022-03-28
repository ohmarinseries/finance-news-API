import json
from django.test import TestCase, Client
from django.urls import reverse
from financeAPI.models import Article, Symbols


class TestViews(TestCase):

    def setup(self):
        self.client = Client()

    def test_symbol_list_GET(self):
        response = self.client.get(reverse('symbol-list'))

        self.assertEquals(response.status_code, 200)

    def test_symbol_details_GET(self):
        symbol1 = Symbols.objects.create(
            symbol="TEST"
        )

        response = self.client.get(reverse('symbol-details', args=[symbol1.id]))

        self.assertEquals(response.status_code, 200)

    def test_symbol_list_POST(self):
        response = self.client.post(reverse('symbol-list'), {
            'symbol': 'TEST'
        })

        symbol1 = Symbols.objects.get(symbol='TEST')

        self.assertEquals(symbol1.symbol, 'TEST')
        self.assertEquals(response.status_code, 201)

    def test_symbol_details_PUT(self):
        symbol1 = Symbols.objects.create(
            symbol="TEST"
        )
        data = json.dumps({'symbol': 'test'})

        response = self.client.patch(reverse('symbol-details', args=[symbol1.id]), data, content_type='application/json')

        symbol1_updated = Symbols.objects.get(pk=symbol1.id)

        self.assertNotEquals(symbol1.symbol, symbol1_updated.symbol)
        self.assertEquals(response.status_code, 200)

    def test_symbol_details_DELETE(self):
        symbol1 = Symbols.objects.create(
            symbol="TEST"
        )

        response = self.client.delete(reverse('symbol-details', args=[symbol1.id]))

        symbol1_deleted = Symbols.objects.get_or_none(symbol='TEST')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(symbol1_deleted, None)

    def test_article_list_GET(self):
        response = self.client.get(reverse('article-list'))

        self.assertEquals(response.status_code, 200)





