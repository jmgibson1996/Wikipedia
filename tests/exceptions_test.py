import unittest
from wikipedia import wikipedia

class TestWikipeidaException(unittest.TestCase):
    def test_wikipedia_exception_no_srsearch(self):
        with self.assertRaises(Exception) as context:
            wikipedia.search("")    # empty query
        self.assertFalse("wikipedia.exceptions.WikipediaException: An unknown error occured: \"{0}\". Please report it on GitHub!" in str(context.exception))
    
    def test_wikipedia_exception_invalid_coordinate(self):
        with self.assertRaises(Exception) as context:
            wikipedia.geosearch('40.67693', '117..23193')   # invalid coordinate
        self.assertFalse("wikipedia.exceptions.WikipediaException: An unknown error occured: \"{0}\". Please report it on GitHub!" in str(context.exception))

class TestPageError(unittest.TestCase):
    def test_page_error_query_does_not_match(self):
        with self.assertRaises(Exception) as context:
            wikipedia.summary("~!@")
        self.assertFalse("wikipedia.exceptions.PageError: \"{0}\" does not match any pages. Try another query!" in str(context.exception))

    def test_page_error_id_does_not_match(self):
        with self.assertRaises(Exception) as context:
            wikipedia.page("~!@")
        self.assertFalse("wikipedia.exceptions.PageError: Page id \"{0}\" does not match any pages. Try another id!" in str(context.exception))
    
class TestDisambiguationError(unittest.TestCase):
    def test_disambiguation_error_summary_function(self):
        with self.assertRaises(Exception) as context:
            wikipedia.summary("Mercury")
        self.assertFalse("wikipedia.exceptions.DisambiguationError: \"{0}\" may refer to: \n{1}" in str(context.exception))
    
    def test_disambiguation_error_page_function(self):
        with self.assertRaises(Exception) as context:
            wikipedia.page("New York")
        self.assertFalse("wikipedia.exceptions.DisambiguationError: \"{0}\" may refer to: \n{1}" in str(context.exception))

