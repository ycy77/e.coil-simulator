---
entity_id: "reaction.R03662"
entity_type: "reaction"
name: "L-serine:tRNA(Ser) ligase (AMP-forming)"
source_database: "KEGG"
source_id: "R03662"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R03662"
---

# L-serine:tRNA(Ser) ligase (AMP-forming)

`reaction.R03662`

## Static

- Type: `reaction`
- Source: `KEGG:R03662`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + L-Serine + tRNA(Ser) AMP + Diphosphate + L-Seryl-tRNA(Ser)

## Biological Role

Catalyzed by serS (protein.P0A8L1). Substrates: ATP (molecule.C00002), L-Serine (molecule.C00065). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), L-Seryl-tRNA(Ser) (molecule.C02553).

## Annotation

ATP + L-Serine + tRNA(Ser) <=> AMP + Diphosphate + L-Seryl-tRNA(Ser)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A8L1|protein.P0A8L1]] `KEGG` `database` - via EC:6.1.1.11
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
- `is_product_of` <-- [[molecule.C02553|molecule.C02553]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `KEGG` `database` - C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553

## External IDs

- `KEGG:R03662`

## Notes

EQUATION: C00002 + C00065 + C01650 <=> C00020 + C00013 + C02553
