import re

regex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')


def mad_libs(source, destination):
    with open(source, 'r') as source, open(destination, 'w') as out:
        output = source.read()

        for match in regex.findall(output):
            replacement = input(f'Enter a{"n" if match.startswith("A") else ""}'
                                f' {match.lower()}: ')
            output = output.replace(match, replacement)

        out.write(output)
        print('\n' + output)


if __name__ == "__main__":
    mad_libs('input.txt', 'output.txt')
