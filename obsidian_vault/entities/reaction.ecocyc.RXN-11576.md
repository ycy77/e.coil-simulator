---
entity_id: "reaction.ecocyc.RXN-11576"
entity_type: "reaction"
name: "RXN-11576"
source_database: "EcoCyc"
source_id: "RXN-11576"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:16S rRNA (guanine<sup>1207</sup>-N<sup>2</sup>)-methyltransferase"
  - "m<sup>2</sup>G1207 methyltransferase"
---

# RXN-11576

`reaction.ecocyc.RXN-11576`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11576`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-1207 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine1207 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-1207 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine1207 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsmC (protein.P39406). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine1207 in 16S rRNA (molecule.ecocyc.16S-rRNA-guanine-1207). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N2-methylguanine1207 in 16S rRNA (molecule.ecocyc.16S-rRNA-N2-methylguanine1207).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-1207 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine1207 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P39406|protein.P39406]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N2-methylguanine1207|molecule.ecocyc.16S-rRNA-N2-methylguanine1207]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-guanine-1207|molecule.ecocyc.16S-rRNA-guanine-1207]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11576`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-1207 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N2-methylguanine1207 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
