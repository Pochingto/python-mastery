from collections import Counter

import readrides

def count_bus_route(rows): 
    route_set = {row['route'] for row in rows}
    return len(route_set)

def total_people_ride(rows): 
    people_count = Counter()
    for row in rows: 
        people_count[row['date'], row['route']] += row['rides']
    return people_count

def total_route_ride(rows): 
    rides_counter = Counter()
    for row in rows:
        rides_counter[row['route']] += row['rides']
    return rides_counter

def total_rides_route_year(rows, year): 
    route_year_counter = Counter()
    for row in rows: 
        date_year = row['date'].split("/")[-1]
        if date_year == year: 
            route_year_counter[row['route']] += row['rides']
    return route_year_counter

if __name__ == "__main__": 
    rows = readrides.read_rides_as_dict('Data/ctabus.csv')

    print(f"Total no. of rows: {len(rows)}")
    print(f"Sampling first 5 records.")
    print(rows[:5])
    people_count = total_people_ride(rows)
    print(f"No. of people rode the number 22 bus on February 2, 2011: {people_count['02/02/2011', '22']}")

    print("Top five bus for the greatest ten-year increase: ")
    rides_2001 = total_rides_route_year(rows, "2001")
    rides_2011 = total_rides_route_year(rows, "2011")
    diff = rides_2011 - rides_2001
    print(diff.most_common(5))

    