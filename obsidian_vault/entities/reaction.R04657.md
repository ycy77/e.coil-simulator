---
entity_id: "reaction.R04657"
entity_type: "reaction"
name: "ATP:2,3,2',3'-tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-beta-D-1,6-glucosaminyl-alpha-phosphate 4-O'-phosphotransferase"
source_database: "KEGG"
source_id: "R04657"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04657"
---

# ATP:2,3,2',3'-tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-beta-D-1,6-glucosaminyl-alpha-phosphate 4-O'-phosphotransferase

`reaction.R04657`

## Static

- Type: `reaction`
- Source: `KEGG:R04657`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + Lipid A disaccharide ADP + 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate

## Biological Role

Catalyzed by lpxK (protein.P27300). Substrates: ATP (molecule.C00002), Lipid A disaccharide (molecule.C04932). Products: ADP (molecule.C00008), 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate (molecule.C04919).

## Annotation

ATP + Lipid A disaccharide <=> ADP + 2,3,2'3'-Tetrakis(3-hydroxytetradecanoyl)-D-glucosaminyl-1,6-beta-D-glucosamine 1,4'-bisphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P27300|protein.P27300]] `KEGG` `database` - via EC:2.7.1.130
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919
- `is_product_of` <-- [[molecule.C04919|molecule.C04919]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919
- `is_substrate_of` <-- [[molecule.C04932|molecule.C04932]] `KEGG` `database` - C00002 + C04932 <=> C00008 + C04919

## External IDs

- `KEGG:R04657`

## Notes

EQUATION: C00002 + C04932 <=> C00008 + C04919
