import json, timeit
from translator import AASQueryTranslator

# 1) load your example AAS‐JSON
example = json.load(open(
    "aas_mapping/examples/queries/01/01_contains_string.json", encoding="utf-8"
))
translator = AASQueryTranslator(example)

# 2) get 5 measurements of 1 000 loops each
times = timeit.repeat(
    stmt="translator.translate()",
    setup="",
    globals=globals(),
    repeat=5,
    number=1000
)

# times is a list of 5 floats, each = total seconds for 1 000 runs
# Compute average seconds per loop:
avg_sec_per_loop = (sum(times) / len(times)) / 1000

# Convert to microseconds:
avg_usec_per_loop = avg_sec_per_loop * 1_000_000

print(f"Average over 5 runs of 1000 loops: {avg_usec_per_loop:.2f} µs per translation")
