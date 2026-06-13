---
entity_id: "reaction.R06863"
entity_type: "reaction"
name: "D-sedoheptulose-7-phosphate:thiamin diphosphate glycolaldehydetransferase"
source_database: "KEGG"
source_id: "R06863"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06863"
---

# D-sedoheptulose-7-phosphate:thiamin diphosphate glycolaldehydetransferase

`reaction.R06863`

## Static

- Type: `reaction`
- Source: `KEGG:R06863`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Sedoheptulose 7-phosphate + Thiamin diphosphate alpha,beta-Dihydroxyethyl-TPP + D-Ribose 5-phosphate

## Biological Role

Catalyzed by tktA (protein.P27302), tktB (protein.P33570). Substrates: Thiamin diphosphate (molecule.C00068), Sedoheptulose 7-phosphate (molecule.C05382). Products: D-Ribose 5-phosphate (molecule.C00117).

## Annotation

Sedoheptulose 7-phosphate + Thiamin diphosphate <=> alpha,beta-Dihydroxyethyl-TPP + D-Ribose 5-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27302|protein.P27302]] `KEGG` `database` - via EC:2.2.1.1
- `catalyzes` <-- [[protein.P33570|protein.P33570]] `KEGG` `database` - via EC:2.2.1.1
- `is_product_of` <-- [[molecule.C00117|molecule.C00117]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117
- `is_substrate_of` <-- [[molecule.C00068|molecule.C00068]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117
- `is_substrate_of` <-- [[molecule.C05382|molecule.C05382]] `KEGG` `database` - C05382 + C00068 <=> C13378 + C00117

## External IDs

- `KEGG:R06863`

## Notes

EQUATION: C05382 + C00068 <=> C13378 + C00117
