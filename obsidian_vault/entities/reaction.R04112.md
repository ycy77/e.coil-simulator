---
entity_id: "reaction.R04112"
entity_type: "reaction"
name: "N-acetylmuramoyl-Ala amidohydrolase"
source_database: "KEGG"
source_id: "R04112"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R04112"
---

# N-acetylmuramoyl-Ala amidohydrolase

`reaction.R04112`

## Static

- Type: `reaction`
- Source: `KEGG:R04112`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N-Acetylmuramoyl-Ala + H2O N-Acetylmuramate + L-Alanine

## Biological Role

Catalyzed by ampD (protein.P13016), amiB (protein.P26365), amiA (protein.P36548), amiC (protein.P63883), amiD (protein.P75820). Substrates: H2O (molecule.C00001). Products: L-Alanine (molecule.C00041), N-Acetylmuramate (molecule.C02713).

## Annotation

N-Acetylmuramoyl-Ala + H2O <=> N-Acetylmuramate + L-Alanine

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P13016|protein.P13016]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` <-- [[protein.P26365|protein.P26365]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` <-- [[protein.P36548|protein.P36548]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` <-- [[protein.P63883|protein.P63883]] `KEGG` `database` - via EC:3.5.1.28
- `catalyzes` <-- [[protein.P75820|protein.P75820]] `KEGG` `database` - via EC:3.5.1.28
- `is_product_of` <-- [[molecule.C00041|molecule.C00041]] `KEGG` `database` - C02999 + C00001 <=> C02713 + C00041
- `is_product_of` <-- [[molecule.C02713|molecule.C02713]] `KEGG` `database` - C02999 + C00001 <=> C02713 + C00041
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C02999 + C00001 <=> C02713 + C00041

## External IDs

- `KEGG:R04112`

## Notes

EQUATION: C02999 + C00001 <=> C02713 + C00041
