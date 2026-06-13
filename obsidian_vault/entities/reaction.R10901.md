---
entity_id: "reaction.R10901"
entity_type: "reaction"
name: "UDP-N-acetylmuramate:L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase"
source_database: "KEGG"
source_id: "R10901"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R10901"
---

# UDP-N-acetylmuramate:L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase

`reaction.R10901`

## Static

- Type: `reaction`
- Source: `KEGG:R10901`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UDP-N-acetylmuramate + L-Alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate

## Biological Role

Catalyzed by mpl (protein.P37773). Substrates: ATP (molecule.C00002), UDP-N-acetylmuramate (molecule.C01050). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877).

## Annotation

ATP + UDP-N-acetylmuramate + L-Alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptanedioate <=> ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37773|protein.P37773]] `KEGG` `database` - via EC:6.3.2.45
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_product_of` <-- [[molecule.C04877|molecule.C04877]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_substrate_of` <-- [[molecule.C01050|molecule.C01050]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877

## External IDs

- `KEGG:R10901`

## Notes

EQUATION: C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
