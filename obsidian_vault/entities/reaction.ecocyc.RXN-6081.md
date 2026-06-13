---
entity_id: "reaction.ecocyc.RXN-6081"
entity_type: "reaction"
name: "RXN-6081"
source_database: "EcoCyc"
source_id: "RXN-6081"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6081

`reaction.ecocyc.RXN-6081`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6081`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-ACETO-LACTATE + Acceptor + PROTON -> DIACETYL + CARBON-DIOXIDE + Donor-H2; direction=LEFT-TO-RIGHT EcoCyc reaction equation: 2-ACETO-LACTATE + Acceptor + PROTON -> DIACETYL + CARBON-DIOXIDE + Donor-H2; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), (S)-2-Acetolactate (molecule.C06010). Products: CO2 (molecule.C00011), Diacetyl (molecule.C00741).

## Annotation

2-ACETO-LACTATE + Acceptor + PROTON -> DIACETYL + CARBON-DIOXIDE + Donor-H2; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06010|molecule.C06010]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-6081`

## Notes

2-ACETO-LACTATE + Acceptor + PROTON -> DIACETYL + CARBON-DIOXIDE + Donor-H2; direction=LEFT-TO-RIGHT
