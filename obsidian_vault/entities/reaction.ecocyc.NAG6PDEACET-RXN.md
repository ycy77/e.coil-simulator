---
entity_id: "reaction.ecocyc.NAG6PDEACET-RXN"
entity_type: "reaction"
name: "NAG6PDEACET-RXN"
source_database: "EcoCyc"
source_id: "NAG6PDEACET-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NAG6PDEACET-RXN

`reaction.ecocyc.NAG6PDEACET-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NAG6PDEACET-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of N-acetylglucosamine catabolism. EcoCyc reaction equation: N-ACETYL-D-GLUCOSAMINE-6-P + WATER -> D-GLUCOSAMINE-6-P + ACET; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is part of N-acetylglucosamine catabolism.

## Biological Role

Catalyzed by N-acetylglucosamine-6-phosphate deacetylase (complex.ecocyc.NAG6PDEACET-CPLX). Substrates: H2O (molecule.C00001), N-Acetyl-D-glucosamine 6-phosphate (molecule.C00357). Products: Acetate (molecule.C00033), D-Glucosamine 6-phosphate (molecule.C00352).

## Enriched Pathways

- `ecocyc.GLUAMCAT-PWY` N-acetylglucosamine degradation I (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

This reaction is part of N-acetylglucosamine catabolism.

## Pathways

- `ecocyc.GLUAMCAT-PWY` N-acetylglucosamine degradation I (EcoCyc)
- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.NAG6PDEACET-CPLX|complex.ecocyc.NAG6PDEACET-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NAG6PDEACET-RXN`

## Notes

N-ACETYL-D-GLUCOSAMINE-6-P + WATER -> D-GLUCOSAMINE-6-P + ACET; direction=PHYSIOL-LEFT-TO-RIGHT
