---
entity_id: "reaction.R04733"
entity_type: "reaction"
name: "UTP:[protein-PII] uridylyltransferase"
source_database: "KEGG"
source_id: "R04733"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04733"
---

# UTP:[protein-PII] uridylyltransferase

`reaction.R04733`

## Static

- Type: `reaction`
- Source: `KEGG:R04733`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UTP + [Protein-PII] Diphosphate + Uridylyl-[protein-PII]

## Biological Role

Catalyzed by glnD (protein.P27249). Substrates: UTP (molecule.C00075). Products: Diphosphate (molecule.C00013).

## Annotation

UTP + [Protein-PII] <=> Diphosphate + Uridylyl-[protein-PII]

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27249|protein.P27249]] `KEGG` `database` - via EC:2.7.7.59
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00075 + C05250 <=> C00013 + C05326
- `is_substrate_of` <-- [[molecule.C00075|molecule.C00075]] `KEGG` `database` - C00075 + C05250 <=> C00013 + C05326

## External IDs

- `KEGG:R04733`

## Notes

EQUATION: C00075 + C05250 <=> C00013 + C05326
