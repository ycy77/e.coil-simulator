---
entity_id: "reaction.R00418"
entity_type: "reaction"
name: "UDP-N-acetyl-D-glucosamine 4-epimerase"
source_database: "KEGG"
source_id: "R00418"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00418"
---

# UDP-N-acetyl-D-glucosamine 4-epimerase

`reaction.R00418`

## Static

- Type: `reaction`
- Source: `KEGG:R00418`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetyl-alpha-D-glucosamine UDP-N-acetyl-D-galactosamine

## Biological Role

Catalyzed by galE (protein.P09147). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043). Products: UDP-N-acetyl-D-galactosamine (molecule.C00203).

## Annotation

UDP-N-acetyl-alpha-D-glucosamine <=> UDP-N-acetyl-D-galactosamine

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P09147|protein.P09147]] `KEGG` `database` - via EC:5.1.3.2
- `is_product_of` <-- [[molecule.C00203|molecule.C00203]] `KEGG` `database` - C00043 <=> C00203
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00043 <=> C00203

## External IDs

- `KEGG:R00418`

## Notes

EQUATION: C00043 <=> C00203
