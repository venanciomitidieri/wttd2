from django.core import mail
from django.test import TestCase


class SubscriblePostValid(TestCase):
    def setUp(self):
        data = dict(name='Venancio Mota', cpf='15332920784',
                    email='venanciomitidieri@gmail.com', phone='21-983474494')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'venanciomitidieri@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['venanciomitidieri@gmail.com', 'venanciomitidieri@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Venancio Mota',
            '15332920784',
            'venanciomitidieri@gmail.com',
            '21-983474494',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
