---
entity_id: "reaction.ecocyc.RXN-18819"
entity_type: "reaction"
name: "RXN-18819"
source_database: "EcoCyc"
source_id: "RXN-18819"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-18819

`reaction.ecocyc.RXN-18819`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-18819`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

D-Ribose + GLY -> CPD-10204 + WATER + GLY; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: D-Ribose + GLY -> CPD-10204 + WATER + GLY; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: Glycine (molecule.C00037), D-Ribose (molecule.C00121). Products: H2O (molecule.C00001), Glycine (molecule.C00037), norfuraneol (molecule.ecocyc.CPD-10204).

## Annotation

D-Ribose + GLY -> CPD-10204 + WATER + GLY; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-10204|molecule.ecocyc.CPD-10204]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00121|molecule.C00121]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-18819`

## Notes

D-Ribose + GLY -> CPD-10204 + WATER + GLY; direction=PHYSIOL-LEFT-TO-RIGHT
