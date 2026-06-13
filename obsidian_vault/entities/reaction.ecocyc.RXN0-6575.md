---
entity_id: "reaction.ecocyc.RXN0-6575"
entity_type: "reaction"
name: "RXN0-6575"
source_database: "EcoCyc"
source_id: "RXN0-6575"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6575

`reaction.ecocyc.RXN0-6575`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6575`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + CPD0-1699 -> CPD-13043 + AMMONIUM; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + CPD0-1699 -> CPD-13043 + AMMONIUM; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by queE (protein.P64554). Substrates: H+ (molecule.C00080), 6-Carboxy-5,6,7,8-tetrahydropterin (molecule.C20239). Products: 7-Carboxy-7-carbaguanine (molecule.C20248), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Annotation

PROTON + CPD0-1699 -> CPD-13043 + AMMONIUM; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-6703` preQ0 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P64554|protein.P64554]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C20248|molecule.C20248]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C20239|molecule.C20239]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6575`

## Notes

PROTON + CPD0-1699 -> CPD-13043 + AMMONIUM; direction=LEFT-TO-RIGHT
