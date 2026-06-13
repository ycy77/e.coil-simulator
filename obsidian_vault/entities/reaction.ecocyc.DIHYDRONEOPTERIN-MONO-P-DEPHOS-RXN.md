---
entity_id: "reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN"
entity_type: "reaction"
name: "DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN"
source_database: "EcoCyc"
source_id: "DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN

`reaction.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the biosynthesis of folic acid. It is uncertain whether there is a specific enzyme for this reaction. E. coli does contain nonspecific phophatases that can catalyze this reaction. EcoCyc reaction equation: DIHYDRONEOPTERIN-P + WATER -> DIHYDRO-NEO-PTERIN + Pi; direction=LEFT-TO-RIGHT. This is a reaction in the biosynthesis of folic acid. It is uncertain whether there is a specific enzyme for this reaction. E. coli does contain nonspecific phophatases that can catalyze this reaction.

## Biological Role

Catalyzed by DIHYDRONEOPTERIN-MONO-P-DEPHOS-MONOMER (protein.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-MONOMER). Substrates: H2O (molecule.C00001), Dihydroneopterin phosphate (molecule.C05925). Products: 7,8-Dihydroneopterin (molecule.C04874), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Annotation

This is a reaction in the biosynthesis of folic acid. It is uncertain whether there is a specific enzyme for this reaction. E. coli does contain nonspecific phophatases that can catalyze this reaction.

## Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-MONOMER|protein.ecocyc.DIHYDRONEOPTERIN-MONO-P-DEPHOS-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04874|molecule.C04874]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05925|molecule.C05925]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DIHYDRONEOPTERIN-MONO-P-DEPHOS-RXN`

## Notes

DIHYDRONEOPTERIN-P + WATER -> DIHYDRO-NEO-PTERIN + Pi; direction=LEFT-TO-RIGHT
