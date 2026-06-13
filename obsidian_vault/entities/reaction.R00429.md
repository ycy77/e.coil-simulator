---
entity_id: "reaction.R00429"
entity_type: "reaction"
name: "ATP:GTP 3'-diphosphotransferase"
source_database: "KEGG"
source_id: "R00429"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00429"
---

# ATP:GTP 3'-diphosphotransferase

`reaction.R00429`

## Static

- Type: `reaction`
- Source: `KEGG:R00429`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + GTP AMP + Guanosine 3'-diphosphate 5'-triphosphate

## Biological Role

Catalyzed by relA (protein.P0AG20), spoT (protein.P0AG24). Substrates: ATP (molecule.C00002), GTP (molecule.C00044). Products: AMP (molecule.C00020), Guanosine 3'-diphosphate 5'-triphosphate (molecule.C04494).

## Annotation

ATP + GTP <=> AMP + Guanosine 3'-diphosphate 5'-triphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AG20|protein.P0AG20]] `KEGG` `database` - via EC:2.7.6.5
- `catalyzes` <-- [[protein.P0AG24|protein.P0AG24]] `KEGG` `database` - via EC:2.7.6.5
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494
- `is_product_of` <-- [[molecule.C04494|molecule.C04494]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494
- `is_substrate_of` <-- [[molecule.C00044|molecule.C00044]] `KEGG` `database` - C00002 + C00044 <=> C00020 + C04494

## External IDs

- `KEGG:R00429`

## Notes

EQUATION: C00002 + C00044 <=> C00020 + C04494
