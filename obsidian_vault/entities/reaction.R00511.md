---
entity_id: "reaction.R00511"
entity_type: "reaction"
name: "cytidine-5'-monophosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00511"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00511"
---

# cytidine-5'-monophosphate phosphohydrolase

`reaction.R00511`

## Static

- Type: `reaction`
- Source: `KEGG:R00511`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CMP + H2O Cytidine + Orthophosphate

## Biological Role

Catalyzed by ushA (protein.P07024), surE (protein.P0A840), nagD (protein.P0AF24). Substrates: H2O (molecule.C00001), CMP (molecule.C00055). Products: Orthophosphate (molecule.C00009), Cytidine (molecule.C00475).

## Annotation

CMP + H2O <=> Cytidine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07024|protein.P07024]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` <-- [[protein.P0AF24|protein.P0AF24]] `KEGG` `database` - via EC:3.1.3.5
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009
- `is_product_of` <-- [[molecule.C00475|molecule.C00475]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `KEGG` `database` - C00055 + C00001 <=> C00475 + C00009

## External IDs

- `KEGG:R00511`

## Notes

EQUATION: C00055 + C00001 <=> C00475 + C00009
