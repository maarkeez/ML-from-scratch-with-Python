import mean


def variance_of_list(value_list):
    mean_value = mean.mean_of_list(value_list)
    return sum([(x - mean_value) ** 2 for x in value_list])


def covariance_of_lists(x, y):
    mean_x = mean.mean_of_list(x)
    mean_y = mean.mean_of_list(y)

    covariance = 0.0
    for i in range(len(x)):
        covariance += (x[i] - mean_x) * (y[i] - mean_y)

    return covariance
