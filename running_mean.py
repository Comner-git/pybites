import statistics


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    mean = []
    for n in range(len(sequence)):
        mean.append(round(statistics.mean(sequence[:n+1]),2))
    return mean
    pass
