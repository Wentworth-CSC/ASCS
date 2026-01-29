def main():
    weights, mean, min, max, total = get_weights()
    print(f"You entered {len(weights)} weights, with an average weight of {mean}")
    print(f"The weights entered have a range of {max - min} ({min} to {max})")
    print(f"The standard deviation is {std_dev(weights, mean)}")

def get_weights() -> tuple:
    """
    Function get_weights()

    Prompts for and receives up to 100 weights, returning the list, as well as
        descriptive statistics
        :return:    weights(list), mean, min, max, total
    """
    weights = []
    total_weight = 0
    max_weight = 0
    min_weight = 1_000_000_000

    while True:
        weights.append(int(input("Enter Weight (-1 to end): ")))
        if weights[-1] == -1:
            weights.pop()
            break
        total_weight += weights[-1]
        if weights[-1] > max_weight:
            max_weight = weights[-1]
        if weights[-1] < min_weight:
            min_weight = weights[-1]
        if len(weights) == 100:
            break

    mean = total_weight/len(weights)
    return weights, mean, min_weight, max_weight, total_weight
def std_dev(weights: list, mean: float) -> float:
    """
    Function std_dev()
        Calculates Standard Deviation based on the weights provided
    :param weights: list of weights
    :param mean: mean of the weights
    :return: standard deviation
    """
    sum_of_deviations_squared = 0
    for weight in weights:
        sum_of_deviations_squared += (weight-mean)**2
    return (sum_of_deviations_squared / len(weights))**0.5

