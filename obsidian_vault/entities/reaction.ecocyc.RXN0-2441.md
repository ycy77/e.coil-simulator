---
entity_id: "reaction.ecocyc.RXN0-2441"
entity_type: "reaction"
name: "RXN0-2441"
source_database: "EcoCyc"
source_id: "RXN0-2441"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2441

`reaction.ecocyc.RXN0-2441`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2441`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + CPD-225 -> MONOMETHYL-ESTER-OF-TRANS-ACONITATE + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-225 -> MONOMETHYL-ESTER-OF-TRANS-ACONITATE + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tam (protein.P76145). Substrates: S-Adenosyl-L-methionine (molecule.C00019), trans-Aconitate (molecule.C02341). Products: S-Adenosyl-L-homocysteine (molecule.C00021), (E)-3-(methoxycarbonyl)pent-2-enedioate (molecule.ecocyc.MONOMETHYL-ESTER-OF-TRANS-ACONITATE).

## Annotation

S-ADENOSYLMETHIONINE + CPD-225 -> MONOMETHYL-ESTER-OF-TRANS-ACONITATE + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76145|protein.P76145]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MONOMETHYL-ESTER-OF-TRANS-ACONITATE|molecule.ecocyc.MONOMETHYL-ESTER-OF-TRANS-ACONITATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C02341|molecule.C02341]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-2441`

## Notes

S-ADENOSYLMETHIONINE + CPD-225 -> MONOMETHYL-ESTER-OF-TRANS-ACONITATE + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
