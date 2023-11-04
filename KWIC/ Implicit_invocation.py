class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event, callback):
        if event not in self.subscribers:
            self.subscribers[event] = []
        self.subscribers[event].append(callback)

    def publish(self, event, data=None):
        if event in self.subscribers:
            for callback in self.subscribers[event]:
                callback(data)


class DocumentProcessor:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def process_document(self, document, keywords):
        words = document.split()
        for i, word in enumerate(words):
            if word in keywords:
                left_context = " ".join(words[max(i - 3, 0):i])
                right_context = " ".join(words[i + 1:i + 4])
                self.event_bus.publish("word_processed", (word, left_context, right_context))


class UI:
    def __init__(self, event_bus):
        self.event_bus = event_bus

    def display_word_with_context(self, data):
        word, left_context, right_context = data
        print(f"{left_context} << {word} >> {right_context}")


if __name__ == "__main__":
    event_bus = EventBus()
    document_processor = DocumentProcessor(event_bus)
    ui = UI(event_bus)

    event_bus.subscribe("word_processed", ui.display_word_with_context)

    document = "KWIC is an acronym for Key Word In Context, the most common format for concordance lines and the Wikipedia slogan in English, searched against a Wikipedia page, might yield a KWIC index as follows. A KWIC index usually uses a wide layout to allow the display of maximum 'in context' information"
    keywords = ["concordance", "lines", "information"]

    document_processor.process_document(document, keywords)
