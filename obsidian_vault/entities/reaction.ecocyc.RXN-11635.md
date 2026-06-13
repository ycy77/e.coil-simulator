---
entity_id: "reaction.ecocyc.RXN-11635"
entity_type: "reaction"
name: "RXN-11635"
source_database: "EcoCyc"
source_id: "RXN-11635"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (guanine<sup>1835</sup>-N<sup>2</sup>)-methyltransferase"
  - "rlmG  (gene name)"
  - "ygjO (gene name)"
---

# RXN-11635

`reaction.ecocyc.RXN-11635`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11635`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-1835 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N2-methylguanine1835 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-1835 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N2-methylguanine1835 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmG (protein.P42596). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine1835 in 23S rRNA (molecule.ecocyc.23S-rRNA-guanine-1835). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N2-methylguanine1835 in 23S rRNA (molecule.ecocyc.23S-rRNA-N2-methylguanine1835).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-1835 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N2-methylguanine1835 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P42596|protein.P42596]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-N2-methylguanine1835|molecule.ecocyc.23S-rRNA-N2-methylguanine1835]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-guanine-1835|molecule.ecocyc.23S-rRNA-guanine-1835]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11635`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-1835 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N2-methylguanine1835 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
