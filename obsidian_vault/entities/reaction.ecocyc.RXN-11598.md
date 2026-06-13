---
entity_id: "reaction.ecocyc.RXN-11598"
entity_type: "reaction"
name: "RXN-11598"
source_database: "EcoCyc"
source_id: "RXN-11598"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "m3U1498 specific methyltransferase"
  - "S-adenosyl-L-methionine:16S rRNA (uracil<sup>1498</sup>-N<sup>3</sup>)-methyltransferase"
---

# RXN-11598

`reaction.ecocyc.RXN-11598`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11598`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-uracil1498 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N3-methyluracil1498 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-uracil1498 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N3-methyluracil1498 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 16S rRNA m3U1498 methyltransferase (complex.ecocyc.CPLX0-7727). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uracil1498 in 16S rRNA (molecule.ecocyc.16S-rRNA-uracil1498). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N3-methyluracil1498 in 16S rRNA (molecule.ecocyc.16S-rRNA-N3-methyluracil1498).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-uracil1498 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N3-methyluracil1498 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7727|complex.ecocyc.CPLX0-7727]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N3-methyluracil1498|molecule.ecocyc.16S-rRNA-N3-methyluracil1498]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-uracil1498|molecule.ecocyc.16S-rRNA-uracil1498]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11598`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-uracil1498 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N3-methyluracil1498 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
