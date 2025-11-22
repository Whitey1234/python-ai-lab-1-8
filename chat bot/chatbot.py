import json
import difflib

# Load database from a JSON file
with open('database.json','r') as file:
    Database = json.load(file)

print('\nWelcome To CatBot\n\n')

while True:
    question = input('Ask: ')
    max_matched = 0
    pinned_index = None

    # Split words of the user question
    question_words = set(question.lower().split())

    # Search through the database
    for index in Database['Neuron']:
        current_keyword = index['Keyword']
        keywords = set(current_keyword.lower().split())
        matching_range = 0.8
        nearly_matched_words = set()

        # Compare each user word with database keywords
        for i in question_words:
            for j in keywords:
                similarity = difflib.SequenceMatcher(None, i, j).ratio()
                if similarity >= matching_range:
                    nearly_matched_words.add(i)
                    break

        # Track best match
        current_matched = len(nearly_matched_words)
        if current_matched > max_matched:
            max_matched = current_matched
            pinned_index = index

    # Print response
    if max_matched < 1:
        print("Sorry, no answers were found.")
    else:
        print(f"Answer: {pinned_index['Value']}")
