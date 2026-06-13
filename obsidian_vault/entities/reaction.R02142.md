---
entity_id: "reaction.R02142"
entity_type: "reaction"
name: "XMP:pyrophosphate phosphoribosyltransferase"
source_database: "KEGG"
source_id: "R02142"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R02142"
---

# XMP:pyrophosphate phosphoribosyltransferase

`reaction.R02142`

## Static

- Type: `reaction`
- Source: `KEGG:R02142`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Xanthosine 5'-phosphate + Diphosphate Xanthine + 5-Phospho-alpha-D-ribose 1-diphosphate

## Biological Role

Catalyzed by hpt (protein.P0A9M2), gpt (protein.P0A9M5). Substrates: Diphosphate (molecule.C00013), Xanthosine 5'-phosphate (molecule.C00655). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Xanthine (molecule.C00385).

## Annotation

Xanthosine 5'-phosphate + Diphosphate <=> Xanthine + 5-Phospho-alpha-D-ribose 1-diphosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A9M2|protein.P0A9M2]] `KEGG` `database` - via EC:2.4.2.8
- `catalyzes` <-- [[protein.P0A9M5|protein.P0A9M5]] `KEGG` `database` - via EC:2.4.2.22
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119
- `is_substrate_of` <-- [[molecule.C00655|molecule.C00655]] `KEGG` `database` - C00655 + C00013 <=> C00385 + C00119

## External IDs

- `KEGG:R02142`

## Notes

EQUATION: C00655 + C00013 <=> C00385 + C00119
