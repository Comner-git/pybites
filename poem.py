import textwrap

INDENTS = 4


def print_hanging_indents(poem):
    split = poem.split("\n\n")
    for x in split:
        print(
            textwrap.fill(
                textwrap.dedent(x.strip()), 
                width=50, 
                subsequent_indent=" " * INDENTS
            )
        )
    pass
