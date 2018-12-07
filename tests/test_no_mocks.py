import unittest

from decimal import Decimal
from wikipedia import wikipedia

class TestQueryOperations(unittest.TestCase):
    def test_search(self):
        _search = wikipedia.search("Queen")[1]
        assert test_search == "u\'Queen (band)\'"

    def test_suggest(self):
        _suggest = wikipedia.suggest("Drum Corpse International")
        assert _suggest == "u\'drum corps international\'"

    def test_summary(self):
        _summary = wikipedia.summary("Hello world")
        assert _summary == "u\'A \"Hello, World!\" program is a computer program that ouputs or displays the message \"Hello, World!\". Because it is very simple in most programming languages, it is often used to illustrate the basic syntax of a programming language and is often the first program people write.\'"

class TestPageOperations(unittest.TestCase):
    def test_page(self):
        _page = wikipedia.page("Foobar")
        assert _page == "<WikipediaPage \'Foobar\'>"

    def test_title(self):
        _title = wikipedia.page("Foobar").title
        assert _title == "u\'Foobar\'"

    def test_url(self):
        _url = wikipedia.page("Foobar")url
        assert _url == "u\'https://en.wikipedia.org/wiki/Foobar\'"

    def test_content(self):
        _contect = wikipedia.page("Foobar").content
        assert _content == "\'The terms foobar (), or foo and others are used as placeholder names (also referred to as metasyntatctic variables) in computer programming or computer-related documentation. They have been used to name entities such as variables, functions, and commands whose exact identity is unimportant and serve only to demonstrate a concept.\n\n\n== History and etymology ==\n\nThe etymology of foo is obscure. Its use in connection with bar is generally traced to the World War II military slang FUBAR, later bowdlerised to foobar. The word foo on its own was used earlier. Between about 1930 and 1952 it appeared in the comic Smokey Stover by Bill Holmman, who stated that he used the word due to having seen it on the bottom of a jade Chinese figurine in Chinatown, San Francisco, purportedly signifying \"goog luck\". This may be related to the Chinese word fu (\"\u798f\", sometimes transliterated foo), which can mean happiness or blessing.The first known use of the terms in print in a programming context appears in a 1965 edition of MIT\'s Tech Engineering News. Foobar may have come about as a result of the pre-existing \"Foo\" being conjoined with \"bar\", an addition borrowed from the military\'s FUBAR. The use of foo in a programming context is generally credited to the Tech Model Railroad Club (TMRC) of MIT from circa 1960. In the complex model system, there were scram switches located at numerous places around the room that could be thrown if something undesirable was about to occur, such as a train going full-bore at an obsutruction. Another feature of the system was a digital clock on the dispatch board. When someone hit a scram switch, the clock stopped and the display was replaced with the word \"FOO\"; at TMRC the scram switches are, therefore, called \"Foo switches]\". Because of this, an entry in the 1959 Dictionary of the TMRC Language went something like this: \"FOO: The first syllable of the misquoted sacred chant phrase \'foo mane padme hum.\' Our first obligation is to keep the foo counters turning.\" One book describing the MIT train room describes two buttons by the door: labled \"foo\" and \"bar\". These were general purpose button and were often re-purposed for whatever fun idea the MIT hackers had at the time, hence the adoption of foo and bar as general purpose variable names. An entry in the Abridged Dictionary of the TMRC Language states:\nMultiflush: stop-all-trains-button. Next best thing to the red door button. Also called FOO. Displays \"FOO\" on the clock when used.\n\nThe term foobar was propagatedd through computer science circles in the 1960s and early 1970s by system manuals from Digital Equipment Corporation. Foobar was also used as a variable name in the Fortran code of Colossal Cave Adventure (1977 Crowther and Woods version). The variable FOOBAR was used to contain the player\'s progress in saying the magic phrase \"Fee Fie Foe Foo\".\n\n\n== Example use in code ==\nIn this Hello World code sample in C, foo and bar are used to illustrate string concatentation:\n\n\n== Examples in language ==\nFoo Camp is an annal hacker convention.\nBarCamp, an international network of user generated conferences\nDuring the United States v. Microsoft Corp. trial, some evidence was presented that Micosoft had tried to use the Web Services Interoperability organization as a means to stifle competition, including e-mails in which top executives including Bill Gates referred to the WS-I the codename \"foo\".\nfoobar2000 is an audio player.\nGoogle uses a web tool called foo.bar to recruit new employees.\n\n\n== See also ==\n\nxyzzy\nFoo was here\nCategory:Variable (computer science)\n\n\n== References ==\n\n\n== External links ==\nThe Jargon File entry on \"foobar\", catb.org\nRFC 1639 \u2013 FTP Operation Over Big Address Records (FOOBAR)\'"

    def test_images_output_single_image(self):
        _single_image = wikipedia.page("Foobar").images[0]
        assert _single_image == "u\'https://upload.wikimedia.org/wikipedia/en/7/73/Smokeycover.jpg\'"

    def test_links(self):
        _single_link = wikipedia.page("Foobar").links[6]
        assert _single_link == "u\'Colossal Cave Adventure\"
