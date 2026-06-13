---
entity_id: "reaction.ecocyc.RXN-11638"
entity_type: "reaction"
name: "RXN-11638"
source_database: "EcoCyc"
source_id: "RXN-11638"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:16S rRNA (cytosine<sup>1402</sup>-N<sup>4</sup>)-methyltransferase"
---

# RXN-11638

`reaction.ecocyc.RXN-11638`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11638`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-cytidine1402 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N4-methylcytidine1402 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-cytidine1402 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N4-methylcytidine1402 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 16S rRNA m4C1402 methyltransferase (complex.ecocyc.CPLX0-7977). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytidine1402 in 16S rRNA (molecule.ecocyc.16S-rRNA-cytidine1402). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N4-methylcytidine1402 in 16S rRNA (molecule.ecocyc.16S-rRNA-N4-methylcytidine1402).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-cytidine1402 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N4-methylcytidine1402 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7977|complex.ecocyc.CPLX0-7977]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N4-methylcytidine1402|molecule.ecocyc.16S-rRNA-N4-methylcytidine1402]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-cytidine1402|molecule.ecocyc.16S-rRNA-cytidine1402]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11638`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-cytidine1402 -> ADENOSYL-HOMO-CYS + 16S-rRNA-N4-methylcytidine1402 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
