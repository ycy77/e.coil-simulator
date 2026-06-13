---
entity_id: "reaction.R01317"
entity_type: "reaction"
name: "phosphatidylcholine 2-acylhydrolase"
source_database: "KEGG"
source_id: "R01317"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01317"
---

# phosphatidylcholine 2-acylhydrolase

`reaction.R01317`

## Static

- Type: `reaction`
- Source: `KEGG:R01317`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphatidylcholine + H2O 1-Acyl-sn-glycero-3-phosphocholine + Arachidonate

## Biological Role

Catalyzed by pldA (protein.P0A921). Substrates: H2O (molecule.C00001), Phosphatidylcholine (molecule.C00157). Products: Arachidonate (molecule.C00219), 1-Acyl-sn-glycero-3-phosphocholine (molecule.C04230).

## Annotation

Phosphatidylcholine + H2O <=> 1-Acyl-sn-glycero-3-phosphocholine + Arachidonate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A921|protein.P0A921]] `KEGG` `database` - via EC:3.1.1.4
- `is_product_of` <-- [[molecule.C00219|molecule.C00219]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219
- `is_product_of` <-- [[molecule.C04230|molecule.C04230]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219
- `is_substrate_of` <-- [[molecule.C00157|molecule.C00157]] `KEGG` `database` - C00157 + C00001 <=> C04230 + C00219

## External IDs

- `KEGG:R01317`

## Notes

EQUATION: C00157 + C00001 <=> C04230 + C00219
