# author: Kuznetsov Mikhail

context_shift = 3

class Text:
    def __init__(self, str_text):
        self.value = list(map(lambda x: Word(x), str_text.split()))

class Word:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value

class WordContext:
    def __init__(self, word, l_context, r_context):
        self.word = word
        self.l_context = l_context
        self.r_context = r_context
    def getWordInContext(self):
        l_context = " ".join(list(map(lambda x: x.value, self.l_context)))
        r_context = " ".join(list(map(lambda x: x.value, self.r_context)))
        return f"{l_context} __{self.word.value}__ {r_context}"

class KWICManager:
    def setUp(self, text, keywords):
        self.text = Text(text.lower())
        self.keywords = list(map(lambda x: Word(x.lower()), keywords))

    def process(self):
        words_in_context = []
        for i, word in enumerate(self.text.value):
            if word in self.keywords:
                l_context = self.text.value[max(i - context_shift, 0):i]
                r_context = self.text.value[i + 1:i + 1 + context_shift]

                words_in_context.append(WordContext(word, l_context, r_context))
        return words_in_context

class WICDisplayManager:

    def display(self, wic):
        sorted_wic = sorted(wic, key=lambda x: x.word.value)
        for wordContext in sorted_wic:
            print(wordContext.getWordInContext())

if __name__ == "__main__":

    kwic_manager = KWICManager()
    displayManager = WICDisplayManager()

    text = "KWIC is an acronym for Key Word In Context, the most common format for concordance lines"
    keywords = ["format", "acronym", "common", "KWIC"]

    kwic_manager.setUp(text, keywords)

    wic = kwic_manager.process()
    displayManager.display(wic)
