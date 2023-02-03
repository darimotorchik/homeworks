def split_into_sentences(text):
    word_list = text.split()
    sentence_list = []
    left_border = 0
    right_border = 1
    for word_i in range(1, len(word_list)):
        if '/' in word_list[word_i] or '"' in word_list[word_i]:
            sentence = ' '.join(word_list[left_border:right_border + 1])
            sentence_list.append(sentence)
            left_border = right_border + 1
        right_border += 1
    return sentence_list


def decipher_cyclic_shift(sentence_list):
    shift = 2
    new_sentence_list = []
    for sentence_i in range(len(sentence_list)):
        words_list = sentence_list[sentence_i].split()
        shift += 1
        new_words_list = []
        for word in words_list:
            left_b = -(shift % len(word))
            new_word = ''.join([word[left_b:], word[:left_b]])
            new_words_list.append(new_word)
        new_words_list = ' '.join(new_words_list)
        new_sentence_list.append(new_words_list)
    return new_sentence_list


def decipher_the_caesar_cipher(new_sentence_list):
    new_text = []
    for sentence in new_sentence_list:
        new_sentence = [chr(ord(symbol) - 1) if symbol != ' ' else ' ' for symbol in sentence]
        new_sentence = ''.join(new_sentence)
        new_text.append(new_sentence)
    return new_text


user_text = """vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf 
jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft 
(ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV 
mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf 
zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou 
/ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg 
fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn 
gp tf"uip"""


user_sentence_list = split_into_sentences(user_text)
new_user_sentence_list = decipher_cyclic_shift(user_sentence_list)
new_user_text = decipher_the_caesar_cipher(new_user_sentence_list)


print(*new_user_text, sep='\n')
