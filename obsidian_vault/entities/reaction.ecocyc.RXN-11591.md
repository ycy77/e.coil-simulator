---
entity_id: "reaction.ecocyc.RXN-11591"
entity_type: "reaction"
name: "RXN-11591"
source_database: "EcoCyc"
source_id: "RXN-11591"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "rsmB (gene name)"
  - "S-adenosyl-L-methionine:16S rRNA (cytosine<sup>967</sup>-C<sup>5</sup>)-methyltransferase"
  - "16S rRNA m<sup>5</sup>C<sup>967</sup> methyltransferase"
---

# RXN-11591

`reaction.ecocyc.RXN-11591`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11591`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine967 -> 16S-rRNA-5-O-methylcytosine967 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine967 -> 16S-rRNA-5-O-methylcytosine967 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsmB (protein.P36929). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytosine967 in 16S rRNA (molecule.ecocyc.16S-rRNA-cytosine967). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methylcytosine967 in 16S rRNA (molecule.ecocyc.16S-rRNA-5-O-methylcytosine967).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine967 -> 16S-rRNA-5-O-methylcytosine967 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P36929|protein.P36929]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-5-O-methylcytosine967|molecule.ecocyc.16S-rRNA-5-O-methylcytosine967]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-cytosine967|molecule.ecocyc.16S-rRNA-cytosine967]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11591`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine967 -> 16S-rRNA-5-O-methylcytosine967 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
