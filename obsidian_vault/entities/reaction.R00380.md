---
entity_id: "reaction.R00380"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:DNA (cytosine-5-)-methyltransferase"
source_database: "KEGG"
source_id: "R00380"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00380"
---

# S-adenosyl-L-methionine:DNA (cytosine-5-)-methyltransferase

`reaction.R00380`

## Static

- Type: `reaction`
- Source: `KEGG:R00380`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + DNA S-Adenosyl-L-homocysteine + 5-Methylcytosine in DNA

## Biological Role

Catalyzed by dcm (protein.P0AED9). Substrates: S-Adenosyl-L-methionine (molecule.C00019), DNA (molecule.C00039). Products: S-Adenosyl-L-homocysteine (molecule.C00021).

## Annotation

S-Adenosyl-L-methionine + DNA <=> S-Adenosyl-L-homocysteine + 5-Methylcytosine in DNA

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AED9|protein.P0AED9]] `KEGG` `database` - via EC:2.1.1.37
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `KEGG` `database` - C00019 + C00039 <=> C00021 + C02967
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C00039 <=> C00021 + C02967
- `is_substrate_of` <-- [[molecule.C00039|molecule.C00039]] `KEGG` `database` - C00019 + C00039 <=> C00021 + C02967

## External IDs

- `KEGG:R00380`

## Notes

EQUATION: C00019 + C00039 <=> C00021 + C02967
