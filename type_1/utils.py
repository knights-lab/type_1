from typing import TextIO, Iterator, Tuple


def read_fasta(fh: TextIO) -> Iterator[Tuple[str, str]]:
    title = ''
    data = ''
    for line in fh:
        if line[0] == ">":
            if title:
                # split fasta header at first whitespace
                yield title.strip().split()[0], data
            title = line[1:]
            data = ''
        else:
            data += line.strip()
    if title:
        # split fasta header at first whitespace
        yield title.strip().split()[0], data
