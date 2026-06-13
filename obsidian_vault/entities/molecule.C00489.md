---
entity_id: "molecule.C00489"
entity_type: "small_molecule"
name: "Glutarate"
source_database: "KEGG"
source_id: "C00489"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glutarate"
  - "Glutaric acid"
  - "Pentanedioic acid"
  - "1,3-Propanedicarboxylic acid"
---

# Glutarate

`molecule.C00489`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00489`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glutarate; Glutaric acid; Pentanedioic acid; 1,3-Propanedicarboxylic acid

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)

## Annotation

KEGG compound: Glutarate; Glutaric acid; Pentanedioic acid; 1,3-Propanedicarboxylic acid

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8293|complex.ecocyc.CPLX0-8293]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R02401|reaction.R02401]] `KEGG` `database` - C03273 + C00003 + C00001 <=> C00489 + C00004 + C00080
- `is_product_of` --> [[reaction.ecocyc.RXN-8182|reaction.ecocyc.RXN-8182]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7316|reaction.ecocyc.RXN0-7316]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7327|reaction.ecocyc.RXN0-7327]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLUTDECARBOX-RXN|reaction.ecocyc.GLUTDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00489`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
