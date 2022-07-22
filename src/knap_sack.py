import math
import pandas as pd
from functools import lru_cache

def by_minimu_weights(weight_knap_sack: int, knap_sack: pd.DataFrame) -> int:
    item_weight: int = 0
    insert_items: int = 0
    set_solution: pd.DataFrame = pd.DataFrame({
        'value': [],
        'weight': []
    })
    for _, item in knap_sack.iterrows():
        item_weight = item.weight
        if item_weight <= weight_knap_sack - insert_items:
            insert_items += item_weight
            set_solution = set_solution.append({
                'value': item_weight,
                'weight': item.value
            }, ignore_index=True)
            weight_knap_sack -= item_weight
            insert_items = item.weight
    return set_solution.weight.sum()

def by_greedy_benefit_cust(weight_knap_sack: int, benefit_knap_sack: int, knap_sack: pd.DataFrame) -> int:
    item_weight: int = 0
    weight_after: int = 0
    benefit_by_cust_after: int = 0
    maximu_benefit_by_cust: int = 0
    set_solution: pd.DataFrame = pd.DataFrame({
        'value': [],
        'weight': []
    })
    maximu_benefit_by_cust = math.trunc(
        weight_knap_sack//benefit_knap_sack
    )
    for _, item in knap_sack.iterrows():
        item_benefit_by_cust = item.benefit_by_cust
        if item_benefit_by_cust <= maximu_benefit_by_cust - benefit_by_cust_after \
                and weight_knap_sack - weight_after >= item.weight:
            set_solution = set_solution.append({
                'value': item.value,
                'weight': item.weight
            }, ignore_index=True)
            weight_knap_sack -= item_weight
            maximu_benefit_by_cust -= benefit_by_cust_after
            benefit_by_cust_after = item_benefit_by_cust
            weight_after = item.weight
    return set_solution.weight.sum()

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

@lru_cache(maxsize=None)
def by_benefit_cust_with_lru(index: int, weight_knap_sack:int, values: tuple, weights:tuple) -> int:
    if index == 0:
        return 0
    if weight_knap_sack == 0:
        return 0
    if weights[index - 1] > weight_knap_sack:
        return by_benefit_cust_with_lru(
            index - 1,
            weight_knap_sack,
            values,
            weights
        )
    return max(
        by_benefit_cust_with_lru(
            index - 1,
            weight_knap_sack,
            values,
            weights
        ),
        values[index - 1] +
        by_benefit_cust_with_lru(
            index - 1,
            weight_knap_sack - weights[index - 1],
            values,
            weights
        )
    )

@lru_cache(maxsize=None)
def by_benefit_cust_ssp(b: int, index: int, weight_knap_sack:int, weight:tuple) -> int:
    if index == 0:
        return 1
    if weight_knap_sack == 0:
        return 0
    b = by_benefit_cust_ssp(b, index - 1, weight_knap_sack, weight)
    if b == 0 and weight[index] <= weight_knap_sack:
        b = by_benefit_cust_ssp(b, index - 1, weight_knap_sack - weight[index], weight)
    return b
