---
entity_id: "reaction.ecocyc.GART-RXN"
entity_type: "reaction"
name: "GART-RXN"
source_database: "EcoCyc"
source_id: "GART-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GART-RXN

`reaction.ecocyc.GART-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GART-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step (first of two transformylation reactions) in de novo purine biosynthesis EcoCyc reaction equation: FORMYL-THF-GLU-N + 5-PHOSPHO-RIBOSYL-GLYCINEAMIDE -> THF-GLU-N + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + PROTON; direction=REVERSIBLE. This is the third step (first of two transformylation reactions) in de novo purine biosynthesis

## Biological Role

Catalyzed by purN (protein.P08179). Substrates: 5'-Phosphoribosylglycinamide (molecule.C03838), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: H+ (molecule.C00080), THF-polyglutamate (molecule.C03541), 5'-Phosphoribosyl-N-formylglycinamide (molecule.C04376).

## Enriched Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)

## Annotation

This is the third step (first of two transformylation reactions) in de novo purine biosynthesis

## Pathways

- `ecocyc.PWY-6121` 5-aminoimidazole ribonucleotide biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P08179|protein.P08179]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04376|molecule.C04376]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03838|molecule.C03838]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1574|molecule.ecocyc.CPD0-1574]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1575|molecule.ecocyc.CPD0-1575]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1576|molecule.ecocyc.CPD0-1576]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GART-RXN`

## Notes

FORMYL-THF-GLU-N + 5-PHOSPHO-RIBOSYL-GLYCINEAMIDE -> THF-GLU-N + 5-P-RIBOSYL-N-FORMYLGLYCINEAMIDE + PROTON; direction=REVERSIBLE
