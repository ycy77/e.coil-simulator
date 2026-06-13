---
entity_id: "reaction.ecocyc.RXN0-7013"
entity_type: "reaction"
name: "RXN0-7013"
source_database: "EcoCyc"
source_id: "RXN0-7013"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7013

`reaction.ecocyc.RXN0-7013`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7013`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-14762 + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-14762 + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2'-O-acetyl-ADP-ribose deacetylase, regulator of RNase III activity (complex.ecocyc.CPLX0-7758). Substrates: H2O (molecule.C00001), 2''-O-acetyl-ADP-ribose (molecule.ecocyc.CPD-14762). Products: Acetate (molecule.C00033), H+ (molecule.C00080), ADP-ribose (molecule.C00301).

## Annotation

CPD-14762 + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7758|complex.ecocyc.CPLX0-7758]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-14762|molecule.ecocyc.CPD-14762]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7013`

## Notes

CPD-14762 + WATER -> ADENOSINE_DIPHOSPHATE_RIBOSE + ACET + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
