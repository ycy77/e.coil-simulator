---
entity_id: "reaction.ecocyc.AICARTRANSFORM-RXN"
entity_type: "reaction"
name: "AICARTRANSFORM-RXN"
source_database: "EcoCyc"
source_id: "AICARTRANSFORM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AICARTRANSFORM-RXN

`reaction.ecocyc.AICARTRANSFORM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AICARTRANSFORM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the ninth step in purine biosynthesis EcoCyc reaction equation: FORMYL-THF-GLU-N + AICAR -> THF-GLU-N + PHOSPHORIBOSYL-FORMAMIDO-CARBOXAMIDE; direction=REVERSIBLE. This is the ninth step in purine biosynthesis

## Biological Role

Catalyzed by purH (protein.P15639). Substrates: 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide (molecule.C04677), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: THF-polyglutamate (molecule.C03541), 1-(5'-Phosphoribosyl)-5-formamido-4-imidazolecarboxamide (molecule.C04734).

## Enriched Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Annotation

This is the ninth step in purine biosynthesis

## Pathways

- `ecocyc.PWY-6123` inosine-5'-phosphate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P15639|protein.P15639]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04734|molecule.C04734]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04677|molecule.C04677]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:AICARTRANSFORM-RXN`

## Notes

FORMYL-THF-GLU-N + AICAR -> THF-GLU-N + PHOSPHORIBOSYL-FORMAMIDO-CARBOXAMIDE; direction=REVERSIBLE
