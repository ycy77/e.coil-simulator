---
entity_id: "reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN"
entity_type: "reaction"
name: "METHENYLTHFCYCLOHYDRO-RXN"
source_database: "EcoCyc"
source_id: "METHENYLTHFCYCLOHYDRO-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHENYLTHFCYCLOHYDRO-RXN

`reaction.ecocyc.METHENYLTHFCYCLOHYDRO-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHENYLTHFCYCLOHYDRO-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is involved in folic acid synthesis and is necessary for the biosynthesis of purines, thymydylate, methionine, histidine, pantothenate and formyl tRNA-MET. EcoCyc reaction equation: 5-10-METHENYL-THF-GLU-N + WATER -> FORMYL-THF-GLU-N + PROTON; direction=REVERSIBLE. This reaction is involved in folic acid synthesis and is necessary for the biosynthesis of purines, thymydylate, methionine, histidine, pantothenate and formyl tRNA-MET.

## Biological Role

Catalyzed by bifunctional methylenetetrahydrofolate dehydrogenase / methenyltetrahydrofolate cyclohydrolase (complex.ecocyc.FOLD-CPLX). Substrates: H2O (molecule.C00001), a 5,10-methenyltetrahydrofolate (molecule.ecocyc.5-10-METHENYL-THF-GLU-N). Products: H+ (molecule.C00080), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Annotation

This reaction is involved in folic acid synthesis and is necessary for the biosynthesis of purines, thymydylate, methionine, histidine, pantothenate and formyl tRNA-MET.

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.FOLD-CPLX|complex.ecocyc.FOLD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-10-METHENYL-THF-GLU-N|molecule.ecocyc.5-10-METHENYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00234|molecule.C00234]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2685|molecule.ecocyc.CPD0-2685]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:METHENYLTHFCYCLOHYDRO-RXN`

## Notes

5-10-METHENYL-THF-GLU-N + WATER -> FORMYL-THF-GLU-N + PROTON; direction=REVERSIBLE
