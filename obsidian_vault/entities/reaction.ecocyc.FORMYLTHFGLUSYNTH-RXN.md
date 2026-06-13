---
entity_id: "reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN"
entity_type: "reaction"
name: "FORMYLTHFGLUSYNTH-RXN"
source_database: "EcoCyc"
source_id: "FORMYLTHFGLUSYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FORMYLTHFGLUSYNTH-RXN

`reaction.ecocyc.FORMYLTHFGLUSYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FORMYLTHFGLUSYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is the same as the folC 6.3.2.17 activity, but using an alternative substrate. EcoCyc reaction equation: FORMYL-THF-GLU-N + GLT + ATP -> FORMYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is the same as the folC 6.3.2.17 activity, but using an alternative substrate.

## Biological Role

Catalyzed by folC (protein.P08192). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: ADP (molecule.C00008), an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Annotation

This reaction is the same as the folC 6.3.2.17 activity, but using an alternative substrate.

## Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P08192|protein.P08192]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FORMYLTHFGLUSYNTH-RXN`

## Notes

FORMYL-THF-GLU-N + GLT + ATP -> FORMYL-THF-GLU-N + ADP + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
