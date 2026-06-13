---
entity_id: "reaction.ecocyc.RXN0-3962"
entity_type: "reaction"
name: "RXN0-3962"
source_database: "EcoCyc"
source_id: "RXN0-3962"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3962

`reaction.ecocyc.RXN0-3962`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3962`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ACETALD + NADP + WATER -> ACET + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ACETALD + NADP + WATER -> ACET + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by aldehyde dehydrogenase B (complex.ecocyc.CPLX0-3482). Substrates: H2O (molecule.C00001), NADP+ (molecule.C00006), Acetaldehyde (molecule.C00084). Products: NADPH (molecule.C00005), Acetate (molecule.C00033), H+ (molecule.C00080).

## Annotation

ACETALD + NADP + WATER -> ACET + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3482|complex.ecocyc.CPLX0-3482]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-3962`

## Notes

ACETALD + NADP + WATER -> ACET + NADPH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
