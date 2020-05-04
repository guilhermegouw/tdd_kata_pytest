'''
Create a function that returns each word backwords, but NOT reverse the order of the words
Examples

backwords('Hello World') ➞ 'olleH dlroW'
backwords('Reverse the Sentence') ➞ 'esreveR eht ecnetneS'
backwords('PalindromemordnilaP') ➞ 'PalindromemordnilaP'
'''


def backwords(str):
    return ' '.join(i[::-1] for i in str.split(' '))


def test_backwords_one_word_1():
    return_value = backwords('hello')
    assert return_value == 'olleh'


def test_backwords_one_word_2():
    return_value = backwords('world')
    assert return_value == 'dlrow'


def test_backwords_one_word_3():
    return_value = backwords('gui')
    assert return_value == 'iug'


def test_backwords_two_words_1():
    return_value = backwords('Hello World')
    assert return_value == 'olleH dlroW'


def test_backwords_two_words_2():
    return_value = backwords('World Hello')
    assert return_value == 'dlroW olleH'


def test_backwords_two_words_3():
    return_value = backwords('Gui Luciana')
    assert return_value == 'iuG anaicuL'


def test_edabit_output_1():
    return_value = backwords('Hello World')
    assert return_value == 'olleH dlroW'


def test_edabit_output_2():
    return_value = backwords('Reverse the Sentence')
    assert return_value == 'esreveR eht ecnetneS'


def test_edabit_output_3():
    return_value = backwords('PalindromemordnilaP')
    assert return_value == 'PalindromemordnilaP'
