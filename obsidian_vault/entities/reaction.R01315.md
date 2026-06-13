---
entity_id: "reaction.R01315"
entity_type: "reaction"
name: "phosphatidylcholine 2-acylhydrolase"
source_database: "KEGG"
source_id: "R01315"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01315"
---

# phosphatidylcholine 2-acylhydrolase

`reaction.R01315`

## Static

- Type: `reaction`
- Source: `KEGG:R01315`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphatidylcholine + H2O 1-Acyl-sn-glycero-3-phosphocholine + Fatty acid

## Biological Role

Catalyzed by pldA (protein.P0A921). Substrates: H2O (molecule.C00001), Phosphatidylcholine (molecule.C00157). Products: Fatty acid (molecule.C00162), 1-Acyl-sn-glycero-3-phosphocholine (molecule.C04230).

## Annotation

Phosphatidylcholine + H2O <=> 1-Acyl-sn-glycero-3-phosphocholine + Fatty acid

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A921|protein.P0A921]] `KEGG` `database` - via EC:3.1.1.4
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_product_of` <-- [[molecule.C04230|molecule.C04230]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162
- `is_substrate_of` <-- [[molecule.C00157|molecule.C00157]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00162

## External IDs

- `KEGG:R01315`

## Notes

EQUATION: C00157 + C00001 <=> C04230 + C00162
