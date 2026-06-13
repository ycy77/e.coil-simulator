---
entity_id: "reaction.R00734"
entity_type: "reaction"
name: "L-tyrosine:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R00734"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00734"
---

# L-tyrosine:2-oxoglutarate aminotransferase

`reaction.R00734`

## Static

- Type: `reaction`
- Source: `KEGG:R00734`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Tyrosine + 2-Oxoglutarate 3-(4-Hydroxyphenyl)pyruvate + L-Glutamate

## Biological Role

Catalyzed by aspC (protein.P00509), tyrB (protein.P04693), hisC (protein.P06986). Substrates: 2-Oxoglutarate (molecule.C00026), L-Tyrosine (molecule.C00082). Products: L-Glutamate (molecule.C00025), 3-(4-Hydroxyphenyl)pyruvate (molecule.C01179).

## Annotation

L-Tyrosine + 2-Oxoglutarate <=> 3-(4-Hydroxyphenyl)pyruvate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00509|protein.P00509]] `KEGG` `database` - via EC:2.6.1.1
- `catalyzes` <-- [[protein.P04693|protein.P04693]] `KEGG` `database` - via EC:2.6.1.57
- `catalyzes` <-- [[protein.P06986|protein.P06986]] `KEGG` `database` - via EC:2.6.1.9
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_product_of` <-- [[molecule.C01179|molecule.C01179]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025
- `is_substrate_of` <-- [[molecule.C00082|molecule.C00082]] `KEGG` `database` - C00082 + C00026 <=> C01179 + C00025

## External IDs

- `KEGG:R00734`

## Notes

EQUATION: C00082 + C00026 <=> C01179 + C00025
