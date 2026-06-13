---
entity_id: "reaction.ecocyc.GMP-REDUCT-RXN"
entity_type: "reaction"
name: "GMP-REDUCT-RXN"
source_database: "EcoCyc"
source_id: "GMP-REDUCT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GMP-REDUCT-RXN

`reaction.ecocyc.GMP-REDUCT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GMP-REDUCT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of nucleotide metabolism. EcoCyc reaction equation: AMMONIUM + IMP + NADP -> PROTON + GMP + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is part of nucleotide metabolism.

## Biological Role

Catalyzed by GMP reductase (complex.ecocyc.GMP-REDUCT-CPLX). Substrates: NADP+ (molecule.C00006), IMP (molecule.C00130), ammonium (molecule.ecocyc.AMMONIUM). Products: NADPH (molecule.C00005), H+ (molecule.C00080), GMP (molecule.C00144).

## Annotation

This reaction is part of nucleotide metabolism.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.GMP-REDUCT-CPLX|complex.ecocyc.GMP-REDUCT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GMP-REDUCT-RXN`

## Notes

AMMONIUM + IMP + NADP -> PROTON + GMP + NADPH; direction=PHYSIOL-RIGHT-TO-LEFT
