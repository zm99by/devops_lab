from unittest import TestCase
import handlers.pulls

template = [
    {
        'number': '1',
        'title': 'homework1',
        'state': 'open',
        'labels': [],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/1'
    },
    {
        'number': '2',
        'title': 'homework2',
        'state': 'closed',
        'labels': [],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/2'
    },
    {
        'number': '3',
        'title': 'homework3',
        'state': 'open',
        'labels': [
            {'name': 'accepted'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/3'
    },
    {
        'number': '4',
        'title': 'homework4',
        'state': 'open',
        'labels': [
            {'name': 'needs work'}
        ],
        'html_url': 'https://github.com/alenaPy/devops_lab/pull/4'
    }
]

full_list = [
    {
        'num': '1',
        'title': 'homework1',
        'link': 'https://github.com/alenaPy/devops_lab/pull/1'
    },
    {
        'num': '2',
        'title': 'homework2',
        'link': 'https://github.com/alenaPy/devops_lab/pull/2'
    },
    {
        'num': '3',
        'title': 'homework3',
        'link': 'https://github.com/alenaPy/devops_lab/pull/3'
    },
    {
        'num': '4',
        'title': 'homework4',
        'link': 'https://github.com/alenaPy/devops_lab/pull/4'
    }
]

open_list = [
    {
        'num': '1',
        'title': 'homework1',
        'link': 'https://github.com/alenaPy/devops_lab/pull/1'
    },
    {
        'num': '3',
        'title': 'homework3',
        'link': 'https://github.com/alenaPy/devops_lab/pull/3'
    },
    {
        'num': '4',
        'title': 'homework4',
        'link': 'https://github.com/alenaPy/devops_lab/pull/4'
    }
]

closed_list = [
    {
        'num': '2',
        'title': 'homework2',
        'link': 'https://github.com/alenaPy/devops_lab/pull/2'
    }
]

accepted_list = [
    {
        'num': '3',
        'title': 'homework3',
        'link': 'https://github.com/alenaPy/devops_lab/pull/3'
    }
]

needs_work_list = [
    {
        'num': '4',
        'title': 'homework4',
        'link': 'https://github.com/alenaPy/devops_lab/pull/4'
    }
]


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_d(self):
        """Test for get_d"""
        self.assertEqual(handlers.pulls.get_d(template), full_list)

    def test_get_pulls(self):
        """Test for get_pulls"""
        self.assertEqual(handlers.pulls.get_pulls("accepted", template), accepted_list)
        self.assertEqual(handlers.pulls.get_pulls("needs work", template), needs_work_list)
        self.assertEqual(handlers.pulls.get_pulls("open", template), open_list)
        self.assertEqual(handlers.pulls.get_pulls("closed", template), closed_list)

    def tearDown(self):
        """Finish"""
