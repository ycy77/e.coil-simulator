---
entity_id: "reaction.R00414"
entity_type: "reaction"
name: "UDP-N-acetyl-D-glucosamine 2-epimerase"
source_database: "KEGG"
source_id: "R00414"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00414"
---

# UDP-N-acetyl-D-glucosamine 2-epimerase

`reaction.R00414`

## Static

- Type: `reaction`
- Source: `KEGG:R00414`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetyl-alpha-D-glucosamine + H2O N-Acetyl-D-mannosamine + UDP

## Biological Role

Catalyzed by wecB (protein.P27828). Substrates: H2O (molecule.C00001), UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043). Products: UDP (molecule.C00015), N-Acetyl-D-mannosamine (molecule.C00645).

## Annotation

UDP-N-acetyl-alpha-D-glucosamine + H2O <=> N-Acetyl-D-mannosamine + UDP

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27828|protein.P27828]] `KEGG` `database` - via EC:5.1.3.14
- `is_product_of` <-- [[molecule.C00015|molecule.C00015]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015
- `is_product_of` <-- [[molecule.C00645|molecule.C00645]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015

## External IDs

- `KEGG:R00414`

## Notes

EQUATION: C00043 + C00001 <=> C00645 + C00015
