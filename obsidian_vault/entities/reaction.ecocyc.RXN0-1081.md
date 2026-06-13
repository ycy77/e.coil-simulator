---
entity_id: "reaction.ecocyc.RXN0-1081"
entity_type: "reaction"
name: "RXN0-1081"
source_database: "EcoCyc"
source_id: "RXN0-1081"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1081

`reaction.ecocyc.RXN0-1081`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1081`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + tRNA-Arg-adenosine34 + WATER -> tRNA-Arg-inosine34 + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + tRNA-Arg-adenosine34 + WATER -> tRNA-Arg-inosine34 + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA adenosine34 deaminase (complex.ecocyc.CPLX0-901). Substrates: H2O (molecule.C00001), H+ (molecule.C00080), an adenosine34 in [tRNAArg2] (molecule.ecocyc.tRNA-Arg-adenosine34). Products: ammonium (molecule.ecocyc.AMMONIUM), an inosine34 in [tRNAArg2] (molecule.ecocyc.tRNA-Arg-inosine34).

## Annotation

PROTON + tRNA-Arg-adenosine34 + WATER -> tRNA-Arg-inosine34 + AMMONIUM; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-901|complex.ecocyc.CPLX0-901]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Arg-inosine34|molecule.ecocyc.tRNA-Arg-inosine34]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-Arg-adenosine34|molecule.ecocyc.tRNA-Arg-adenosine34]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1081`

## Notes

PROTON + tRNA-Arg-adenosine34 + WATER -> tRNA-Arg-inosine34 + AMMONIUM; direction=LEFT-TO-RIGHT
