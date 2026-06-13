---
entity_id: "molecule.C00224"
entity_type: "small_molecule"
name: "Adenylyl sulfate"
source_database: "KEGG"
source_id: "C00224"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Adenylyl sulfate"
  - "Adenosine 5'-phosphosulfate"
  - "APS"
  - "5'-Adenylyl sulfate"
---

# Adenylyl sulfate

`molecule.C00224`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00224`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Adenylyl sulfate; Adenosine 5'-phosphosulfate; APS; 5'-Adenylyl sulfate EcoCyc common name: adenosine 5'-phosphosulfate.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

KEGG compound: Adenylyl sulfate; Adenosine 5'-phosphosulfate; APS; 5'-Adenylyl sulfate

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.MONOMER-2720|complex.ecocyc.MONOMER-2720]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00508|reaction.R00508]] `KEGG` `database` - C00053 + C00001 <=> C00224 + C00009
- `is_product_of` --> [[reaction.R00529|reaction.R00529]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224
- `is_product_of` --> [[reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN|reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00509|reaction.R00509]] `KEGG` `database` - C00002 + C00224 <=> C00008 + C00053
- `is_substrate_of` --> [[reaction.ecocyc.ADENYLYLSULFKIN-RXN|reaction.ecocyc.ADENYLYLSULFKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-5077|reaction.ecocyc.RXN-5077]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ADENYLYLSULFKIN-RXN|reaction.ecocyc.ADENYLYLSULFKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00224`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
