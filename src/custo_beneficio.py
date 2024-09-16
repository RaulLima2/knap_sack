import math
import pandas as pd

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
            new_item:pd.DataFrame = pd.DataFrame({
                'value': item.value,
                'weight': item.weight
            })
            set_solution = pd.concat([set_solution, new_item], ignore_index=True)
            weight_knap_sack -= item_weight
            maximu_benefit_by_cust -= benefit_by_cust_after
            benefit_by_cust_after = item_benefit_by_cust
            weight_after = item.weight
    return set_solution.weight.sum()