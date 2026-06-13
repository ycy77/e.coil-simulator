---
entity_id: "reaction.ecocyc.RXN0-1721"
entity_type: "reaction"
name: "RXN0-1721"
source_database: "EcoCyc"
source_id: "RXN0-1721"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1721

`reaction.ecocyc.RXN0-1721`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1721`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD0-2482 + PROTON -> CPD0-2482 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-2482 + PROTON -> CPD0-2482 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine trimer] complex (molecule.ecocyc.CPD0-2482). Products: H+ (molecule.C00080), iron(III)-[N-(2,3-dihydroxybenzoyl)-L-serine trimer] complex (molecule.ecocyc.CPD0-2482).

## Annotation

CPD0-2482 + PROTON -> CPD0-2482 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-2482|molecule.ecocyc.CPD0-2482]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2482|molecule.ecocyc.CPD0-2482]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1721`

## Notes

CPD0-2482 + PROTON -> CPD0-2482 + PROTON; direction=LEFT-TO-RIGHT
