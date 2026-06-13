---
entity_id: "reaction.ecocyc.SUCCARGDIHYDRO-RXN"
entity_type: "reaction"
name: "SUCCARGDIHYDRO-RXN"
source_database: "EcoCyc"
source_id: "SUCCARGDIHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# SUCCARGDIHYDRO-RXN

`reaction.ecocyc.SUCCARGDIHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:SUCCARGDIHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD-421 + WATER -> AMMONIUM + N2-SUCCINYLORNITHINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD-421 + WATER -> AMMONIUM + N2-SUCCINYLORNITHINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by N-succinylarginine dihydrolase (complex.ecocyc.CPLX0-7947). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), N2-Succinyl-L-arginine (molecule.C03296). Products: CO2 (molecule.C00011), N2-Succinyl-L-ornithine (molecule.C03415), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Annotation

PROTON + CPD-421 + WATER -> AMMONIUM + N2-SUCCINYLORNITHINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.AST-PWY` L-arginine degradation II (AST pathway) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7947|complex.ecocyc.CPLX0-7947]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03415|molecule.C03415]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03296|molecule.C03296]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:SUCCARGDIHYDRO-RXN`

## Notes

PROTON + CPD-421 + WATER -> AMMONIUM + N2-SUCCINYLORNITHINE + CARBON-DIOXIDE; direction=LEFT-TO-RIGHT
