---
entity_id: "reaction.ecocyc.GLYCOLATEDEHYDRO-RXN"
entity_type: "reaction"
name: "GLYCOLATEDEHYDRO-RXN"
source_database: "EcoCyc"
source_id: "GLYCOLATEDEHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOLATEDEHYDRO-RXN

`reaction.ecocyc.GLYCOLATEDEHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOLATEDEHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the metabolism of glycolate. EcoCyc reaction equation: Acceptor + GLYCOLLATE -> Donor-H2 + GLYOX; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of the metabolism of glycolate.

## Biological Role

Catalyzed by glycolate dehydrogenase (complex.ecocyc.CPLX0-7458). Substrates: Glycolate (molecule.C00160). Products: Glyoxylate (molecule.C00048).

## Annotation

This reaction is part of the metabolism of glycolate.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7458|complex.ecocyc.CPLX0-7458]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00160|molecule.C00160]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLYCOLATEDEHYDRO-RXN`

## Notes

Acceptor + GLYCOLLATE -> Donor-H2 + GLYOX; direction=PHYSIOL-LEFT-TO-RIGHT
