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

    def test_symbol_details_PATCH(self):
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

    def test_article_pagination_GET(self):
        symbol1 = Symbols.objects.create(
            symbol="TEST"
        )
        for i in range(5):
            Article.objects.create(
                 title='2022 Oscars preview: The awards show is back but it wont be a traditional Oscars',
                 description='Heres what to expect at this years Academy Awards.',
                 article_link='https://finance.yahoo.com/news/2022-oscars-preview-award-show-still-in-a-very-unusual-marketplace-135220904.html?.tsrc=rss',
                 publish_date='Sat, 26 Mar 2022 13:56:03 +0000',
                 external_id='8970a92a-11d6-4244-9132-c0206ba248f5',
                 created_at='2022-03-26 18:13:10.584117 +00:00',
                 updated_at='2022-03-26 18:16:03.479667 +00:00',
                 symbol_id=symbol1.id
              )
        for i in range(5):
            Article.objects.create(
                 title='2021 Oscars',
                 description='Heres what to expect at this years Academy Awards.',
                 article_link='https://finance.yahoo.com/news/2022-oscars-preview-award-show-still-in-a-very-unusual-marketplace-135220904.html?.tsrc=rss',
                 publish_date='Sat, 26 Mar 2022 13:56:03 +0000',
                 external_id='8970a92a-11d6-4244-9132-c0206ba248f5',
                 created_at='2022-03-26 18:13:10.584117 +00:00',
                 updated_at='2022-03-26 18:16:03.479667 +00:00',
                 symbol_id=symbol1.id
              )

        response = self.client.get(reverse('article-list'))

        response_with_page_size_param = self.client.get(reverse('article-list'), {'page_size': 1})

        response_second_page_title = self.client.get(reverse('article-list'), {'page': 2})
        response_second_page_title = response_second_page_title.json()['results'][0]['title']
        response_first_page_title = response.json()['results'][0]['title']

        self.assertEquals(len(response.json()['results']), 5)
        self.assertEquals(len(response_with_page_size_param.json()['results']), 1)
        self.assertNotEquals(response_first_page_title, response_second_page_title)








