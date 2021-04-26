# Bootstrap limits.
import os.path as op

import numpy as np  # The array library.
import pandas as pd
# Safe settings for Pandas.
pd.set_option('mode.chained_assignment', 'raise')

HERE = op.dirname(__file__)
sample_2019 = pd.read_csv(op.join(HERE, '..', 'havana_math_2019_sample.csv'))
sample_marks = np.array(sample_2019['mark'])

n_sample = len(sample_marks)
n_reps = 1000
n_replications = 10000
boot_means = np.zeros((n_reps, n_replications))
for r in range(n_reps):
    for i in range(n_replications):
        boot_sample = np.random.choice(sample_marks, n_sample)
        boot_means[r, i] = np.mean(boot_sample)

means = np.mean(boot_means, axis=1)
stds = np.std(boot_means, axis=1)
lefts, rights = np.percentile(boot_means, [10, 90], axis=1)

means_diff = means - np.mean(sample_marks)
print('Means diff', np.min(means_diff), np.max(means_diff))
print('stds', np.min(stds), np.max(stds))
print('Lefts', np.min(lefts), np.max(lefts))
print('Rights', np.min(rights), np.max(rights))
