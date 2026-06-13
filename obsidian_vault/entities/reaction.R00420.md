---
entity_id: "reaction.R00420"
entity_type: "reaction"
name: "UDP-N-acetyl-D-glucosamine 2-epimerase"
source_database: "KEGG"
source_id: "R00420"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00420"
---

# UDP-N-acetyl-D-glucosamine 2-epimerase

`reaction.R00420`

## Static

- Type: `reaction`
- Source: `KEGG:R00420`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetyl-alpha-D-glucosamine UDP-N-acetyl-D-mannosamine

## Biological Role

Catalyzed by wecB (protein.P27828). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043). Products: UDP-N-acetyl-D-mannosamine (molecule.C01170).

## Annotation

UDP-N-acetyl-alpha-D-glucosamine <=> UDP-N-acetyl-D-mannosamine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P27828|protein.P27828]] `KEGG` `database` - via EC:5.1.3.14
- `is_product_of` <-- [[molecule.C01170|molecule.C01170]] `KEGG` `database` - C00043 <=> C01170
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00043 <=> C01170

## External IDs

- `KEGG:R00420`

## Notes

EQUATION: C00043 <=> C01170
