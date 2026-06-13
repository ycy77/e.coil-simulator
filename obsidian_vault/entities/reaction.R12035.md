---
entity_id: "reaction.R12035"
entity_type: "reaction"
name: "N,N-dimethyl-1,4-phenylenediamine,anthranilate:NAD+ oxidoreductase"
source_database: "KEGG"
source_id: "R12035"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R12035"
---

# N,N-dimethyl-1,4-phenylenediamine,anthranilate:NAD+ oxidoreductase

`reaction.R12035`

## Static

- Type: `reaction`
- Source: `KEGG:R12035`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Anthranilate + N,N-Dimethyl-1,4-phenylenediamine + 2 NAD+ Methyl red + 2 NADH + 2 H+

## Biological Role

Catalyzed by azoR (protein.P41407). Substrates: NAD+ (molecule.C00003), Anthranilate (molecule.C00108). Products: NADH (molecule.C00004), H+ (molecule.C00080).

## Annotation

Anthranilate + N,N-Dimethyl-1,4-phenylenediamine + 2 NAD+ <=> Methyl red + 2 NADH + 2 H+

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P41407|protein.P41407]] `KEGG` `database` - via EC:1.7.1.17
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
- `is_substrate_of` <-- [[molecule.C00108|molecule.C00108]] `KEGG` `database` - C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080

## External IDs

- `KEGG:R12035`

## Notes

EQUATION: C00108 + C04203 + 2 C00003 <=> C19459 + 2 C00004 + 2 C00080
