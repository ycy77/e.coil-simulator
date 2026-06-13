---
entity_id: "reaction.ecocyc.RXN0-2921"
entity_type: "reaction"
name: "RXN0-2921"
source_database: "EcoCyc"
source_id: "RXN0-2921"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2921

`reaction.ecocyc.RXN0-2921`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2921`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

METHYLENE-THF-GLU-N + GLT + ATP -> METHYLENE-THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: METHYLENE-THF-GLU-N + GLT + ATP -> METHYLENE-THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by folC (protein.P08192). Substrates: ATP (molecule.C00002), L-Glutamate (molecule.C00025), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N). Products: ADP (molecule.C00008), a 5,10-methylenetetrahydrofolate (molecule.ecocyc.METHYLENE-THF-GLU-N), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Annotation

METHYLENE-THF-GLU-N + GLT + ATP -> METHYLENE-THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-2161` folate polyglutamylation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P08192|protein.P08192]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.METHYLENE-THF-GLU-N|molecule.ecocyc.METHYLENE-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2921`

## Notes

METHYLENE-THF-GLU-N + GLT + ATP -> METHYLENE-THF-GLU-N + Pi + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
