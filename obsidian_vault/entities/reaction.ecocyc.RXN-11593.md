---
entity_id: "reaction.ecocyc.RXN-11593"
entity_type: "reaction"
name: "RXN-11593"
source_database: "EcoCyc"
source_id: "RXN-11593"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "RNA m5C methyltransferase YebU"
  - "S-adenosyl-L-methionine:16S rRNA (cytosine<sup>1407</sup>-C<sup>5</sup>)-methyltransferase"
---

# RXN-11593

`reaction.ecocyc.RXN-11593`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11593`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine1407 -> ADENOSYL-HOMO-CYS + 16S-rRNA-5-O-methylcytosine1407 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine1407 -> ADENOSYL-HOMO-CYS + 16S-rRNA-5-O-methylcytosine1407 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsmF (protein.P76273). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytosine1407 in 16S rRNA (molecule.ecocyc.16S-rRNA-cytosine1407). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methylcytosine1407 in 16S rRNA (molecule.ecocyc.16S-rRNA-5-O-methylcytosine1407).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine1407 -> ADENOSYL-HOMO-CYS + 16S-rRNA-5-O-methylcytosine1407 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P76273|protein.P76273]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-5-O-methylcytosine1407|molecule.ecocyc.16S-rRNA-5-O-methylcytosine1407]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-cytosine1407|molecule.ecocyc.16S-rRNA-cytosine1407]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11593`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-cytosine1407 -> ADENOSYL-HOMO-CYS + 16S-rRNA-5-O-methylcytosine1407 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
