import collections
import csv


def read_csv_as_dicts(filename, coltypes):
    portfolio = []
    f = open(filename)
    rows = csv.reader(f)
    headings = next(rows)
    for row in rows:
        portfolio.append(
            {name: func(val) for name, func, val in zip(headings, coltypes, row)}
        )
    return portfolio


class DataCollecion(collections.abc.Sequence):
    def __init__(self, headings, coltypes=None):
        self.headings = headings
        if self.headings is None or len(self.headings) == 0:
            raise ValueError("Empty heading, cannot initialize DataCollection.")

        self.columns = {heading: [] for heading in headings}
        self.coltypes = coltypes[:]
        if self.coltypes is None:
            self.coltypes = [str] * len(headings)

    def __len__(self):
        return len(self.columns[self.headings[0]])

    def __getitem__(self, index):
        return {heading: self.columns[heading][index] for heading in self.headings}

    def append(self, record):
        for heading, func in zip(self.headings, self.coltypes):
            self.columns[heading].append(func(record[heading]))


def read_csv_as_columns(filename, types):
    f = open(filename)
    rows = csv.reader(f)
    headings = next(rows)

    data_collection = DataCollecion(headings, types)
    for row in rows:
        record = {heading: val for heading, val in zip(headings, row)}
        data_collection.append(record)

    return data_collection
