# AASQL → Cypher Translator

This tool converts Asset Administration Shell (AAS) queries (JSON) into Neo4j Cypher.

# Usage

1. Run the translator tests: 
    
    python translator.py

2. Execute each example separately:

    python TestAASTranslator.py 01
    python TestAASTranslator.py 02
    python TestAASTranslator.py 03
    python TestAASTranslator.py 04
    python TestAASTranslator.py 09

3. Benchmark performance

    python benchmark.py

This script uses Python's timeit to run one example 1000× and reports the average execution time.

4. Try in Neo4j

    Load the digitalnameplate example .cypher file into your Neo4j browser. (you can just copy idta_digital_nameplate_light.cypher)

    In TestAASTranslator.py, comment out the line: # unittest.main()

    At the bottom of the file, you can run manual translations. For example:

        "05_eq_country_of_origin": {
        "$condition": {
            "$eq": [
            { "$field": "$sme.CountryOfOrigin#value" },
            { "$strVal": "DE" }
            ]
        }
        }

        Then, print the generated Cypher and execute that in Neo4j to see results.

# Project Structure

.
├── translator.py            # Core translation logic
├── TestAASTranslator.py     # Unit tests and manual tests harness
├── benchmark.py             # Performance measurement script
├── README_translator.md     # This file
└── aas_mapping/examples/queries/
    ├── 01/01_contains_string.json
    ├── 01/01_contains_string.cypher
    ├── ...
    └── 09/09_query_match_eq.json
