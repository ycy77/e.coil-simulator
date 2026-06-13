---
entity_id: "reaction.R03193"
entity_type: "reaction"
name: "UDP-N-acetylmuramate:L-alanine ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R03193"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03193"
---

# UDP-N-acetylmuramate:L-alanine ligase (ADP-forming)

`reaction.R03193`

## Static

- Type: `reaction`
- Source: `KEGG:R03193`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UDP-N-acetylmuramate + L-Alanine ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanine

## Biological Role

Catalyzed by murC (protein.P17952). Substrates: ATP (molecule.C00002), L-Alanine (molecule.C00041), UDP-N-acetylmuramate (molecule.C01050). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), UDP-N-acetylmuramoyl-L-alanine (molecule.C01212).

## Annotation

ATP + UDP-N-acetylmuramate + L-Alanine <=> ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanine

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P17952|protein.P17952]] `KEGG` `database` - via EC:6.3.2.8
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_product_of` <-- [[molecule.C01212|molecule.C01212]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_substrate_of` <-- [[molecule.C00041|molecule.C00041]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212

## External IDs

- `KEGG:R03193`

## Notes

EQUATION: C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
