def remove(items, value):
	new_items = []
	found = False
	for item in items:
		if not found and item == value:
			found = True
			continue
		new_items.append(item)

	if not found:
		raise ValueError('list.remove(x): x not in list')

	return new_items