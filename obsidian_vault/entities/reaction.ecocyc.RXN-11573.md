---
entity_id: "reaction.ecocyc.RXN-11573"
entity_type: "reaction"
name: "RXN-11573"
source_database: "EcoCyc"
source_id: "RXN-11573"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (guanine<sup>745</sup>-N<sup>1</sup>)-methyltransferase"
  - "23S rRNA:m<sup>1</sup>G<sup>745</sup> methyltransferase"
  - "RlmAI methyltransferase"
  - "23S rRNA m<sup>1</sup>G<sup>745</sup> methyltransferase"
---

# RXN-11573

`reaction.ecocyc.RXN-11573`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11573`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-745 -> 23S-rRNA-N1-methylguanine745 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-745 -> 23S-rRNA-N1-methylguanine745 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmA (protein.P36999). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine745 in 23S rRNA (molecule.ecocyc.23S-rRNA-guanine-745). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N1-methylguanine745 in 23S rRNA (molecule.ecocyc.23S-rRNA-N1-methylguanine745).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-745 -> 23S-rRNA-N1-methylguanine745 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P36999|protein.P36999]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-N1-methylguanine745|molecule.ecocyc.23S-rRNA-N1-methylguanine745]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-guanine-745|molecule.ecocyc.23S-rRNA-guanine-745]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11573`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-745 -> 23S-rRNA-N1-methylguanine745 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
