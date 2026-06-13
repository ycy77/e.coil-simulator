---
entity_id: "reaction.R00383"
entity_type: "reaction"
name: "acyl-CoA hydrolase"
source_database: "KEGG"
source_id: "R00383"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00383"
---

# acyl-CoA hydrolase

`reaction.R00383`

## Static

- Type: `reaction`
- Source: `KEGG:R00383`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acyl-CoA + H2O CoA + Carboxylate

## Biological Role

Catalyzed by tesB (protein.P0AGG2). Substrates: H2O (molecule.C00001), Acyl-CoA (molecule.C00040). Products: CoA (molecule.C00010).

## Annotation

Acyl-CoA + H2O <=> CoA + Carboxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AGG2|protein.P0AGG2]] `KEGG` `database` - via EC:3.1.2.20
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `KEGG` `database` - C00040 + C00001 <=> C00010 + C00060
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00040 + C00001 <=> C00010 + C00060
- `is_substrate_of` <-- [[molecule.C00040|molecule.C00040]] `KEGG` `database` - C00040 + C00001 <=> C00010 + C00060

## External IDs

- `KEGG:R00383`

## Notes

EQUATION: C00040 + C00001 <=> C00010 + C00060
