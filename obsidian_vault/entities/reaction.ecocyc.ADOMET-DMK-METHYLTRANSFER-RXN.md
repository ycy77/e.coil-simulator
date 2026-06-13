---
entity_id: "reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN"
entity_type: "reaction"
name: "ADOMET-DMK-METHYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "ADOMET-DMK-METHYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ADOMET-DMK-METHYLTRANSFER-RXN

`reaction.ecocyc.ADOMET-DMK-METHYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ADOMET-DMK-METHYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh and final reaction in menaquinone biosynthesis. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + CPD-12115 -> REDUCED-MENAQUINONE + PROTON + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This is the seventh and final reaction in menaquinone biosynthesis.

## Biological Role

Catalyzed by ubiE (protein.P0A887). Substrates: S-Adenosyl-L-methionine (molecule.C00019), demethylmenaquinol-8 (molecule.ecocyc.CPD-12115). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), menaquinol-8 (molecule.ecocyc.REDUCED-MENAQUINONE).

## Enriched Pathways

- `ecocyc.MENAQUINONESYN-PWY` menaquinol-8 biosynthesis (EcoCyc)

## Annotation

This is the seventh and final reaction in menaquinone biosynthesis.

## Pathways

- `ecocyc.MENAQUINONESYN-PWY` menaquinol-8 biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A887|protein.P0A887]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.REDUCED-MENAQUINONE|molecule.ecocyc.REDUCED-MENAQUINONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-12115|molecule.ecocyc.CPD-12115]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ADOMET-DMK-METHYLTRANSFER-RXN`

## Notes

S-ADENOSYLMETHIONINE + CPD-12115 -> REDUCED-MENAQUINONE + PROTON + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
