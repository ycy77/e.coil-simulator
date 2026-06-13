---
entity_id: "reaction.ecocyc.RXN-11596"
entity_type: "reaction"
name: "RXN-11596"
source_database: "EcoCyc"
source_id: "RXN-11596"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "m<sup>6</sup>A1618 methyltransferase"
  - "rlmF (gene name)"
  - "S-adenosyl-L-methionine:23S rRNA (adenine<sup>1618</sup>-N<sup>6</sup>)-methyltransferase"
---

# RXN-11596

`reaction.ecocyc.RXN-11596`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11596`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-1618 -> 23S-rRNA-N6-m-adenine1618 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-1618 -> 23S-rRNA-N6-m-adenine1618 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmF (protein.P75782). Substrates: S-Adenosyl-L-methionine (molecule.C00019), adenine1618 in 23S rRNA (molecule.ecocyc.23S-rRNA-adenine-1618). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N6-methyladenine1618 in 23S rRNA (molecule.ecocyc.23S-rRNA-N6-m-adenine1618).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-1618 -> 23S-rRNA-N6-m-adenine1618 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P75782|protein.P75782]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-N6-m-adenine1618|molecule.ecocyc.23S-rRNA-N6-m-adenine1618]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-adenine-1618|molecule.ecocyc.23S-rRNA-adenine-1618]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11596`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-adenine-1618 -> 23S-rRNA-N6-m-adenine1618 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
