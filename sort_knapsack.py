items = [
    {"value": 70, "weight": 30},
    {"value": 60, "weight": 10},
    {"value": 100, "weight": 20},
    {"value": 120, "weight": 30}
]
def ratio(item):
    return item["value"] / item["weight"]

sorted_items = sorted(items,key=ratio,reverse=True)
print(sorted_items)