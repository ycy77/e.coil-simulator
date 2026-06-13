---
entity_id: "reaction.R01309"
entity_type: "reaction"
name: "phosphatidylcholine acylhydrolase"
source_database: "KEGG"
source_id: "R01309"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01309"
---

# phosphatidylcholine acylhydrolase

`reaction.R01309`

## Static

- Type: `reaction`
- Source: `KEGG:R01309`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Phosphatidylcholine + 2 H2O sn-Glycero-3-phosphocholine + 2 Fatty acid

## Biological Role

Catalyzed by pldB (protein.P07000), tesA (protein.P0ADA1). Substrates: H2O (molecule.C00001), Phosphatidylcholine (molecule.C00157). Products: Fatty acid (molecule.C00162), sn-Glycero-3-phosphocholine (molecule.C00670).

## Annotation

Phosphatidylcholine + 2 H2O <=> sn-Glycero-3-phosphocholine + 2 Fatty acid

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P07000|protein.P07000]] `KEGG` `database` - via EC:3.1.1.5
- `catalyzes` <-- [[protein.P0ADA1|protein.P0ADA1]] `KEGG` `database` - via EC:3.1.1.5
- `is_product_of` <-- [[molecule.C00162|molecule.C00162]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_product_of` <-- [[molecule.C00670|molecule.C00670]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162
- `is_substrate_of` <-- [[molecule.C00157|molecule.C00157]] `KEGG` `database` - C00157 + 2 C00001 <=> C00670 + 2 C00162

## External IDs

- `KEGG:R01309`

## Notes

EQUATION: C00157 + 2 C00001 <=> C00670 + 2 C00162
