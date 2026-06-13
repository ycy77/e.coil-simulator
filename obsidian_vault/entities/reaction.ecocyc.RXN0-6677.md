---
entity_id: "reaction.ecocyc.RXN0-6677"
entity_type: "reaction"
name: "RXN0-6677"
source_database: "EcoCyc"
source_id: "RXN0-6677"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6677

`reaction.ecocyc.RXN0-6677`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6677`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-13314 + NADPH + PROTON -> CPD-13315 + NADP; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-13314 + NADPH + PROTON -> CPD-13315 + NADP; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADPH-dependent curcumin/dihydrocurcumin reductase (complex.ecocyc.CPLX0-7927). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080), dihydrocurcumin (molecule.ecocyc.CPD-13314). Products: NADP+ (molecule.C00006), tetrahydrocurcumin (molecule.ecocyc.CPD-13315).

## Enriched Pathways

- `ecocyc.PWY0-1527` curcumin degradation (EcoCyc)

## Annotation

CPD-13314 + NADPH + PROTON -> CPD-13315 + NADP; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1527` curcumin degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7927|complex.ecocyc.CPLX0-7927]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-13315|molecule.ecocyc.CPD-13315]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-13314|molecule.ecocyc.CPD-13314]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6677`

## Notes

CPD-13314 + NADPH + PROTON -> CPD-13315 + NADP; direction=LEFT-TO-RIGHT
