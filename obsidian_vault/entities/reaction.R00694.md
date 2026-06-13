---
entity_id: "reaction.R00694"
entity_type: "reaction"
name: "L-phenylalanine:2-oxoglutarate aminotransferase"
source_database: "KEGG"
source_id: "R00694"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00694"
---

# L-phenylalanine:2-oxoglutarate aminotransferase

`reaction.R00694`

## Static

- Type: `reaction`
- Source: `KEGG:R00694`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

L-Phenylalanine + 2-Oxoglutarate Phenylpyruvate + L-Glutamate

## Biological Role

Catalyzed by aspC (protein.P00509), tyrB (protein.P04693), hisC (protein.P06986). Substrates: 2-Oxoglutarate (molecule.C00026), L-Phenylalanine (molecule.C00079). Products: L-Glutamate (molecule.C00025), Phenylpyruvate (molecule.C00166).

## Annotation

L-Phenylalanine + 2-Oxoglutarate <=> Phenylpyruvate + L-Glutamate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00509|protein.P00509]] `KEGG` `database` - via EC:2.6.1.1
- `catalyzes` <-- [[protein.P04693|protein.P04693]] `KEGG` `database` - via EC:2.6.1.57
- `catalyzes` <-- [[protein.P06986|protein.P06986]] `KEGG` `database` - via EC:2.6.1.9
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_product_of` <-- [[molecule.C00166|molecule.C00166]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_substrate_of` <-- [[molecule.C00026|molecule.C00026]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_substrate_of` <-- [[molecule.C00079|molecule.C00079]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025

## External IDs

- `KEGG:R00694`

## Notes

EQUATION: C00079 + C00026 <=> C00166 + C00025
