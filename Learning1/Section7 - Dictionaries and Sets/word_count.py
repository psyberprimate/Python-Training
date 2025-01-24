# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."


def word_counter(data: dict, string: str) -> None:
     for character in string.casefold():
         if character.isalnum():
             data[character] = data.setdefault(character, 0) + 1
 
word_counter(word_count, text)
#sorted(word_count)

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
  