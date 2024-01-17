import csv

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of class
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records

import typing
class RowNamedTuple(typing.NamedTuple):
    route: str
    date: str
    daytype: str
    rides: int

def read_rides_as_namedtuples(filename):
    '''
    Read the bus ride data as a list of namedtuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowNamedTuple(route, date, daytype, rides)
            records.append(record)
    return records

class RowWithSlot:
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

def read_rides_as_classwithslot(filename):
    '''
    Read the bus ride data as a list of class with __slots__
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = RowWithSlot(route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_columns(filename): 
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename, "r", encoding="utf-8") as f: 
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows: 
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))

    return dict(routes=routes, dates=dates, daytypes=daytypes, numrides=numrides)

import collections
class RideData(collections.abc.Sequence): 
    
    def __init__(self): 
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __getitem__(self, index):
        if isinstance(index, slice): 
            sliced = RideData()
            sliced.routes = self.routes[index]
            sliced.dates = self.dates[index]
            sliced.daytypes = self.daytypes[index]
            sliced.numrides = self.numrides[index]
            return sliced
        
        return {
            'route': self.routes[index],
            'date': self.dates[index], 
            'daytype': self.daytypes[index],
            'rides': self.numrides[index]
        }
    
    def __len__(self): 
        return len(self.routes)
    
    def append(self, record): 
        self.routes.append(record['route'])
        self.dates.append(record['date'])
        self.daytypes.append(record['daytype'])
        self.numrides.append(record['rides'])

def read_rides_as_ridedata_dicts(filename):
    '''
    Read the bus ride data as a list of dictionary
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                'route': route,
                'date': date,
                'daytype': daytype,
                'rides': rides,
            }
            records.append(record)
    return records

if __name__ == '__main__':
    func = read_rides_as_classwithslot

    import tracemalloc
    tracemalloc.start()
    rows = func('Data/ctabus.csv')
    print(f'Function: {func.__name__} Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())