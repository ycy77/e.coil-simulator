---
entity_id: "reaction.R00497"
entity_type: "reaction"
name: "gamma-L-glutamyl-L-cysteine:glycine ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R00497"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00497"
---

# gamma-L-glutamyl-L-cysteine:glycine ligase (ADP-forming)

`reaction.R00497`

## Static

- Type: `reaction`
- Source: `KEGG:R00497`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + gamma-L-Glutamyl-L-cysteine + Glycine ADP + Orthophosphate + Glutathione

## Biological Role

Catalyzed by gshB (protein.P04425). Substrates: ATP (molecule.C00002), Glycine (molecule.C00037), gamma-L-Glutamyl-L-cysteine (molecule.C00669). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Glutathione (molecule.C00051).

## Annotation

ATP + gamma-L-Glutamyl-L-cysteine + Glycine <=> ADP + Orthophosphate + Glutathione

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P04425|protein.P04425]] `KEGG` `database` - via EC:6.3.2.3
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_product_of` <-- [[molecule.C00051|molecule.C00051]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
- `is_substrate_of` <-- [[molecule.C00669|molecule.C00669]] `KEGG` `database` - C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051

## External IDs

- `KEGG:R00497`

## Notes

EQUATION: C00002 + C00669 + C00037 <=> C00008 + C00009 + C00051
