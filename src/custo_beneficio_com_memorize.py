import math
import pandas as pd

def by_benefit_cust_with_table(weight_knap_sack: int, number_of_items: int, knap_sack: pd.DataFrame) -> int:
    memo: list = [
        [
            0 for j in range(weight_knap_sack + 1)
        ]
        for i in range(number_of_items+1)
    ]
    weight: int = weight_knap_sack + 1
    number_of_items: int = number_of_items + 1
    for i in range(1, number_of_items):
        for j in range(1, weight):
            if knap_sack.weight.get(i-1) <= j:
                memo[i][j] = max(
                    memo[i-1][j],
                    memo[i-1][j - knap_sack.weight.get(i-1)]
                    + knap_sack.value.get(i-1)
                )
            else:
                memo[i][j] = memo[i-1][j]
    return memo[number_of_items - 1][weight - 1]