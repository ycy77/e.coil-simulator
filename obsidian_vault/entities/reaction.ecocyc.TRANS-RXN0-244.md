---
entity_id: "reaction.ecocyc.TRANS-RXN0-244"
entity_type: "reaction"
name: "Cd2+:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-244"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# Cd2+:proton antiport

`reaction.ecocyc.TRANS-RXN0-244`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-244`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CD+2 -> PROTON + CD+2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CD+2 -> PROTON + CD+2; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by Zn2+/Fe2+/Cd2+ exporter (complex.ecocyc.CPLX0-7641). Substrates: H+ (molecule.C00080), Cd2+ (molecule.ecocyc.CD_2). Products: H+ (molecule.C00080), Cd2+ (molecule.ecocyc.CD_2).

## Annotation

PROTON + CD+2 -> PROTON + CD+2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7641|complex.ecocyc.CPLX0-7641]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-244`

## Notes

PROTON + CD+2 -> PROTON + CD+2; direction=LEFT-TO-RIGHT
