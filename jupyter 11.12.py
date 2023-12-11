def sum_of_list(values):
    sum = 0
    for val in values:
        try:
            numeric_val = float(val)
        except Exception as e:
            print(e)
        sum += numeric_val
    return sum
