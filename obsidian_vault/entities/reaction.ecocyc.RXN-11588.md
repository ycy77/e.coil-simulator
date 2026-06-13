---
entity_id: "reaction.ecocyc.RXN-11588"
entity_type: "reaction"
name: "RXN-11588"
source_database: "EcoCyc"
source_id: "RXN-11588"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "yifH (gene name)"
  - "rlmB (gene name)"
  - "S-adenosyl-L-methionine:23S rRNA (guanosine<sup>2251</sup>-2-<i>O</i>)-methyltransferase"
---

# RXN-11588

`reaction.ecocyc.RXN-11588`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11588`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2551 -> 23S-rRNA-2-O-methylguanosine2251 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2551 -> 23S-rRNA-2-O-methylguanosine2251 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 23S rRNA 2'-O-ribose G2251 methyltransferase (complex.ecocyc.CPLX0-1121). Substrates: S-Adenosyl-L-methionine (molecule.C00019), guanosine2251 in 23S rRNA (molecule.ecocyc.23S-rRNA-guanine-2551). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), 2-O-methylguanosine2251 in 23S rRNA (molecule.ecocyc.23S-rRNA-2-O-methylguanosine2251).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2551 -> 23S-rRNA-2-O-methylguanosine2251 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1121|complex.ecocyc.CPLX0-1121]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-2-O-methylguanosine2251|molecule.ecocyc.23S-rRNA-2-O-methylguanosine2251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-guanine-2551|molecule.ecocyc.23S-rRNA-guanine-2551]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11588`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-guanine-2551 -> 23S-rRNA-2-O-methylguanosine2251 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
