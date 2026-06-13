---
entity_id: "reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "METHIONYL-TRNA-FORMYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "METHIONYL-TRNA-FORMYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# METHIONYL-TRNA-FORMYLTRANSFERASE-RXN

`reaction.ecocyc.METHIONYL-TRNA-FORMYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:METHIONYL-TRNA-FORMYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FORMYL-THF-GLU-N + L-methionyl-tRNAfmet -> THF-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: FORMYL-THF-GLU-N + L-methionyl-tRNAfmet -> THF-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fmt (protein.P23882). Substrates: an N10-formyltetrahydrofolate (molecule.ecocyc.FORMYL-THF-GLU-N). Products: H+ (molecule.C00080), THF-polyglutamate (molecule.C03541).

## Annotation

FORMYL-THF-GLU-N + L-methionyl-tRNAfmet -> THF-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P23882|protein.P23882]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.FORMYL-THF-GLU-N|molecule.ecocyc.FORMYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:METHIONYL-TRNA-FORMYLTRANSFERASE-RXN`

## Notes

FORMYL-THF-GLU-N + L-methionyl-tRNAfmet -> THF-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
