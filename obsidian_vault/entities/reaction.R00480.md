---
entity_id: "reaction.R00480"
entity_type: "reaction"
name: "ATP:L-aspartate 4-phosphotransferase"
source_database: "KEGG"
source_id: "R00480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00480"
---

# ATP:L-aspartate 4-phosphotransferase

`reaction.R00480`

## Static

- Type: `reaction`
- Source: `KEGG:R00480`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Aspartate ADP + 4-Phospho-L-aspartate

## Biological Role

Catalyzed by thrA (protein.P00561), metL (protein.P00562), lysC (protein.P08660). Substrates: ATP (molecule.C00002), L-Aspartate (molecule.C00049). Products: ADP (molecule.C00008), 4-Phospho-L-aspartate (molecule.C03082).

## Annotation

ATP + L-Aspartate <=> ADP + 4-Phospho-L-aspartate

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P00561|protein.P00561]] `KEGG` `database` - via EC:2.7.2.4
- `catalyzes` <-- [[protein.P00562|protein.P00562]] `KEGG` `database` - via EC:2.7.2.4
- `catalyzes` <-- [[protein.P08660|protein.P08660]] `KEGG` `database` - via EC:2.7.2.4
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082
- `is_product_of` <-- [[molecule.C03082|molecule.C03082]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082
- `is_substrate_of` <-- [[molecule.C00049|molecule.C00049]] `KEGG` `database` - C00002 + C00049 <=> C00008 + C03082

## External IDs

- `KEGG:R00480`

## Notes

EQUATION: C00002 + C00049 <=> C00008 + C03082
