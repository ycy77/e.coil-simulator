---
entity_id: "molecule.C02133"
entity_type: "small_molecule"
name: "Acyl phosphate"
source_database: "KEGG"
source_id: "C02133"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acyl phosphate"
  - "Fatty acyl phosphate"
---

# Acyl phosphate

`molecule.C02133`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02133`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acyl phosphate; Fatty acyl phosphate EcoCyc common name: an acyl phosphate.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Annotation

KEGG compound: Acyl phosphate; Fatty acyl phosphate

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-9590|reaction.ecocyc.RXN-9590]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00539|reaction.R00539]] `KEGG` `database` - C02133 + C00001 <=> C00060 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.ACYLPHOSPHATASE-RXN|reaction.ecocyc.ACYLPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02133`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
