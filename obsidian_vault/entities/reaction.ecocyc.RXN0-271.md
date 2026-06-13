---
entity_id: "reaction.ecocyc.RXN0-271"
entity_type: "reaction"
name: "RXN0-271"
source_database: "EcoCyc"
source_id: "RXN0-271"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-271

`reaction.ecocyc.RXN0-271`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-271`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

ETR-Quinones + PROTON + NADPH -> ETR-Quinols + NADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ETR-Quinones + PROTON + NADPH -> ETR-Quinols + NADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by NADPH:quinone oxidoreductase MdaB (complex.ecocyc.CPLX0-253). Substrates: NADPH (molecule.C00005), H+ (molecule.C00080). Products: NADP+ (molecule.C00006).

## Annotation

ETR-Quinones + PROTON + NADPH -> ETR-Quinols + NADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-253|complex.ecocyc.CPLX0-253]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-271`

## Notes

ETR-Quinones + PROTON + NADPH -> ETR-Quinols + NADP; direction=PHYSIOL-LEFT-TO-RIGHT
