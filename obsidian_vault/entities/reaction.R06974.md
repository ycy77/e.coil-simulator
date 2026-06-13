---
entity_id: "reaction.R06974"
entity_type: "reaction"
name: "formate:N1-(5-phospho-beta-D-ribosyl)glycinamide ligase (ADP-forming)"
source_database: "KEGG"
source_id: "R06974"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06974"
---

# formate:N1-(5-phospho-beta-D-ribosyl)glycinamide ligase (ADP-forming)

`reaction.R06974`

## Static

- Type: `reaction`
- Source: `KEGG:R06974`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Formate + ATP + 5'-Phosphoribosylglycinamide ADP + Orthophosphate + 5'-Phosphoribosyl-N-formylglycinamide

## Biological Role

Catalyzed by purT (protein.P33221). Substrates: ATP (molecule.C00002), Formate (molecule.C00058), 5'-Phosphoribosylglycinamide (molecule.C03838). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), 5'-Phosphoribosyl-N-formylglycinamide (molecule.C04376).

## Annotation

Formate + ATP + 5'-Phosphoribosylglycinamide <=> ADP + Orthophosphate + 5'-Phosphoribosyl-N-formylglycinamide

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P33221|protein.P33221]] `KEGG` `database` - via EC:6.3.1.21
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_product_of` <-- [[molecule.C04376|molecule.C04376]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_substrate_of` <-- [[molecule.C00058|molecule.C00058]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
- `is_substrate_of` <-- [[molecule.C03838|molecule.C03838]] `KEGG` `database` - C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376

## External IDs

- `KEGG:R06974`

## Notes

EQUATION: C00058 + C00002 + C03838 <=> C00008 + C00009 + C04376
