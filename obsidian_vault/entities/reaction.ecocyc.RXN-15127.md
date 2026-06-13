---
entity_id: "reaction.ecocyc.RXN-15127"
entity_type: "reaction"
name: "RXN-15127"
source_database: "EcoCyc"
source_id: "RXN-15127"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-15127

`reaction.ecocyc.RXN-15127`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-15127`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-16015 + WATER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-16015 + WATER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by enamine/imine deaminase, redox-regulated chaperone (complex.ecocyc.CPLX0-1881). Substrates: H2O (molecule.C00001), 2-iminopropanoate (molecule.ecocyc.CPD-16015). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)
- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)
- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)
- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Annotation

CPD-16015 + WATER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LCYSDEG-PWY` L-cysteine degradation II (EcoCyc)
- `ecocyc.PWY0-1535` D-serine degradation (EcoCyc)
- `ecocyc.SERDEG-PWY` L-serine degradation (EcoCyc)
- `ecocyc.TRYPDEG-PWY` L-tryptophan degradation II (via pyruvate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1881|complex.ecocyc.CPLX0-1881]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-16015|molecule.ecocyc.CPD-16015]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-15127`

## Notes

CPD-16015 + WATER -> PYRUVATE + AMMONIUM; direction=PHYSIOL-LEFT-TO-RIGHT
