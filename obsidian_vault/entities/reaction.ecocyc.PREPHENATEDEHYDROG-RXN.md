---
entity_id: "reaction.ecocyc.PREPHENATEDEHYDROG-RXN"
entity_type: "reaction"
name: "PREPHENATEDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "PREPHENATEDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PREPHENATEDEHYDROG-RXN

`reaction.ecocyc.PREPHENATEDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PREPHENATEDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PREPHENATE + NAD -> P-HYDROXY-PHENYLPYRUVATE + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PREPHENATE + NAD -> P-HYDROXY-PHENYLPYRUVATE + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fused chorismate mutase/prephenate dehydrogenase (complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX). Substrates: NAD+ (molecule.C00003), Prephenate (molecule.C00254). Products: NADH (molecule.C00004), CO2 (molecule.C00011), 3-(4-Hydroxyphenyl)pyruvate (molecule.C01179).

## Enriched Pathways

- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Annotation

PREPHENATE + NAD -> P-HYDROXY-PHENYLPYRUVATE + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.TYRSYN` L-tyrosine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX|complex.ecocyc.CHORISMUTPREPHENDEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01179|molecule.C01179]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00254|molecule.C00254]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00082|molecule.C00082]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PREPHENATEDEHYDROG-RXN`

## Notes

PREPHENATE + NAD -> P-HYDROXY-PHENYLPYRUVATE + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT
