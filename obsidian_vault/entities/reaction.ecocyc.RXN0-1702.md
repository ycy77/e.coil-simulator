---
entity_id: "reaction.ecocyc.RXN0-1702"
entity_type: "reaction"
name: "RXN0-1702"
source_database: "EcoCyc"
source_id: "RXN0-1702"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1702

`reaction.ecocyc.RXN0-1702`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1702`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD0-621 + PROTON -> CPD0-621 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-621 + PROTON -> CPD0-621 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferric coprogen outer membrane transport complex (complex.ecocyc.CPLX0-7952). Substrates: H+ (molecule.C00080), iron(III)-coprogen (molecule.ecocyc.CPD0-621). Products: H+ (molecule.C00080), iron(III)-coprogen (molecule.ecocyc.CPD0-621).

## Annotation

CPD0-621 + PROTON -> CPD0-621 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7952|complex.ecocyc.CPLX0-7952]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-621|molecule.ecocyc.CPD0-621]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-621|molecule.ecocyc.CPD0-621]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1702`

## Notes

CPD0-621 + PROTON -> CPD0-621 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
