import click
import sys
import unicodedata
from nltk.tokenize import word_tokenize

# See https://stackoverflow.com/questions/11066400/remove-punctuation-from-unicode-formatted-strings/21635971#21635971
tbl = dict.fromkeys(i for i in range(sys.maxunicode) if unicodedata.category(chr(i)).startswith('P'))


def remove_punctuation(text):
    return text.translate(tbl)


def is_mesoword(word, first, second):
    if word.find(first) > -1:
        spine_index = word.find(first)
        if word.find(second, spine_index + 1) == -1 or second == '':
            return True, spine_index
        else:
            return False, -1
    else:
        return False, -1


def is_wingword(word, first, second, num_first):
    if word.find(second) > -1 or second == '':
        return False
    if word.find(first) > -1 and num_first < 1:
        return True
    else:
        return False


def print_mesowords(m_array):
    max_offset = 0
    margin = 4
    for m in m_array:
        if m.spine_index > max_offset:
            max_offset = m.spine_index
    for m in m_array:
        # print('{:1} {:1} {:2}'.format(m.first, m.second, m.mesostring_index), end='')
        for i in range(margin):
            print(' ', end='')
        for i in range(max_offset - m.spine_index):
            print(' ', end='')
        print(m.word)


def print_poem(l_array):
    max_offset = 0
    margin = 4
    for l in l_array:
        if len(l.left_wing) + l.mesoword.spine_index > max_offset:
            max_offset = len(l.left_wing) + l.mesoword.spine_index
    for l in l_array:
        for i in range(margin):
            print(' ', end='')
        for i in range(max_offset - (len(l.left_wing) + l.mesoword.spine_index)):
            print(' ', end='')
        print(l.assemble())


class Poemline:
    """Poemlines are constructed from Mesowords with wingwords potentially to the left and right."""
    def __init__(self, mesoword):
        self.mesoword = mesoword
        self.left_wing = ''
        self.right_wing = ''

    def prepend(self, wingword):
        self.left_wing = wingword + ' ' + self.left_wing

    def append(self, wingword):
        self.right_wing = self.right_wing + ' ' + wingword

    def assemble(self):
        line = self.mesoword.word
        if len(self.left_wing) > 0:
            line = self.left_wing + line
        if len(self.right_wing) > 0:
            line = line + self.right_wing
        return line


class Mesoword:
    """Mesowords are identified from supplied texts using rules."""
    def __init__(self, first, second, word, spine_index, mesostring_index, sourcetext_index):
        self.first = first
        self.second = second
        self.word = ''.join([word[:spine_index], word[spine_index].upper(), word[spine_index + 1:]])
        self.spine_index = spine_index
        self.mesostring_index = mesostring_index
        self.sourcetext_index = sourcetext_index


@click.command()
@click.option('--sourcefile', prompt='file containing source text')
@click.option('--mesostring', prompt='Mesostic spine, surrounded by quotes')
@click.option('--rule', prompt='rule, 50 or 100', default=50)
def mesosticize(sourcefile, mesostring, rule):
    """An implementation of the mesostic generation algorithm Andrew Culver developed for John Cage."""
    with open(sourcefile, 'r') as f:
        sourcetext = word_tokenize(remove_punctuation(f.read()).casefold())
    mesostring = remove_punctuation(mesostring).replace(' ','').casefold()

    k = 0
    mesowords = []
    for i, first in enumerate(mesostring):
        try:
            second = mesostring[i+1]
        except:
            second = ''
        if rule == 100:
            # Don't trust this yet!
            for j in range(k, len(sourcetext)):
                if sourcetext[j].find(first) == -1 and (sourcetext[j].find(second) == -1 or (second == '')):
                    mesowords.append(Mesoword(first, second, sourcetext[j], sourcetext[j].find(first), i, j))
                    k = j + 1
                    break
        else:  # Force 50% rule:
            for j in range(k, len(sourcetext)):
                accept, spine_index = is_mesoword(sourcetext[j], first, second)
                if accept:
                    mesowords.append(Mesoword(first, second, sourcetext[j], spine_index, i, j))
                    k = j + 1
                    break

    # print('Mesostring chars: {} Mesowords: {}\n'.format(len(mesostring), len(mesowords)))
    # print_mesowords(mesowords)

    lines = [''] * len(mesowords)
    for i in range(len(mesowords)-1, -1, -1):
        line = Poemline(mesowords[i])
        # Find wing words to the left.
        num_first = 0
        for j in range(mesowords[i].sourcetext_index-1, mesowords[i-1].sourcetext_index, -1):
            if is_wingword(sourcetext[j], mesowords[i-1].first, mesowords[i-1].second, num_first):
                line.prepend(sourcetext[j])
            else:
                break
        # Find wing words to the right.
        num_first = 0
        if i != len(mesowords)-1:
            for j in range(mesowords[i].sourcetext_index+1, mesowords[i+1].sourcetext_index, 1):
                if is_wingword(sourcetext[j], mesowords[i].first, mesowords[i].second, num_first):
                    line.append(sourcetext[j])
                else:
                    break
        lines[i] = line

    print_poem(lines)

if __name__ == '__main__':
  mesosticize()
