---
entity_id: "reaction.ecocyc.RXN-21539"
entity_type: "reaction"
name: "RXN-21539"
source_database: "EcoCyc"
source_id: "RXN-21539"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21539

`reaction.ecocyc.RXN-21539`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21539`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-METHYL-THF-GLU-N + Methionine-synthase-cob-I-alamins + PROTON -> THF-GLU-N + METHIONINE-SYNTHASE-METHYLCOBALAMIN; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 5-METHYL-THF-GLU-N + Methionine-synthase-cob-I-alamins + PROTON -> THF-GLU-N + METHIONINE-SYNTHASE-METHYLCOBALAMIN; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080), a 5-methyltetrahydrofolate (molecule.ecocyc.5-METHYL-THF-GLU-N), cob(I)alamin-[methionine synthase] (molecule.ecocyc.Methionine-synthase-cob-I-alamins). Products: THF-polyglutamate (molecule.C03541), [Methionine synthase]-methylcob(III)alamin (molecule.C06410).

## Annotation

5-METHYL-THF-GLU-N + Methionine-synthase-cob-I-alamins + PROTON -> THF-GLU-N + METHIONINE-SYNTHASE-METHYLCOBALAMIN; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C03541|molecule.C03541]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C06410|molecule.C06410]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-METHYL-THF-GLU-N|molecule.ecocyc.5-METHYL-THF-GLU-N]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Methionine-synthase-cob-I-alamins|molecule.ecocyc.Methionine-synthase-cob-I-alamins]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21539`

## Notes

5-METHYL-THF-GLU-N + Methionine-synthase-cob-I-alamins + PROTON -> THF-GLU-N + METHIONINE-SYNTHASE-METHYLCOBALAMIN; direction=PHYSIOL-LEFT-TO-RIGHT
