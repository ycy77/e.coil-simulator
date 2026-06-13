---
entity_id: "reaction.ecocyc.TRANS-RXN-299"
entity_type: "reaction"
name: "fumarate:proton symport"
source_database: "EcoCyc"
source_id: "TRANS-RXN-299"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# fumarate:proton symport

`reaction.ecocyc.TRANS-RXN-299`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-299`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

FUM + PROTON -> FUM + PROTON; direction=REVERSIBLE EcoCyc reaction equation: FUM + PROTON -> FUM + PROTON; direction=REVERSIBLE.

## Biological Role

Catalyzed by dcuA (protein.P0ABN5), dcuB (protein.P0ABN9), dcuC (protein.P0ABP3). Substrates: H+ (molecule.C00080), Fumarate (molecule.C00122). Products: H+ (molecule.C00080), Fumarate (molecule.C00122).

## Annotation

FUM + PROTON -> FUM + PROTON; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0ABN5|protein.P0ABN5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABN9|protein.P0ABN9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABP3|protein.P0ABP3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00122|molecule.C00122]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-299`

## Notes

FUM + PROTON -> FUM + PROTON; direction=REVERSIBLE
