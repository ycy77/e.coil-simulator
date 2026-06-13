---
entity_id: "reaction.R03409"
entity_type: "reaction"
name: "guanosine 3'-diphosphate 5'-triphosphate 5'-phosphohydrolase"
source_database: "KEGG"
source_id: "R03409"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03409"
---

# guanosine 3'-diphosphate 5'-triphosphate 5'-phosphohydrolase

`reaction.R03409`

## Static

- Type: `reaction`
- Source: `KEGG:R03409`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Guanosine 3'-diphosphate 5'-triphosphate + H2O Guanosine 3',5'-bis(diphosphate) + Orthophosphate

## Biological Role

Catalyzed by ppx (protein.P0AFL6), gppA (protein.P25552). Substrates: H2O (molecule.C00001), Guanosine 3'-diphosphate 5'-triphosphate (molecule.C04494). Products: Orthophosphate (molecule.C00009), Guanosine 3',5'-bis(diphosphate) (molecule.C01228).

## Annotation

Guanosine 3'-diphosphate 5'-triphosphate + H2O <=> Guanosine 3',5'-bis(diphosphate) + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AFL6|protein.P0AFL6]] `KEGG` `database` - via EC:3.6.1.11
- `catalyzes` <-- [[protein.P25552|protein.P25552]] `KEGG` `database` - via EC:3.6.1.11
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009
- `is_product_of` <-- [[molecule.C01228|molecule.C01228]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009
- `is_substrate_of` <-- [[molecule.C04494|molecule.C04494]] `KEGG` `database` - C04494 + C00001 <=> C01228 + C00009

## External IDs

- `KEGG:R03409`

## Notes

EQUATION: C04494 + C00001 <=> C01228 + C00009
