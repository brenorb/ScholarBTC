def find_range(utxos, x):
	smallest = 21000000
	result = []

	for t in reversed(range(len(utxos))):
		soma = 0
		j = 0
		while (soma < x) and ((t - j) > 0):
			soma = sum(utxos.amount for utxos in utxos[t-j:t+1])
			if (soma >= x and (soma - x) < smallest):
				smallest = soma - x
				result = [utxos[t].timestamp, utxos[t-j].timestamp]
			if smallest == 0: return result
			j += 1
	return result