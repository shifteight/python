from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts

path = 'data/usagov_bitly_data2012-03-16-1331923249.txt'
import json
records = [json.loads(line) for line in open(path)]
time_zones = [rec['tz'] for rec in records if 'tz' in rec]

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

# using Counter class
from collections import Counter
counts2 = Counter(time_zones)
print(counts2.most_common(10))

# using Pandas
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
print(tz_counts[:10])

# replace missing and unknown values
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts2 = clean_tz.value_counts()
print(tz_counts2[:10])

# make a horizontal bar plot
tz_counts2[:10].plot(kind='barh', rot=0)
# matplotlib.pyplot.show()

results = Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5])
print(results.value_counts()[:8])

# decompose the top time zones into Windows and non-Windows users
import numpy as np

# exclude missing agents
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),
                            'Windows', 'Not Windows')
print(operating_system[:5])

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10])

# use to sort in ascending order
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])

# select the rows in that order, then slice off the last 10 rows
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)

# make a stacked bar plot
count_subset.plot(kind='barh', stacked=True)

# normalize the rows
normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)
