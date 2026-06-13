---
entity_id: "reaction.R03423"
entity_type: "reaction"
name: "nucleoside-2',3'-cyclic-phosphate 3'-nucleotidohydrolase"
source_database: "KEGG"
source_id: "R03423"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03423"
---

# nucleoside-2',3'-cyclic-phosphate 3'-nucleotidohydrolase

`reaction.R03423`

## Static

- Type: `reaction`
- Source: `KEGG:R03423`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2',3'-Cyclic nucleotide + H2O Nucleoside 3'-phosphate

## Biological Role

Catalyzed by cpdB (protein.P08331). Substrates: H2O (molecule.C00001).

## Annotation

2',3'-Cyclic nucleotide + H2O <=> Nucleoside 3'-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P08331|protein.P08331]] `KEGG` `database` - via EC:3.1.4.16
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01240 + C00001 <=> C03419

## External IDs

- `KEGG:R03423`

## Notes

EQUATION: C01240 + C00001 <=> C03419
