---
entity_id: "reaction.ecocyc.TRANS-RXN-82"
entity_type: "reaction"
name: "lactose:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-82"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lactose:proton antiport

`reaction.ecocyc.TRANS-RXN-82`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-82`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=REVERSIBLE EcoCyc reaction equation: PROTON + CPD-15972 -> PROTON + CPD-15972; direction=REVERSIBLE.

## Biological Role

Catalyzed by setA (protein.P31675), setB (protein.P33026). Substrates: H+ (molecule.C00080), Lactose (molecule.C00243). Products: H+ (molecule.C00080), Lactose (molecule.C00243).

## Annotation

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (14)

- `catalyzes` <-- [[protein.P31675|protein.P31675]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33026|protein.P33026]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CELLOBIOSE|molecule.ecocyc.CELLOBIOSE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-22525|molecule.ecocyc.CPD-22525]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-22526|molecule.ecocyc.CPD-22526]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-22528|molecule.ecocyc.CPD-22528]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1667|molecule.ecocyc.CPD0-1667]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1668|molecule.ecocyc.CPD0-1668]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-82`

## Notes

PROTON + CPD-15972 -> PROTON + CPD-15972; direction=REVERSIBLE
