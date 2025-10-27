# Simulated DB utility (deliberately inefficient)
def fake_query(table, filters=None):
    result = []
    for record in table:
        match = True
        if filters:
            for k, v in filters.items():
                if getattr(record, k) != v:
                    match = False
        if match:
            result.append(record)
    return result
