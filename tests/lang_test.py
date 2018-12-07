# -*- coding: utf-8 -*-
import unittest

from wikipedia import wikipedia


class TestLang(unittest.TestCase):
  """Test the ability for wikipedia to change the language of the API being accessed."""

  def test_set_lang_fr(self):
    wikipedia.set_lang("fr")
    self.assertEqual(wikipedia.API_URL, 'http://fr.wikipedia.org/w/api.php')
  
  def test_set_lang_it(self):
    wikipedia.set_lang("zh")
    self.assertEqual(wikipedia.API_URL, 'http://zh.wikipedia.org/w/api.php')

  def test_set_lang_then_back_to_eng(self):
    # set language to Spanish
    wikipedia.set_lang("es")
    self.assertEqual(wikipedia.API_URL, 'http://es.wikipedia.org/w/api.php')
      
    # revert language back to English
    wikipedia.set_lang("en")
    self.assertEqual(wikipedia.API_URL, 'http://en.wikipedia.org/w/api.php')

  def test_change_through_multiple_langs(self):
    # set language to Swedish
    wikipedia.set_lang("sv")
    self.assertEqual(wikipedia.API_URL, 'http://sv.wikipedia.org/w/api.php')
    
    # switch language to German
    wikipedia.set_lang("de")
    self.assertEqual(wikipedia.API_URL, 'http://de.wikipedia.org/w/api.php')

    # switch language to Russian
    wikipedia.set_lang("ru")
    self.assertEqual(wikipedia.API_URL, 'http://ru.wikipedia.org/w/api.php')

    # switch language to Polish
    wikipedia.set_lang("pl")
    self.assertEqual(wikipedia.API_URL, 'http://pl.wikipedia.org/w/api.php')
    
    # switch language to Portuguese
    wikipedia.set_lang("pt")
    self.assertEqual(wikipedia.API_URL, 'http://pt.wikipedia.org/w/api.php')
