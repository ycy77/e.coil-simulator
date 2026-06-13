---
entity_id: "reaction.ecocyc.RXN0-7422"
entity_type: "reaction"
name: "RXN0-7422"
source_database: "EcoCyc"
source_id: "RXN0-7422"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7422

`reaction.ecocyc.RXN0-7422`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7422`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

10-FORMYL-DIHYDROFOLATE-GLU-N + L-methionyl-tRNAfmet -> DIHYDROFOLATE-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 10-FORMYL-DIHYDROFOLATE-GLU-N + L-methionyl-tRNAfmet -> DIHYDROFOLATE-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by fmt (protein.P23882). Substrates: an N10-formyl-7,8-dihydrofolate (molecule.ecocyc.10-FORMYL-DIHYDROFOLATE-GLU-N). Products: H+ (molecule.C00080), a 7,8-dihydrofolate (molecule.ecocyc.DIHYDROFOLATE-GLU-N).

## Annotation

10-FORMYL-DIHYDROFOLATE-GLU-N + L-methionyl-tRNAfmet -> DIHYDROFOLATE-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P23882|protein.P23882]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.DIHYDROFOLATE-GLU-N|molecule.ecocyc.DIHYDROFOLATE-GLU-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.10-FORMYL-DIHYDROFOLATE-GLU-N|molecule.ecocyc.10-FORMYL-DIHYDROFOLATE-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7422`

## Notes

10-FORMYL-DIHYDROFOLATE-GLU-N + L-methionyl-tRNAfmet -> DIHYDROFOLATE-GLU-N + N-formyl-L-methionyl-tRNAfmet + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
