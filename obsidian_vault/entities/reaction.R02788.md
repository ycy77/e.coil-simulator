---
entity_id: "reaction.R02788"
entity_type: "reaction"
name: "UDP-N-acetylmuramoyl-L-alanyl-D-glutamate:(L)-meso-2,6-diaminoheptanedioate gamma-ligase (ADP-forming);"
source_database: "KEGG"
source_id: "R02788"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02788"
---

# UDP-N-acetylmuramoyl-L-alanyl-D-glutamate:(L)-meso-2,6-diaminoheptanedioate gamma-ligase (ADP-forming);

`reaction.R02788`

## Static

- Type: `reaction`
- Source: `KEGG:R02788`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + UDP-N-acetylmuramoyl-L-alanyl-D-glutamate + meso-2,6-Diaminoheptanedioate ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate

## Biological Role

Catalyzed by murE (protein.P22188). Substrates: ATP (molecule.C00002), meso-2,6-Diaminoheptanedioate (molecule.C00680), UDP-N-acetylmuramoyl-L-alanyl-D-glutamate (molecule.C00692). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate (molecule.C04877).

## Annotation

ATP + UDP-N-acetylmuramoyl-L-alanyl-D-glutamate + meso-2,6-Diaminoheptanedioate <=> ADP + Orthophosphate + UDP-N-acetylmuramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimelate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P22188|protein.P22188]] `KEGG` `database` - via EC:6.3.2.13
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_product_of` <-- [[molecule.C04877|molecule.C04877]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_substrate_of` <-- [[molecule.C00680|molecule.C00680]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
- `is_substrate_of` <-- [[molecule.C00692|molecule.C00692]] `KEGG` `database` - C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877

## External IDs

- `KEGG:R02788`

## Notes

EQUATION: C00002 + C00692 + C00680 <=> C00008 + C00009 + C04877
