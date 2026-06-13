---
entity_id: "reaction.ecocyc.PYRIMSYN3-RXN"
entity_type: "reaction"
name: "PYRIMSYN3-RXN"
source_database: "EcoCyc"
source_id: "PYRIMSYN3-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRIMSYN3-RXN

`reaction.ecocyc.PYRIMSYN3-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRIMSYN3-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third part of the multistep synthesis of the pyrimidine moiety of thiamine. EcoCyc reaction equation: AMINO-HYDROXYMETHYL-METHYL-PYR-P + ATP -> AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + ADP; direction=LEFT-TO-RIGHT. This is the third part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Biological Role

Catalyzed by hydroxymethylpyrimidine kinase / phosphomethylpyrimidine kinase (complex.ecocyc.HMP-P-KIN-CPLX). Substrates: ATP (molecule.C00002), 4-Amino-2-methyl-5-(phosphooxymethyl)pyrimidine (molecule.C04556). Products: ADP (molecule.C00008), 4-Amino-5-hydroxymethyl-2-methylpyrimidine diphosphate (molecule.C04752).

## Enriched Pathways

- `ecocyc.PWY-6890` 4-amino-2-methyl-5-diphosphomethylpyrimidine biosynthesis I (EcoCyc)
- `ecocyc.PWY-6910` hydroxymethylpyrimidine salvage (EcoCyc)

## Annotation

This is the third part of the multistep synthesis of the pyrimidine moiety of thiamine.

## Pathways

- `ecocyc.PWY-6890` 4-amino-2-methyl-5-diphosphomethylpyrimidine biosynthesis I (EcoCyc)
- `ecocyc.PWY-6910` hydroxymethylpyrimidine salvage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.HMP-P-KIN-CPLX|complex.ecocyc.HMP-P-KIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04752|molecule.C04752]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04556|molecule.C04556]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PYRIMSYN3-RXN`

## Notes

AMINO-HYDROXYMETHYL-METHYL-PYR-P + ATP -> AMINO-HYDROXYMETHYL-METHYLPYRIMIDINE-PP + ADP; direction=LEFT-TO-RIGHT
