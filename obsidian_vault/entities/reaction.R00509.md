---
entity_id: "reaction.R00509"
entity_type: "reaction"
name: "ATP:adenylylsulfate 3'-phosphotransferase"
source_database: "KEGG"
source_id: "R00509"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00509"
---

# ATP:adenylylsulfate 3'-phosphotransferase

`reaction.R00509`

## Static

- Type: `reaction`
- Source: `KEGG:R00509`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Adenylyl sulfate ADP + 3'-Phosphoadenylyl sulfate

## Biological Role

Catalyzed by cysC (protein.P0A6J1). Substrates: ATP (molecule.C00002), Adenylyl sulfate (molecule.C00224). Products: ADP (molecule.C00008), 3'-Phosphoadenylyl sulfate (molecule.C00053).

## Annotation

ATP + Adenylyl sulfate <=> ADP + 3'-Phosphoadenylyl sulfate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6J1|protein.P0A6J1]] `KEGG` `database` - via EC:2.7.1.25
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053
- `is_product_of` <-- [[molecule.C00053|molecule.C00053]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053
- `is_substrate_of` <-- [[molecule.C00224|molecule.C00224]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053

## External IDs

- `KEGG:R00509`

## Notes

EQUATION: C00002 + C00224 <=> C00008 + C00053
