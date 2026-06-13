---
entity_id: "reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN"
entity_type: "reaction"
name: "GLUCOSAMINE-6-P-DEAMIN-RXN"
source_database: "EcoCyc"
source_id: "GLUCOSAMINE-6-P-DEAMIN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUCOSAMINE-6-P-DEAMIN-RXN

`reaction.ecocyc.GLUCOSAMINE-6-P-DEAMIN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUCOSAMINE-6-P-DEAMIN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in the catabolism of acetyl-glucosamine-6-phosphate and glucosamine-6-phosphate. EcoCyc reaction equation: CPD-13469 + WATER -> AMMONIUM + FRUCTOSE-6P; direction=REVERSIBLE. This is a reaction in the catabolism of acetyl-glucosamine-6-phosphate and glucosamine-6-phosphate.

## Biological Role

Catalyzed by glucosamine-6-phosphate deaminase (complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX). Substrates: H2O (molecule.C00001), D-Glucosamine 6-phosphate (molecule.C00352). Products: ammonium (molecule.ecocyc.AMMONIUM), β-D-fructofuranose 6-phosphate (molecule.ecocyc.FRUCTOSE-6P).

## Enriched Pathways

- `ecocyc.GLUAMCAT-PWY` N-acetylglucosamine degradation I (EcoCyc)

## Annotation

This is a reaction in the catabolism of acetyl-glucosamine-6-phosphate and glucosamine-6-phosphate.

## Pathways

- `ecocyc.GLUAMCAT-PWY` N-acetylglucosamine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.C00357|molecule.C00357]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0A761|protein.P0A761]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0A9Z1|protein.P0A9Z1]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX|complex.ecocyc.GLUCOSAMINE-6-P-DEAMIN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FRUCTOSE-6P|molecule.ecocyc.FRUCTOSE-6P]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00352|molecule.C00352]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-9051|molecule.ecocyc.CPD-9051]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUCOSAMINE-6-P-DEAMIN-RXN`

## Notes

CPD-13469 + WATER -> AMMONIUM + FRUCTOSE-6P; direction=REVERSIBLE
