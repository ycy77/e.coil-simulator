---
entity_id: "reaction.ecocyc.RXN-12480"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA1Val (adenine37-N6)-methyltransferase"
source_database: "EcoCyc"
source_id: "RXN-12480"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# S-adenosyl-L-methionine:tRNA1Val (adenine37-N6)-methyltransferase

`reaction.ecocyc.RXN-12480`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12480`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Val-tRNA1-Adenine37 -> ADENOSYL-HOMO-CYS + Val-tRNA1-N6-MeAdenine37 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Val-tRNA1-Adenine37 -> ADENOSYL-HOMO-CYS + Val-tRNA1-N6-MeAdenine37 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by yfiC (protein.P31825). Substrates: S-Adenosyl-L-methionine (molecule.C00019), adenine37 in tRNA1val (molecule.ecocyc.Val-tRNA1-Adenine37). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N6-methyladenine37 in tRNA1val (molecule.ecocyc.Val-tRNA1-N6-MeAdenine37).

## Annotation

S-ADENOSYLMETHIONINE + Val-tRNA1-Adenine37 -> ADENOSYL-HOMO-CYS + Val-tRNA1-N6-MeAdenine37 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P31825|protein.P31825]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Val-tRNA1-N6-MeAdenine37|molecule.ecocyc.Val-tRNA1-N6-MeAdenine37]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Val-tRNA1-Adenine37|molecule.ecocyc.Val-tRNA1-Adenine37]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12480`

## Notes

S-ADENOSYLMETHIONINE + Val-tRNA1-Adenine37 -> ADENOSYL-HOMO-CYS + Val-tRNA1-N6-MeAdenine37 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
