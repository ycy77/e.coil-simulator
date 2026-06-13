---
entity_id: "reaction.ecocyc.RXN-11600"
entity_type: "reaction"
name: "RXN-11600"
source_database: "EcoCyc"
source_id: "RXN-11600"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (uracil<sup>747</sup>-C<sup>5</sup>)-methyltransferase"
---

# RXN-11600

`reaction.ecocyc.RXN-11600`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11600`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-747 -> 23S-rRNA-5-methyluracil747 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-747 -> 23S-rRNA-5-methyluracil747 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmC (protein.P75817). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uracil747 in 23S rRNA (molecule.ecocyc.23S-rRNA-uracil-747). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methyluracil747 in 23S rRNA (molecule.ecocyc.23S-rRNA-5-methyluracil747).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-747 -> 23S-rRNA-5-methyluracil747 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75817|protein.P75817]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-5-methyluracil747|molecule.ecocyc.23S-rRNA-5-methyluracil747]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uracil-747|molecule.ecocyc.23S-rRNA-uracil-747]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11600`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-uracil-747 -> 23S-rRNA-5-methyluracil747 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
