---
entity_id: "reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN

`reaction.ecocyc.TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This activity has been observed in E. coli . EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Guanine46-in-tRNA -> tRNA-Containing-N7-Methylguanine-46 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This activity has been observed in E. coli .

## Biological Role

Catalyzed by trmB (protein.P0A8I5). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine46 in tRNA (molecule.ecocyc.Guanine46-in-tRNA). Products: S-Adenosyl-L-homocysteine (molecule.C00021), an N7-methylguanine46 in tRNA (molecule.ecocyc.tRNA-Containing-N7-Methylguanine-46).

## Annotation

This activity has been observed in E. coli .

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A8I5|protein.P0A8I5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Containing-N7-Methylguanine-46|molecule.ecocyc.tRNA-Containing-N7-Methylguanine-46]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Guanine46-in-tRNA|molecule.ecocyc.Guanine46-in-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-GUANINE-N7--METHYLTRANSFERASE-RXN`

## Notes

S-ADENOSYLMETHIONINE + Guanine46-in-tRNA -> tRNA-Containing-N7-Methylguanine-46 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
