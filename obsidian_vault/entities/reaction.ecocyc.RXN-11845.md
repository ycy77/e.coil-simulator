---
entity_id: "reaction.ecocyc.RXN-11845"
entity_type: "reaction"
name: "RXN-11845"
source_database: "EcoCyc"
source_id: "RXN-11845"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "S-adenosyl-L-methionine:23S rRNA (uridine<sup>2552</sup>-2-O-)-methyltransferase"
---

# RXN-11845

`reaction.ecocyc.RXN-11845`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11845`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 23S-rRNA-uridine-2552 -> 23S-rRNA-2-O-methyluridine2552 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 23S-rRNA-uridine-2552 -> 23S-rRNA-2-O-methyluridine2552 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rlmE (protein.P0C0R7). Substrates: S-Adenosyl-L-methionine (molecule.C00019), uridine2552 in 23S rRNA (molecule.ecocyc.23S-rRNA-uridine-2552). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 2'-O-methyluridine2552 in 23S rRNA (molecule.ecocyc.23S-rRNA-2-O-methyluridine2552).

## Annotation

S-ADENOSYLMETHIONINE + 23S-rRNA-uridine-2552 -> 23S-rRNA-2-O-methyluridine2552 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0C0R7|protein.P0C0R7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.23S-rRNA-2-O-methyluridine2552|molecule.ecocyc.23S-rRNA-2-O-methyluridine2552]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.23S-rRNA-uridine-2552|molecule.ecocyc.23S-rRNA-uridine-2552]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11845`

## Notes

S-ADENOSYLMETHIONINE + 23S-rRNA-uridine-2552 -> 23S-rRNA-2-O-methyluridine2552 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
