---
entity_id: "reaction.ecocyc.XANPRIBOSYLTRAN-RXN"
entity_type: "reaction"
name: "XANPRIBOSYLTRAN-RXN"
source_database: "EcoCyc"
source_id: "XANPRIBOSYLTRAN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# XANPRIBOSYLTRAN-RXN

`reaction.ecocyc.XANPRIBOSYLTRAN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:XANPRIBOSYLTRAN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in purine salvage. EcoCyc reaction equation: XANTHOSINE-5-PHOSPHATE + PPI -> XANTHINE + PRPP; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is involved in purine salvage.

## Biological Role

Catalyzed by xanthine-guanine phosphoribosyltransferase (complex.ecocyc.GPT-CPLX). Substrates: Diphosphate (molecule.C00013), Xanthosine 5'-phosphate (molecule.C00655). Products: 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Xanthine (molecule.C00385).

## Enriched Pathways

- `ecocyc.SALVPURINE2-PWY` xanthine and xanthosine salvage (EcoCyc)

## Annotation

This reaction is involved in purine salvage.

## Pathways

- `ecocyc.SALVPURINE2-PWY` xanthine and xanthosine salvage (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.GPT-CPLX|complex.ecocyc.GPT-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00385|molecule.C00385]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5721|molecule.ecocyc.CPD-5721]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1143|molecule.ecocyc.CPD0-1143]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:XANPRIBOSYLTRAN-RXN`

## Notes

XANTHOSINE-5-PHOSPHATE + PPI -> XANTHINE + PRPP; direction=PHYSIOL-RIGHT-TO-LEFT
