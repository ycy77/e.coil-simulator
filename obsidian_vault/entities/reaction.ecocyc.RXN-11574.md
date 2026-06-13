---
entity_id: "reaction.ecocyc.RXN-11574"
entity_type: "reaction"
name: "RXN-11574"
source_database: "EcoCyc"
source_id: "RXN-11574"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (guanine<sup>2445</sup>-N<sup>2</sup>)-methyltransferase"
  - "rlmL (gene name)"
  - "ycbY (gene name)"
---

# RXN-11574

`reaction.ecocyc.RXN-11574`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11574`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2445 -> ADENOSYL-HOMO-CYS + 23S-RRNA-N2-METHYLGUANINE2445 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2445 -> ADENOSYL-HOMO-CYS + 23S-RRNA-N2-METHYLGUANINE2445 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmL (protein.P75864). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine2445 in 23S rRNA (molecule.ecocyc.23S-rRNA-guanine-2445). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N2-methylguanine2445 in 23S rRNA (molecule.ecocyc.23S-RRNA-N2-METHYLGUANINE2445).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2445 -> ADENOSYL-HOMO-CYS + 23S-RRNA-N2-METHYLGUANINE2445 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75864|protein.P75864]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-RRNA-N2-METHYLGUANINE2445|molecule.ecocyc.23S-RRNA-N2-METHYLGUANINE2445]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-guanine-2445|molecule.ecocyc.23S-rRNA-guanine-2445]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11574`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2445 -> ADENOSYL-HOMO-CYS + 23S-RRNA-N2-METHYLGUANINE2445 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
