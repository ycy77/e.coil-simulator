---
entity_id: "reaction.R04148"
entity_type: "reaction"
name: "nicotinate-nucleotide:dimethylbenzimidazole phospho-D-ribosyltransferase"
source_database: "KEGG"
source_id: "R04148"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04148"
---

# nicotinate-nucleotide:dimethylbenzimidazole phospho-D-ribosyltransferase

`reaction.R04148`

## Static

- Type: `reaction`
- Source: `KEGG:R04148`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nicotinate D-ribonucleotide + Dimethylbenzimidazole Nicotinate + N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole + H+

## Biological Role

Catalyzed by cobT (protein.P36562). Substrates: Nicotinate D-ribonucleotide (molecule.C01185), Dimethylbenzimidazole (molecule.C03114). Products: H+ (molecule.C00080), Nicotinate (molecule.C00253), N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole (molecule.C04778).

## Annotation

Nicotinate D-ribonucleotide + Dimethylbenzimidazole <=> Nicotinate + N1-(5-Phospho-alpha-D-ribosyl)-5,6-dimethylbenzimidazole + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P36562|protein.P36562]] `KEGG` `database` - via EC:2.4.2.21
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_product_of` <-- [[molecule.C00253|molecule.C00253]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_product_of` <-- [[molecule.C04778|molecule.C04778]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_substrate_of` <-- [[molecule.C01185|molecule.C01185]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080
- `is_substrate_of` <-- [[molecule.C03114|molecule.C03114]] `KEGG` `database` - C01185 + C03114 <=> C00253 + C04778 + C00080

## External IDs

- `KEGG:R04148`

## Notes

EQUATION: C01185 + C03114 <=> C00253 + C04778 + C00080
