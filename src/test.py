complete = dict()
market = {
    "id": 20121
}

for i in range(10):
    query = dict()
    query["weyo"] = "masjalla"
    query["wow"] = "efsef"
    query["id"] = market["id"]
    complete[i] = query

print(complete)