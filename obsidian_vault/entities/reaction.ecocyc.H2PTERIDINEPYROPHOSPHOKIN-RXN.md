---
entity_id: "reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN"
entity_type: "reaction"
name: "H2PTERIDINEPYROPHOSPHOKIN-RXN"
source_database: "EcoCyc"
source_id: "H2PTERIDINEPYROPHOSPHOKIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# H2PTERIDINEPYROPHOSPHOKIN-RXN

`reaction.ecocyc.H2PTERIDINEPYROPHOSPHOKIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:H2PTERIDINEPYROPHOSPHOKIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in folic acid biosynthesis. EcoCyc reaction equation: AMINO-OH-HYDROXYMETHYL-DIHYDROPTERIDINE + ATP -> PROTON + DIHYDROPTERIN-CH2OH-PP + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This is a reaction in folic acid biosynthesis.

## Biological Role

Catalyzed by folK (protein.P26281). Substrates: ATP (molecule.C00002), 6-(Hydroxymethyl)-7,8-dihydropterin (molecule.C01300). Products: AMP (molecule.C00020), H+ (molecule.C00080), 6-Hydroxymethyl-7,8-dihydropterin diphosphate (molecule.C04807).

## Enriched Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Annotation

This is a reaction in folic acid biosynthesis.

## Pathways

- `ecocyc.PWY-6147` 6-hydroxymethyl-dihydropterin diphosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P26281|protein.P26281]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04807|molecule.C04807]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01300|molecule.C01300]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:H2PTERIDINEPYROPHOSPHOKIN-RXN`

## Notes

AMINO-OH-HYDROXYMETHYL-DIHYDROPTERIDINE + ATP -> PROTON + DIHYDROPTERIN-CH2OH-PP + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
