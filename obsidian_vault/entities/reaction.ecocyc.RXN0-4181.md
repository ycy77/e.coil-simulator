---
entity_id: "reaction.ecocyc.RXN0-4181"
entity_type: "reaction"
name: "RXN0-4181"
source_database: "EcoCyc"
source_id: "RXN0-4181"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-4181

`reaction.ecocyc.RXN0-4181`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-4181`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

C-DI-GMP + WATER -> PROTON + L-DI-GMP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: C-DI-GMP + WATER -> PROTON + L-DI-GMP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by DNA-binding transcriptional dual regulator/c-di-GMP phosphodiesterase PdeL (complex.ecocyc.CPLX0-8109), oxygen-sensing cyclic di-GMP phosphodiesterase DosP (complex.ecocyc.CPLX0-8199), cyclic di-GMP phosphodiesterase PdeF (complex.ecocyc.CPLX0-8200), cyclic di-GMP phosphodiesterase PdeK (complex.ecocyc.CPLX0-8555), pdeC (protein.P32701), pdeH (protein.P37646), pdeR (protein.P77334). Substrates: H2O (molecule.C00001), 3',5'-Cyclic diGMP (molecule.C16463). Products: H+ (molecule.C00080), 5'-phosphoguanylyl(3'→5')guanosine (molecule.ecocyc.L-DI-GMP).

## Annotation

C-DI-GMP + WATER -> PROTON + L-DI-GMP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (15)

- `activates` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8109|complex.ecocyc.CPLX0-8109]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8199|complex.ecocyc.CPLX0-8199]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8200|complex.ecocyc.CPLX0-8200]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8555|complex.ecocyc.CPLX0-8555]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P32701|protein.P32701]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37646|protein.P37646]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77334|protein.P77334]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.L-DI-GMP|molecule.ecocyc.L-DI-GMP]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C16463|molecule.C16463]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-4181`

## Notes

C-DI-GMP + WATER -> PROTON + L-DI-GMP; direction=PHYSIOL-LEFT-TO-RIGHT
