---
entity_id: "molecule.C00040"
entity_type: "small_molecule"
name: "Acyl-CoA"
source_database: "KEGG"
source_id: "C00040"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Acyl-CoA"
  - "Acyl coenzyme A"
---

# Acyl-CoA

`molecule.C00040`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00040`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Acyl-CoA; Acyl coenzyme A EcoCyc common name: an acyl-CoA. ACYL-COA "Acyl-CoAs" are oxoacids that have been activated by CO-A. They are often classified by the length of their acyl moiety.

## Biological Role

Consumed as substrate in 7 reaction(s).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

KEGG compound: Acyl-CoA; Acyl coenzyme A

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.MONOMER-51|complex.ecocyc.MONOMER-51]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_substrate_of` --> [[reaction.R00383|reaction.R00383]] `KEGG` `database` - C00040 + C00001 <=> C00010 + C00060
- `is_substrate_of` --> [[reaction.R00391|reaction.R00391]] `KEGG` `database` - C00040 + C00024 <=> C00010 + C00264
- `is_substrate_of` --> [[reaction.R00393|reaction.R00393]] `KEGG` `database` - C00040 + C00033 <=> C02403 + C00024
- `is_substrate_of` --> [[reaction.ecocyc.ACYL-COA-HYDROLASE-RXN|reaction.ecocyc.ACYL-COA-HYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R134-RXN|reaction.ecocyc.R134-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-1623|reaction.ecocyc.RXN-1623]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00040`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
