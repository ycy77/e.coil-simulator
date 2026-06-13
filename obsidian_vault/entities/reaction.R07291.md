---
entity_id: "reaction.R07291"
entity_type: "reaction"
name: "2-lysophosphatidylcholine acylhydrolase"
source_database: "KEGG"
source_id: "R07291"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R07291"
---

# 2-lysophosphatidylcholine acylhydrolase

`reaction.R07291`

## Static

- Type: `reaction`
- Source: `KEGG:R07291`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-Acyl-sn-glycero-3-phosphocholine + H2O sn-Glycero-3-phosphocholine + Carboxylate

## Biological Role

Catalyzed by pldB (protein.P07000), tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001), 1-Acyl-sn-glycero-3-phosphocholine (molecule.C04230). Products: sn-Glycero-3-phosphocholine (molecule.C00670).

## Annotation

1-Acyl-sn-glycero-3-phosphocholine + H2O <=> sn-Glycero-3-phosphocholine + Carboxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P07000|protein.P07000]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.1.5
- `is_product_of` <-- [[molecule.C00670|molecule.C00670]] `KEGG` `database` - C04230 + C00001 <=> C00670 + C00060
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04230 + C00001 <=> C00670 + C00060
- `is_substrate_of` <-- [[molecule.C04230|molecule.C04230]] `KEGG` `database` - C04230 + C00001 <=> C00670 + C00060

## External IDs

- `KEGG:R07291`

## Notes

EQUATION: C04230 + C00001 <=> C00670 + C00060
