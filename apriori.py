from itertools import combinations

def extract_frequent_itemsets(transactions, min_support_count):
    counts = {}

    for transaction in transactions:
        for item in transaction:
            item_set = frozenset([item])
            if item_set in counts:
                counts[item_set] += 1
            else:
                counts[item_set] = 1

    frequent_sets = {item for item, count in counts.items() if count >= min_support_count}

    return frequent_sets, counts


def merge_itemsets(itemsets, desired_length):
    merged_sets = []
    for set1, set2 in combinations(itemsets, 2):
        union = set1 | set2
        if len(union) == desired_length:
            merged_sets.append(union)
    return merged_sets


def filter_itemsets(candidates, transactions, min_support_count):
    counts = {candidate: 0 for candidate in candidates}

    for transaction in transactions:
        transaction_set = set(transaction)
        for candidate in candidates:
            if candidate.issubset(transaction_set):
                counts[candidate] += 1

    valid_itemsets = [itemset for itemset, count in counts.items() if count >= min_support_count]
    counts = {itemset: count for itemset, count in counts.items() if count >= min_support_count}

    return valid_itemsets, counts


def create_rules(frequent_itemsets, itemset_counts, min_confidence_ratio):
    association_rules = []
    for itemset in frequent_itemsets:
        set_length = len(itemset)
        if set_length < 2:
            continue
        for i in range(1, set_length):
            antecedent_combinations = list(combinations(itemset, i))
            for antecedent in antecedent_combinations:
                antecedent_set = frozenset(antecedent)
                consequent_set = itemset - antecedent_set
                if not consequent_set:
                    continue
                antecedent_support = itemset_counts.get(antecedent_set, 0)
                set_support = itemset_counts.get(itemset, 0)
                confidence_ratio = set_support / antecedent_support if antecedent_support > 0 else 0

                if confidence_ratio >= min_confidence_ratio:
                    association_rules.append((antecedent_set, consequent_set, set_support, confidence_ratio))

    return association_rules


def apriori_algorithm(transactions, min_support_count, min_confidence_ratio):
    transactions = list(map(set, transactions))
    frequent_itemsets, itemset_counts = extract_frequent_itemsets(transactions, min_support_count)

    all_frequent_itemsets = frequent_itemsets.copy()
    k = 2
    while frequent_itemsets:
        candidates = merge_itemsets(frequent_itemsets, k)
        pruned_candidates, _ = filter_itemsets(candidates, transactions, min_support_count)

        frequent_itemsets, itemset_counts_k = filter_itemsets(pruned_candidates, transactions, min_support_count)
        itemset_counts.update(itemset_counts_k)
        all_frequent_itemsets.update(frequent_itemsets)
        k += 1

    rules = create_rules(all_frequent_itemsets, itemset_counts, min_confidence_ratio)
    return sorted(all_frequent_itemsets, key=lambda x: (len(x), sorted(x))), rules

data = [
    ["bread", "milk"],
    ["beer", "bread", "diaper", "eggs"],
    ["beer", "coke", "diaper", "milk"],
    ["beer", "bread", "milk", "diaper"],
    ["bread", "coke", "diaper", "milk"]
]

support_threshold = 3
confidence_threshold = 0.5

frequent_itemsets_result, rules_result = apriori_algorithm(data, support_threshold, confidence_threshold)

print("Frequent Itemsets:")
for itemset in frequent_itemsets_result:
    print(set(itemset))

print("\nAssociation Rules:")
for antecedent, consequent, support, confidence in rules_result:
    print(f"{set(antecedent)} => {set(consequent)}, Support Count: {support}, Confidence: {confidence:.2f}")