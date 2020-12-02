from nose.tools import *
from ex48 import parser

# def peek(word_list):
    # if word_list:
        # word = word_list[0]
        # return word[0]
    # else:
        # return None

def test_peek():
    assert_equal(parser.peek([('verb','run')]),'verb')
    assert_equal(parser.peek([]),None)
    
# def match(word_list, expecting):
    # if word_list:
        # word = word_list.pop(0)
        
        # if word[0] == expecting:
            # return word
        # else:
            # return None
    # else:
        # return None
        
def test_match():
    assert_equal(parser.match([('verb','run')],'verb'),('verb','run'))
    


# def test_directions():
    # assert_equal(lexicon.scan("north"),[('direction','north')])
    # result = lexicon.scan("north south east")
    # assert_equal(result,[('direction','north'),('direction','south'),('direction','east')])
    
# def test_verbs():
    # assert_equal(lexicon.scan("go"),[('verb','go')])
    # result = lexicon.scan("go kill eat")
    # assert_equal(result,[('verb','go'),('verb','kill'),('verb','eat')])
    
# def test_stops():
    # assert_equal(lexicon.scan("the"),[('stop','the')])
    # result = lexicon.scan("the in of")
    # assert_equal(result,[('stop','the'),('stop','in'),('stop','of')])
    
# def test_nouns():
    # assert_equal(lexicon.scan("bear"),[('noun','bear')])
    # result = lexicon.scan("bear princess")
    # assert_equal(result,[('noun','bear'),('noun','princess')])
    
# def test_numbers():
    # assert_equal(lexicon.scan("1234"),[('number',1234)])
    # result = lexicon.scan("3 91234")
    # assert_equal(result,[('number',3),('number',91234)])

# def test_errors():
    # assert_equal(lexicon.scan("ASDFASDFASDF"),[('error','ASDFASDFASDF')])
    # result = lexicon.scan("bear IAS princess")
    # assert_equal(result,[('noun','bear'),('error','IAS'),('noun','princess')])    
