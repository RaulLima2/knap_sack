import math
import pandas as pd

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
            new_item:pd.DataFrame = pd.DataFrame({
                'value': item_weight,
                'weight': item.value
            })
            set_solution = pd.concat([set_solution, new_item], ignore_index=True)
            weight_knap_sack -= item_weight
            insert_items = item.weight
    return set_solution.weight.sum()