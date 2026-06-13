---
entity_id: "reaction.ecocyc.TRANS-RXN0-589"
entity_type: "reaction"
name: "deoxycholate:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-589"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxycholate:proton antiport

`reaction.ecocyc.TRANS-RXN0-589`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-589`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=REVERSIBLE EcoCyc reaction equation: DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by mdtG (protein.P25744), mdtM (protein.P39386). Substrates: H+ (molecule.C00080), Deoxycholic acid (molecule.C04483). Products: H+ (molecule.C00080), Deoxycholic acid (molecule.C04483).

## Annotation

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P25744|protein.P25744]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P39386|protein.P39386]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-589`

## Notes

DEOXYCHOLATE + PROTON -> DEOXYCHOLATE + PROTON; direction=REVERSIBLE
