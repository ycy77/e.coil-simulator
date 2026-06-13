---
entity_id: "reaction.ecocyc.RXN-11592"
entity_type: "reaction"
name: "RXN-11592"
source_database: "EcoCyc"
source_id: "RXN-11592"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "&psi"
  - "1915-specific methyltransferase"
  - "m3 &psi"
  - "methyltransferase"
  - "S-adenosyl-L-methionine:23S rRNA (pseudouridine<sup>1915</sup>-N<sup>3</sup>)-methyltransferase"
---

# RXN-11592

`reaction.ecocyc.RXN-11592`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11592`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-pseudouridine1915 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N3-methylpseudouridine1915 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-pseudouridine1915 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N3-methylpseudouridine1915 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 23S rRNA m3Ψ1915 methyltransferase (complex.ecocyc.CPLX0-7423). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a pseudouridine1915 in 23S rRNA (molecule.ecocyc.23S-rRNA-pseudouridine1915). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N3-methylpseudouridine1915 in 23S rRNA (molecule.ecocyc.23S-rRNA-N3-methylpseudouridine1915).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-pseudouridine1915 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N3-methylpseudouridine1915 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7423|complex.ecocyc.CPLX0-7423]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-N3-methylpseudouridine1915|molecule.ecocyc.23S-rRNA-N3-methylpseudouridine1915]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-pseudouridine1915|molecule.ecocyc.23S-rRNA-pseudouridine1915]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11592`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-pseudouridine1915 -> ADENOSYL-HOMO-CYS + 23S-rRNA-N3-methylpseudouridine1915 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
