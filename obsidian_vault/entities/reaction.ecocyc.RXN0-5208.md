---
entity_id: "reaction.ecocyc.RXN0-5208"
entity_type: "reaction"
name: "RXN0-5208"
source_database: "EcoCyc"
source_id: "RXN0-5208"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5208

`reaction.ecocyc.RXN0-5208`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5208`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + ATP -> ADENOSYL-P4 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + ATP -> ADENOSYL-P4 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2,3-dihydroxybenzoate-[aryl-carrier protein] ligase (complex.ecocyc.ENTE-CPLX), lysine—tRNA ligase (complex.ecocyc.LYSU-CPLX). Substrates: ATP (molecule.C00002), H+ (molecule.C00080). Products: Diphosphate (molecule.C00013), P1,P4-Bis(5'-adenosyl)tetraphosphate (molecule.C01260).

## Annotation

PROTON + ATP -> ADENOSYL-P4 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ENTE-CPLX|complex.ecocyc.ENTE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.LYSU-CPLX|complex.ecocyc.LYSU-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01260|molecule.C01260]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5208`

## Notes

PROTON + ATP -> ADENOSYL-P4 + PPI; direction=PHYSIOL-LEFT-TO-RIGHT
