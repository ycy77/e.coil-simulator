---
entity_id: "reaction.ecocyc.5-FORMYL-THF-CYCLO-LIGASE-RXN"
entity_type: "reaction"
name: "5-FORMYL-THF-CYCLO-LIGASE-RXN"
source_database: "EcoCyc"
source_id: "5-FORMYL-THF-CYCLO-LIGASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "Methenyl-THF synthetase"
  - "5-Formyltetrahydrofolate cyclodehydrase"
---

# 5-FORMYL-THF-CYCLO-LIGASE-RXN

`reaction.ecocyc.5-FORMYL-THF-CYCLO-LIGASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:5-FORMYL-THF-CYCLO-LIGASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

N5-Formyl-THF-Glu-N + ATP -> 5-10-METHENYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: N5-Formyl-THF-Glu-N + ATP -> 5-10-METHENYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ygfA (protein.P0AC28). Substrates: ATP (molecule.C00002), a (6S)-5-formyltetrahydrofolate (molecule.ecocyc.N5-Formyl-THF-Glu-N). Products: ADP (molecule.C00008), a 5,10-methenyltetrahydrofolate (molecule.ecocyc.5-10-METHENYL-THF-GLU-N), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Annotation

N5-Formyl-THF-Glu-N + ATP -> 5-10-METHENYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.1CMET2-PWY` folate transformations III (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0AC28|protein.P0AC28]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-10-METHENYL-THF-GLU-N|molecule.ecocyc.5-10-METHENYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.N5-Formyl-THF-Glu-N|molecule.ecocyc.N5-Formyl-THF-Glu-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:5-FORMYL-THF-CYCLO-LIGASE-RXN`

## Notes

N5-Formyl-THF-Glu-N + ATP -> 5-10-METHENYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
