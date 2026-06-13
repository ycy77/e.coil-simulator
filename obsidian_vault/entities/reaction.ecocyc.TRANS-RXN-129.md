---
entity_id: "reaction.ecocyc.TRANS-RXN-129"
entity_type: "reaction"
name: "electrogenic sodium:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-129"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# electrogenic sodium:proton antiport

`reaction.ecocyc.TRANS-RXN-129`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-129`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

NA+ + PROTON -> NA+ + PROTON; direction=REVERSIBLE EcoCyc reaction equation: NA+ + PROTON -> NA+ + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by Na+:H+ antiporter NhaA (complex.ecocyc.CPLX0-7629), mdtM (protein.P39386). Substrates: H+ (molecule.C00080), Sodium cation (molecule.C01330). Products: H+ (molecule.C00080), Sodium cation (molecule.C01330).

## Annotation

NA+ + PROTON -> NA+ + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7629|complex.ecocyc.CPLX0-7629]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39386|protein.P39386]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-129`

## Notes

NA+ + PROTON -> NA+ + PROTON; direction=REVERSIBLE
