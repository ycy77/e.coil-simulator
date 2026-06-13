---
entity_id: "reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN

`reaction.ecocyc.HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + HOMO-CYS -> PROTON + MET + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + HOMO-CYS -> PROTON + MET + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: S-Adenosyl-L-methionine (molecule.C00019), L-Homocysteine (molecule.C00155). Products: S-Adenosyl-L-homocysteine (molecule.C00021), L-Methionine (molecule.C00073), H+ (molecule.C00080).

## Annotation

S-ADENOSYLMETHIONINE + HOMO-CYS -> PROTON + MET + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00155|molecule.C00155]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:HOMOCYSTEINE-S-METHYLTRANSFERASE-RXN`

## Notes

S-ADENOSYLMETHIONINE + HOMO-CYS -> PROTON + MET + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
