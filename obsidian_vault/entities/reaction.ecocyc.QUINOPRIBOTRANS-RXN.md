---
entity_id: "reaction.ecocyc.QUINOPRIBOTRANS-RXN"
entity_type: "reaction"
name: "QUINOPRIBOTRANS-RXN"
source_database: "EcoCyc"
source_id: "QUINOPRIBOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# QUINOPRIBOTRANS-RXN

`reaction.ecocyc.QUINOPRIBOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:QUINOPRIBOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is part of the de novo biosynthesis of NAD and NADP. EcoCyc reaction equation: NICOTINATE_NUCLEOTIDE + PPI + CARBON-DIOXIDE -> PRPP + QUINOLINATE + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT. This reaction is part of the de novo biosynthesis of NAD and NADP.

## Biological Role

Catalyzed by quinolinate phosphoribosyltransferase (decarboxylating) (complex.ecocyc.QUINOPRIBOTRANS-CPLX). Substrates: CO2 (molecule.C00011), Diphosphate (molecule.C00013), Nicotinate D-ribonucleotide (molecule.C01185). Products: H+ (molecule.C00080), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Quinolinate (molecule.C03722).

## Enriched Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Annotation

This reaction is part of the de novo biosynthesis of NAD and NADP.

## Pathways

- `ecocyc.PYRIDNUCSYN-PWY` NAD de novo biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.QUINOPRIBOTRANS-CPLX|complex.ecocyc.QUINOPRIBOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03722|molecule.C03722]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01185|molecule.C01185]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01606|molecule.C01606]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:QUINOPRIBOTRANS-RXN`

## Notes

NICOTINATE_NUCLEOTIDE + PPI + CARBON-DIOXIDE -> PRPP + QUINOLINATE + PROTON; direction=PHYSIOL-RIGHT-TO-LEFT
