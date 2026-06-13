---
entity_id: "reaction.R12075"
entity_type: "reaction"
name: "UDP-N-acetyl-alpha-D-glucosamine:trans,octacis-decaprenyl-phosphate N-acetylglucosaminephosphotransferase"
source_database: "KEGG"
source_id: "R12075"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12075"
---

# UDP-N-acetyl-alpha-D-glucosamine:trans,octacis-decaprenyl-phosphate N-acetylglucosaminephosphotransferase

`reaction.R12075`

## Static

- Type: `reaction`
- Source: `KEGG:R12075`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetyl-D-glucosamine + Decaprenol phosphate UMP + GlcNAc-pyrophosphoryldecaprenol

## Biological Role

Catalyzed by wecA (protein.P0AC78). Products: UMP (molecule.C00105).

## Annotation

UDP-N-acetyl-D-glucosamine + Decaprenol phosphate <=> UMP + GlcNAc-pyrophosphoryldecaprenol

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `catalyzes` <-- [[protein.P0AC78|protein.P0AC78]] `KEGG` `database` - via EC:2.7.8.35
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `KEGG` `database` - G10610 + C02970 <=> C00105 + G13118

## External IDs

- `KEGG:R12075`

## Notes

EQUATION: G10610 + C02970 <=> C00105 + G13118
