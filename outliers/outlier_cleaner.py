#!/usr/bin/python


def outlier_cleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    temp_data = []
    index = 0

    for prediction in predictions:
        error = (prediction - net_worths[index]) ** 2
        temp_data.append([ages[index], net_worths[index], error])
        index += 1

    print("Data with errors: ", temp_data)
    cleaned_data = sorted(temp_data, key=lambda x: x[2])
    print("Data sorted by error: ", cleaned_data)

    return_list_size = round(len(cleaned_data)*0.9)
    print("Array size: ", len(cleaned_data), " items to return: ", return_list_size)
    returned_data = cleaned_data[:return_list_size]
    print("Data to return: ", returned_data)

    return returned_data
