---
entity_id: "reaction.ecocyc.RXN-11601"
entity_type: "reaction"
name: "RXN-11601"
source_database: "EcoCyc"
source_id: "RXN-11601"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (uracil<sup>1939</sup>-C<sup>5</sup>)-methyltransferase"
---

# RXN-11601

`reaction.ecocyc.RXN-11601`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11601`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-1939 -> 23S-rRNA-5-methyluracil1939 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-1939 -> 23S-rRNA-5-methyluracil1939 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmD (protein.P55135). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uracil1939 in 23S rRNA (molecule.ecocyc.23S-rRNA-uracil-1939). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methyluracil1939 in 23S rRNA (molecule.ecocyc.23S-rRNA-5-methyluracil1939).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-1939 -> 23S-rRNA-5-methyluracil1939 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P55135|protein.P55135]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-5-methyluracil1939|molecule.ecocyc.23S-rRNA-5-methyluracil1939]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uracil-1939|molecule.ecocyc.23S-rRNA-uracil-1939]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11601`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-1939 -> 23S-rRNA-5-methyluracil1939 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
