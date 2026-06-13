---
entity_id: "reaction.ecocyc.RXN-11578"
entity_type: "reaction"
name: "RXN-11578"
source_database: "EcoCyc"
source_id: "RXN-11578"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:16S rRNA (guanine<sup>527</sup>-N<sup>7</sup>)-methyltransferase"
  - "rsmG (gene name)"
---

# RXN-11578

`reaction.ecocyc.RXN-11578`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11578`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The enzyme specifically methylates guanine527 at N7 in 16S rRNA. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-527 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N7-methylguanine527; direction=PHYSIOL-LEFT-TO-RIGHT. The enzyme specifically methylates guanine527 at N7 in 16S rRNA.

## Biological Role

Catalyzed by rsmG (protein.P0A6U5). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine527 in 16S rRNA (molecule.ecocyc.16S-rRNA-guanine-527). Products: S-Adenosyl-L-homocysteine (molecule.C00021), an N7-methylguanine527 in 16S rRNA (molecule.ecocyc.16S-rRNA-N7-methylguanine527).

## Annotation

The enzyme specifically methylates guanine527 at N7 in 16S rRNA.

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6U5|protein.P0A6U5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N7-methylguanine527|molecule.ecocyc.16S-rRNA-N7-methylguanine527]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-guanine-527|molecule.ecocyc.16S-rRNA-guanine-527]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11578`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine-527 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N7-methylguanine527; direction=PHYSIOL-LEFT-TO-RIGHT
