---
entity_id: "reaction.R00183"
entity_type: "reaction"
name: "adenosine 5'-monophosphate phosphohydrolase"
source_database: "KEGG"
source_id: "R00183"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00183"
---

# adenosine 5'-monophosphate phosphohydrolase

`reaction.R00183`

## Static

- Type: `reaction`
- Source: `KEGG:R00183`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

AMP + H2O Adenosine + Orthophosphate

## Biological Role

Catalyzed by ushA (protein.P07024), surE (protein.P0A840), nagD (protein.P0AF24). Substrates: H2O (molecule.C00001), AMP (molecule.C00020). Products: Orthophosphate (molecule.C00009), Adenosine (molecule.C00212).

## Annotation

AMP + H2O <=> Adenosine + Orthophosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P07024|protein.P07024]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` <-- [[protein.P0A840|protein.P0A840]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` <-- [[protein.P0AF24|protein.P0AF24]] `KEGG` `database` - via EC:3.1.3.5
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00020 + C00001 <=> C00212 + C00009
- `is_product_of` <-- [[molecule.C00212|molecule.C00212]] `KEGG` `database` - C00020 + C00001 <=> C00212 + C00009
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00020 + C00001 <=> C00212 + C00009
- `is_substrate_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00020 + C00001 <=> C00212 + C00009

## External IDs

- `KEGG:R00183`

## Notes

EQUATION: C00020 + C00001 <=> C00212 + C00009
