---
entity_id: "reaction.ecocyc.RXN-6321"
entity_type: "reaction"
name: "RXN-6321"
source_database: "EcoCyc"
source_id: "RXN-6321"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-6321

`reaction.ecocyc.RXN-6321`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-6321`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-10-METHENYL-THF-GLU-N + WATER -> N5-Formyl-THF-Glu-N + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-10-METHENYL-THF-GLU-N + WATER -> N5-Formyl-THF-Glu-N + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by serine hydroxymethyltransferase (complex.ecocyc.GLYOHMETRANS-CPLX). Substrates: H2O (molecule.C00001), a 5,10-methenyltetrahydrofolate (molecule.ecocyc.5-10-METHENYL-THF-GLU-N). Products: H+ (molecule.C00080), a (6S)-5-formyltetrahydrofolate (molecule.ecocyc.N5-Formyl-THF-Glu-N).

## Annotation

5-10-METHENYL-THF-GLU-N + WATER -> N5-Formyl-THF-Glu-N + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.GLYOHMETRANS-CPLX|complex.ecocyc.GLYOHMETRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.N5-Formyl-THF-Glu-N|molecule.ecocyc.N5-Formyl-THF-Glu-N]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-10-METHENYL-THF-GLU-N|molecule.ecocyc.5-10-METHENYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-6321`

## Notes

5-10-METHENYL-THF-GLU-N + WATER -> N5-Formyl-THF-Glu-N + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
