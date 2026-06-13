---
entity_id: "reaction.ecocyc.AMINOBUTDEHYDROG-RXN"
entity_type: "reaction"
name: "AMINOBUTDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "AMINOBUTDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMINOBUTDEHYDROG-RXN

`reaction.ecocyc.AMINOBUTDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMINOBUTDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in a putrescine degradative pathway. EcoCyc reaction equation: 4-AMINO-BUTYRALDEHYDE + NAD + WATER -> 4-AMINO-BUTYRATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the second reaction in a putrescine degradative pathway.

## Biological Role

Catalyzed by γ-aminobutyraldehyde dehydrogenase (complex.ecocyc.CPLX0-3641), puuC (protein.P23883). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), 4-Aminobutyraldehyde (molecule.C00555). Products: NADH (molecule.C00004), H+ (molecule.C00080), 4-Aminobutanoate (molecule.C00334).

## Enriched Pathways

- `ecocyc.PUTDEG-PWY` putrescine degradation I (EcoCyc)

## Annotation

This is the second reaction in a putrescine degradative pathway.

## Pathways

- `ecocyc.PUTDEG-PWY` putrescine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3641|complex.ecocyc.CPLX0-3641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P23883|protein.P23883]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00334|molecule.C00334]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00555|molecule.C00555]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AMINOBUTDEHYDROG-RXN`

## Notes

4-AMINO-BUTYRALDEHYDE + NAD + WATER -> 4-AMINO-BUTYRATE + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
