---
entity_id: "reaction.R00363"
entity_type: "reaction"
name: "oxaloacetate keto-enol-isomerase"
source_database: "KEGG"
source_id: "R00363"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00363"
---

# oxaloacetate keto-enol-isomerase

`reaction.R00363`

## Static

- Type: `reaction`
- Source: `KEGG:R00363`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Oxaloacetate 2-Hydroxyethylenedicarboxylate

## Biological Role

Catalyzed by ycgM (protein.P76004). Substrates: Oxaloacetate (molecule.C00036). Products: 2-Hydroxyethylenedicarboxylate (molecule.C03981).

## Annotation

Oxaloacetate <=> 2-Hydroxyethylenedicarboxylate

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P76004|protein.P76004]] `KEGG` `database` - via EC:5.3.2.2
- `is_product_of` <-- [[molecule.C03981|molecule.C03981]] `KEGG` `database` - C00036 <=> C03981
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `KEGG` `database` - C00036 <=> C03981

## External IDs

- `KEGG:R00363`

## Notes

EQUATION: C00036 <=> C03981
