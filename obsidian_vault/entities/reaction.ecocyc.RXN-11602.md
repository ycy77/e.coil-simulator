---
entity_id: "reaction.ecocyc.RXN-11602"
entity_type: "reaction"
name: "RXN-11602"
source_database: "EcoCyc"
source_id: "RXN-11602"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (cytosine<sup>1962</sup>-C<sup>5</sup>)-methyltransferase"
---

# RXN-11602

`reaction.ecocyc.RXN-11602`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11602`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-cytosine-1962 -> 23S-rRNA-5-methylcytosine1962 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-cytosine-1962 -> 23S-rRNA-5-methylcytosine1962 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 23S rRNA m5C1962 methyltransferase (complex.ecocyc.CPLX0-7726). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a cytosine1962 in 23S rRNA (molecule.ecocyc.23S-rRNA-cytosine-1962). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methylcytosine1962 in 23S rRNA (molecule.ecocyc.23S-rRNA-5-methylcytosine1962).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-cytosine-1962 -> 23S-rRNA-5-methylcytosine1962 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7726|complex.ecocyc.CPLX0-7726]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-5-methylcytosine1962|molecule.ecocyc.23S-rRNA-5-methylcytosine1962]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-cytosine-1962|molecule.ecocyc.23S-rRNA-cytosine-1962]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11602`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-cytosine-1962 -> 23S-rRNA-5-methylcytosine1962 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
