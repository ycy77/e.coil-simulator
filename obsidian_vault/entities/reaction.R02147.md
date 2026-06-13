---
entity_id: "reaction.R02147"
entity_type: "reaction"
name: "guanosine:phosphate alpha-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R02147"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02147"
---

# guanosine:phosphate alpha-D-ribosyltransferase

`reaction.R02147`

## Static

- Type: `reaction`
- Source: `KEGG:R02147`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Guanosine + Orthophosphate Guanine + alpha-D-Ribose 1-phosphate

## Biological Role

Catalyzed by deoD (protein.P0ABP8), ppnP (protein.P0C037), yfiH (protein.P33644), xapA (protein.P45563). Substrates: Orthophosphate (molecule.C00009), Guanosine (molecule.C00387). Products: Guanine (molecule.C00242), alpha-D-Ribose 1-phosphate (molecule.C00620).

## Annotation

Guanosine + Orthophosphate <=> Guanine + alpha-D-Ribose 1-phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0ABP8|protein.P0ABP8]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P0C037|protein.P0C037]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P33644|protein.P33644]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` <-- [[protein.P45563|protein.P45563]] `KEGG` `database` - via EC:2.4.2.1
- `is_product_of` <-- [[molecule.C00242|molecule.C00242]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_product_of` <-- [[molecule.C00620|molecule.C00620]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620
- `is_substrate_of` <-- [[molecule.C00387|molecule.C00387]] `KEGG` `database` - C00387 + C00009 <=> C00242 + C00620

## External IDs

- `KEGG:R02147`

## Notes

EQUATION: C00387 + C00009 <=> C00242 + C00620
