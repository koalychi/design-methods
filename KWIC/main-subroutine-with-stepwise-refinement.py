# author: Maratkanova Alexandra

class Input:
    def __init__ (self):
      self.input_text = ''

    def get_input(self):
        self.input_text = input("Enter text: ")

    def process_input(self):
        return self.input_text.split()

    def get_keyword(self):
        return input("Enter keyword: ")


class CalculationUnit:
    def __init__(self, text, keyword):
        self.text = text
        self.keyword = keyword

    def search_keyword(self):
        contexts = []
    
        for i in range(len(self.text)):
            if self.text[i] == self.keyword:
                context = " ".join(self.text[max(0, i-5):i+6])
                contexts.append(context)
        
        return contexts


class Output:
    def __init__(self, contexts):
        self.contexts = contexts

    def output_results(self):
        if len(self.contexts) > 0:
            print("Found contexts:")
            for context in self.contexts:
                print(context)
        else:
            print("No contexts found.")
            return

if __name__ == "__main__":
    input_unit = Input()

    input_unit.get_input()
    text= input_unit.process_input()
    keyword = input_unit.get_keyword()

    calc_unit = CalculationUnit(text, keyword)
    contexts = calc_unit.search_keyword()

    output = Output(contexts)
    output.output_results()
