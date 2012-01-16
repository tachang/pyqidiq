import unittest
import os
import base64
from pyqidiq import QidiqAPI


class TestQidiqAPI(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    self.api = QidiqAPI(api_key="4ADOWCW3TMJKXEVIUQ4R")
    self.feed_url_path = base64.urlsafe_b64encode(os.urandom(20))[0:19]

  def test_create_feed(self):
    params = {
      'feed_url_path':  self.feed_url_path,
      'create_feed_name': 'pyqidiq test feed',
      'feed_description': "Qidiq test feed description",
      'feed_private': False
    }
    response = self.api.create_feed(**params)
    self.assertEqual(response['error_code'], 0)

  def test_get_feed(self):
    response = self.api.get_feed(feed_url_path=self.feed_url_path)
    self.assertEqual(response['error_code'], 0)
    self.assertEqual(response['feed']['url_path'], self.feed_url_path)

  def test_get_created_feed_list(self):
    response = self.api.get_created_feed_list()
    self.assertEqual(response['error_code'], 0)

  def test_get_subscribed_feed_list(self):
    response = self.api.get_subscribed_feed_list()
    self.assertEqual(response['error_code'], 0)
