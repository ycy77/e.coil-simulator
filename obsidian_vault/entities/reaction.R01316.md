---
entity_id: "reaction.R01316"
entity_type: "reaction"
name: "phosphatidylcholine 1-acylhydrolase"
source_database: "KEGG"
source_id: "R01316"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01316"
---

# phosphatidylcholine 1-acylhydrolase

`reaction.R01316`

## Static

- Type: `reaction`
- Source: `KEGG:R01316`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphatidylcholine + H2O 2-Acyl-sn-glycero-3-phosphocholine + Fatty acid

## Biological Role

Catalyzed by pldA (protein.P0A921). Substrates: H2O (molecule.C00001), Phosphatidylcholine (molecule.C00157). Products: Fatty acid (molecule.C00162), 2-Acyl-sn-glycero-3-phosphocholine (molecule.C04233).

## Annotation

Phosphatidylcholine + H2O <=> 2-Acyl-sn-glycero-3-phosphocholine + Fatty acid

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A921|protein.P0A921]] `KEGG` `database` - via EC:3.1.1.32
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_product_of` <-- [[molecule.C04233|molecule.C04233]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162
- `is_substrate_of` <-- [[molecule.C00157|molecule.C00157]] `KEGG` `database` - C00157 + C00001 <=> C04233 + C00162

## External IDs

- `KEGG:R01316`

## Notes

EQUATION: C00157 + C00001 <=> C04233 + C00162
