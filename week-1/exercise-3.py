import random
import math


def loss_function():
    num_samples = input("Input number of samples (integer number) which are generated: ")
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return
    num_samples = int(num_samples)
    loss_name = input("Input loss name: ")
    _sum = 0
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        if loss_name == "MAE":
            diff = abs(predict - target)
        else:
            diff = (predict - target) ** 2
        _sum += diff
        print(f"loss name: {loss_name}, sample: {i}, pred: {predict} target: {target}, loss: {diff}")

    final_loss = math.sqrt(_sum / num_samples) if loss_name == "RMSE" else _sum / num_samples
    print(f"final {loss_name}: {final_loss}")
