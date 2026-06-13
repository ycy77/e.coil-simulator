---
entity_id: "reaction.R04144"
entity_type: "reaction"
name: "5-phospho-D-ribosylamine:glycine ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R04144"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04144"
---

# 5-phospho-D-ribosylamine:glycine ligase (ADP-forming)

`reaction.R04144`

## Static

- Type: `reaction`
- Source: `KEGG:R04144`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + 5-Phosphoribosylamine + Glycine ADP + Orthophosphate + 5'-Phosphoribosylglycinamide

## Biological Role

Catalyzed by purD (protein.P15640). Substrates: ATP (molecule.C00002), Glycine (molecule.C00037), 5-Phosphoribosylamine (molecule.C03090). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), 5'-Phosphoribosylglycinamide (molecule.C03838).

## Annotation

ATP + 5-Phosphoribosylamine + Glycine <=> ADP + Orthophosphate + 5'-Phosphoribosylglycinamide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P15640|protein.P15640]] `KEGG` `database` - via EC:6.3.4.13
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_product_of` <-- [[molecule.C03838|molecule.C03838]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
- `is_substrate_of` <-- [[molecule.C03090|molecule.C03090]] `KEGG` `database` - C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838

## External IDs

- `KEGG:R04144`

## Notes

EQUATION: C00002 + C03090 + C00037 <=> C00008 + C00009 + C03838
