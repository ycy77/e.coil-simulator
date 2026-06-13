---
entity_id: "reaction.R01909"
entity_type: "reaction"
name: "ATP:pyridoxine 5'-phosphotransferase"
source_database: "KEGG"
source_id: "R01909"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01909"
---

# ATP:pyridoxine 5'-phosphotransferase

`reaction.R01909`

## Static

- Type: `reaction`
- Source: `KEGG:R01909`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Pyridoxine ADP + Pyridoxine phosphate

## Biological Role

Catalyzed by pdxK (protein.P40191), pdxY (protein.P77150). Substrates: ATP (molecule.C00002), Pyridoxine (molecule.C00314). Products: ADP (molecule.C00008), Pyridoxine phosphate (molecule.C00627).

## Annotation

ATP + Pyridoxine <=> ADP + Pyridoxine phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P40191|protein.P40191]] `KEGG` `database` - via EC:2.7.1.35
- `catalyzes` <-- [[protein.P77150|protein.P77150]] `KEGG` `database` - via EC:2.7.1.35
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627
- `is_product_of` <-- [[molecule.C00627|molecule.C00627]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627
- `is_substrate_of` <-- [[molecule.C00314|molecule.C00314]] `KEGG` `database` - C00002 + C00314 <=> C00008 + C00627

## External IDs

- `KEGG:R01909`

## Notes

EQUATION: C00002 + C00314 <=> C00008 + C00627
