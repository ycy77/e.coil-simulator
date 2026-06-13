---
entity_id: "molecule.C00555"
entity_type: "small_molecule"
name: "4-Aminobutyraldehyde"
source_database: "KEGG"
source_id: "C00555"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "4-Aminobutyraldehyde"
  - "4-Aminobutanal"
---

# 4-Aminobutyraldehyde

`molecule.C00555`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00555`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 4-Aminobutyraldehyde; 4-Aminobutanal EcoCyc common name: 4-aminobutanal.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)

## Annotation

KEGG compound: 4-Aminobutyraldehyde; 4-Aminobutanal

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)

## Outgoing Edges (4)

- `is_product_of` --> [[reaction.R01155|reaction.R01155]] `KEGG` `database` - C00134 + C00026 <=> C00555 + C00025
- `is_product_of` --> [[reaction.ecocyc.PUTTRANSAM-RXN|reaction.ecocyc.PUTTRANSAM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.AMINOBUTDEHYDROG-RXN|reaction.ecocyc.AMINOBUTDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-6423|reaction.ecocyc.RXN-6423]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00555`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
