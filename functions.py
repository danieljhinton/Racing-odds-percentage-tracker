def remove_every_second_list_element(input_list: list) -> list:
    '''Takes in a list and returns the list with every second element removed'''
    output_list = []

    for i, el in enumerate(input_list):
        if i % 2 == 0:
            output_list.append(el)
    
    return output_list


def percentage_calculator(odds_list: list[float]) -> float:
    '''
    Takes in a list of decimal betting odds and returns the total percentage.
    '''
    percentage_total = 0

    for price in odds_list:
        percentage_total += 100 / price

    return percentage_total