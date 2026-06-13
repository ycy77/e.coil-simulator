---
entity_id: "reaction.ecocyc.RXN-12458"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA (guanine37-N1)-methyltransferase"
source_database: "EcoCyc"
source_id: "RXN-12458"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "tRNA-(N1G37) methyltransferase"
  - "transfer RNA (m1G37) methyltransferase"
  - "tRNA (m1G37) methyltransferase"
---

# S-adenosyl-L-methionine:tRNA (guanine37-N1)-methyltransferase

`reaction.ecocyc.RXN-12458`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12458`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Guanine37-in-tRNA -> tRNA-Containing-N1-Methylguanine-37 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Guanine37-in-tRNA -> tRNA-Containing-N1-Methylguanine-37 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA m1G37 methyltransferase (complex.ecocyc.CPLX0-3950). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine37 in tRNA (molecule.ecocyc.Guanine37-in-tRNA). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N1-methylguanine37 in tRNA (molecule.ecocyc.tRNA-Containing-N1-Methylguanine-37).

## Annotation

S-ADENOSYLMETHIONINE + Guanine37-in-tRNA -> tRNA-Containing-N1-Methylguanine-37 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3950|complex.ecocyc.CPLX0-3950]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Containing-N1-Methylguanine-37|molecule.ecocyc.tRNA-Containing-N1-Methylguanine-37]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Guanine37-in-tRNA|molecule.ecocyc.Guanine37-in-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00212|molecule.C00212]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.SINEFUNGIN|molecule.ecocyc.SINEFUNGIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-12458`

## Notes

S-ADENOSYLMETHIONINE + Guanine37-in-tRNA -> tRNA-Containing-N1-Methylguanine-37 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
