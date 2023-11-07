def read_input(search_text, results_text):
    return search_text.split(), results_text.strip().split('\n')

def extract_keywords(search_words, stop_words):
    return [word for word in search_words if word.lower() not in stop_words]

def index_context(keywords, result_lines):
    index_entries = []
    for keyword in keywords:
        for line in result_lines:
            if keyword.lower() in line.lower():
                index_entries.append((keyword, line))
    return index_entries

def alphabetize(index_entries):
    return sorted(index_entries, key=lambda x: x[0].lower())

def format_output(sorted_entries):
    return '\n'.join([f"{entry[0]}: {entry[1]}" for entry in sorted_entries])

def kwic(search_text, results_text, stop_words):
    # Pipe 1: Read input
    search_words, result_lines = read_input(search_text, results_text)
    
    # Pipe 2: Extract keywords
    keywords = extract_keywords(search_words, stop_words)
    
    # Pipe 3: Index context
    index_entries = index_context(keywords, result_lines)
    
    # Pipe 4: Alphabetize
    sorted_entries = alphabetize(index_entries)
    
    # Pipe 5: Format output
    output = format_output(sorted_entries)
    
    return output

# Example usage:
search_text = "KWIC is an acronym"
results_text = """
KWIC is an acronym for Key Word In Context, the most common format for concordance lines.
Wikipedia, The Free Encyclopedia
"""
stop_words = ["the", "is", "an", "for", "a", "of", "and", "in"]

result = kwic(search_text, results_text, stop_words)
print(result)