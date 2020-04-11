"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions["ambo"] = "a raised desk from which the Gospels or Epistles were read or chanted"

word_definitions["rachigraph"] = "a graph for recording the curves of the vertebrae"

word_definitions["prate"] = " to talk excessively and pointlessly"
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions["ambo"])

print(word_definitions["prate"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word,definition) in word_definitions.items():
    print(f"The definition of {word} is {definition}")