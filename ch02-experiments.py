# Python for Data Analysis: Ch 02
# 4.12.2016
# @totallygloria

import json
from collections import defaultdict
from collections import Counter

path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'rb')]


def find_locations(records):
    by_location = {}

    for place in records:
        if 'tz' in place:
            loc = place['tz'][0:4]
        if loc not in by_location:
            by_location[loc] = [place['tz']]
        try:
            by_location[loc].append(place['tz'])
        except:
            pass

    return by_location

#print find_locations(records)

def timezones(records):

    time_zones = [rec['tz'] for rec in records if 'tz' in rec]

    return time_zones


def count_zones():

    zones = timezones(records)
    counts = {}
    for x in zones:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts


def get_counts():
    zones = timezones(records)
    counts = defaultdict(int)  # initalizes to zero

    for x in zones:
        counts[x] += 1
    return counts


def count_cy(records):

    counts = defaultdict(int)
    cys = [rec['cy'] for rec in records if 'cy' in rec]

    for entry in cys:
        counts[entry] += 1

    return counts

def top_ten(n=10):
    zones = get_counts()
    vk_pairs = [(count, tz) for tz, count in zones.items()]
    vk_pairs.sort()
    return vk_pairs[-n:]

def counter_ten():
    zones = get_counts()
    counts = Counter(zones)
    print counts.most_common(10)

counter_ten()