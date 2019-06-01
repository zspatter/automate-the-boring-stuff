import re

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')


def mad_libs(source, destination):
    with open(source, 'r') as source, open(destination, 'w') as out:
        text = source.read()

        if regex.findall(text):
            for match in regex.findall(text):
                replacement = input(f'Enter a{"n" if match.startswith("A") else ""}'
                                    f' {match.lower()}: ')
                text = text.replace(match, replacement, 1)

            out.write(text)
            print('\n' + text)


if __name__ == "__main__":
    mad_libs('./sample_files/input.txt', './sample_files/output.txt')
