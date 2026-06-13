---
entity_id: "molecule.C00059"
entity_type: "small_molecule"
name: "Sulfate"
source_database: "KEGG"
source_id: "C00059"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Sulfate"
  - "Sulfuric acid"
---

# Sulfate

`molecule.C00059`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00059`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Sulfate; Sulfuric acid

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

KEGG compound: Sulfate; Sulfuric acid

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (11)

- `activates` --> [[reaction.ecocyc.F16BDEPHOS-RXN|reaction.ecocyc.F16BDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.ABC-70-RXN|reaction.ecocyc.ABC-70-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15761|reaction.ecocyc.RXN-15761]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-586|reaction.ecocyc.TRANS-RXN0-586]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00529|reaction.R00529]] `KEGG` `database` - C00002 + C00059 <=> C00013 + C00224
- `is_substrate_of` --> [[reaction.ecocyc.ABC-70-RXN|reaction.ecocyc.ABC-70-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN|reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-586|reaction.ecocyc.TRANS-RXN0-586]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.D-PPENTOMUT-RXN|reaction.ecocyc.D-PPENTOMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GSADENYLATION-RXN|reaction.ecocyc.GSADENYLATION-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN|reaction.ecocyc.THIOSULFATE-SULFURTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-7-CPLX|complex.ecocyc.ABC-7-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0A6J3|protein.P0A6J3]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00059`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
