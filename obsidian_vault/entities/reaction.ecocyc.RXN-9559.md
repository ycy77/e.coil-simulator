---
entity_id: "reaction.ecocyc.RXN-9559"
entity_type: "reaction"
name: "RXN-9559"
source_database: "EcoCyc"
source_id: "RXN-9559"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-9559

`reaction.ecocyc.RXN-9559`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-9559`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-10204 + FORMALDEHYDE -> CPD-10205 + WATER; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-10204 + FORMALDEHYDE -> CPD-10205 + WATER; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: Formaldehyde (molecule.C00067), norfuraneol (molecule.ecocyc.CPD-10204). Products: H2O (molecule.C00001), 4-hydroxy-5-methyl-2-methylene-3(2H)-furanone (molecule.ecocyc.CPD-10205).

## Annotation

CPD-10204 + FORMALDEHYDE -> CPD-10205 + WATER; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-10205|molecule.ecocyc.CPD-10205]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00067|molecule.C00067]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-10204|molecule.ecocyc.CPD-10204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-9559`

## Notes

CPD-10204 + FORMALDEHYDE -> CPD-10205 + WATER; direction=LEFT-TO-RIGHT
