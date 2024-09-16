import math
import pandas as pd
from functools import lru_cache

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
