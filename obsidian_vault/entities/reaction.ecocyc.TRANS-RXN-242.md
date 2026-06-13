---
entity_id: "reaction.ecocyc.TRANS-RXN-242"
entity_type: "reaction"
name: "L-homoserine:proton antiport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-242"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# L-homoserine:proton antiport

`reaction.ecocyc.TRANS-RXN-242`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-242`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

PROTON + HOMO-SER -> PROTON + HOMO-SER; direction=REVERSIBLE EcoCyc reaction equation: PROTON + HOMO-SER -> PROTON + HOMO-SER; direction=REVERSIBLE.

## Biological Role

Catalyzed by rhtA (protein.P0AA67), rhtB (protein.P0AG34). Substrates: H+ (molecule.C00080), L-Homoserine (molecule.C00263). Products: H+ (molecule.C00080), L-Homoserine (molecule.C00263).

## Annotation

PROTON + HOMO-SER -> PROTON + HOMO-SER; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0AA67|protein.P0AA67]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AG34|protein.P0AG34]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00263|molecule.C00263]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN-242`

## Notes

PROTON + HOMO-SER -> PROTON + HOMO-SER; direction=REVERSIBLE
