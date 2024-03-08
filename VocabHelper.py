from PyDictionary import PyDictionary

# Creates PyDictionary Instance (Needed)
dictionary = PyDictionary()

# opens words.txt and reads the text file to find word definitions
with open("words.txt", 'r') as words:
    # writes to another text file called definition.txt
    # If text file not there, it will be created
    with open("definitions.txt", 'w') as definition:
        # Reads each line in words.txt
        for eachLine in words:
            # Formatting
            word = eachLine.strip()
            # Trys to get the definitions
            try:
                definitions = dictionary.meaning(word)
                output_line = f"{word}\t"

                # Check if the word is a noun
                if 'Noun' in definitions:
                    noun_definitions = definitions['Noun']
                    # Add only the first noun definition to the output line
                    output_line += f"{noun_definitions[0]}\n"

                # Check if the word has verb definitions if noun definition not found
                elif 'Verb' in definitions:
                    verb_definitions = definitions['Verb']
                    # Add only the first verb definition to the output line
                    output_line += f"{verb_definitions[0]}\n"

                # If neither noun nor verb definitions are found
                else:
                    output_line += f"Word not found\n"

                # Write the output line to the definitions
                definition.write(output_line)

            except TypeError:
                # If the word is not found
                definition.write(f"{word}\tWord not found\n")
