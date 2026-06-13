---
entity_id: "reaction.ecocyc.DHDOGALDOL-RXN"
entity_type: "reaction"
name: "DHDOGALDOL-RXN"
source_database: "EcoCyc"
source_id: "DHDOGALDOL-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DHDOGALDOL-RXN

`reaction.ecocyc.DHDOGALDOL-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DHDOGALDOL-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-DEHYDRO-3-DEOXY-D-GLUCONATE -> GLYCERALD + PYRUVATE; direction=REVERSIBLE EcoCyc reaction equation: 2-DEHYDRO-3-DEOXY-D-GLUCONATE -> GLYCERALD + PYRUVATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by CP4-6 prophage; 2-dehydro-3-deoxygluconate aldolase (complex.ecocyc.CPLX0-7940). Substrates: 2-Dehydro-3-deoxy-D-gluconate (molecule.C00204). Products: Pyruvate (molecule.C00022), D-Glyceraldehyde (molecule.C00577).

## Annotation

2-DEHYDRO-3-DEOXY-D-GLUCONATE -> GLYCERALD + PYRUVATE; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7940|complex.ecocyc.CPLX0-7940]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00577|molecule.C00577]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00204|molecule.C00204]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DHDOGALDOL-RXN`

## Notes

2-DEHYDRO-3-DEOXY-D-GLUCONATE -> GLYCERALD + PYRUVATE; direction=REVERSIBLE
