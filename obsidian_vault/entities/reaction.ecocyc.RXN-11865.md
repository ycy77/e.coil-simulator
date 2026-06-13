---
entity_id: "reaction.ecocyc.RXN-11865"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase"
source_database: "EcoCyc"
source_id: "RXN-11865"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "tRNA (cytidine34/5-carboxymethylaminomethyluridine<sup>34-</sup>2'-<i>O</i>)-methyltransferase"
  - "methyltransferase yibK"
  - "YibK (gene name)"
---

# S-adenosyl-L-methionine:tRNA (cytidine34/5-carboxymethylaminomethyluridine34-2'-O)-methyltransferase

`reaction.ecocyc.RXN-11865`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11865`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 5-carbo-me-ami-me-ur-34-tRNALeu -> 5-CarboxyMeAmMe-2-O-MeU34-tRNALeu + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 5-carbo-me-ami-me-ur-34-tRNALeu -> 5-CarboxyMeAmMe-2-O-MeU34-tRNALeu + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA (cytidine/uridine-2'-O)-ribose methyltransferase (complex.ecocyc.CPLX0-7421). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a 5-carboxymethylaminomethyluridine34 in tRNALeu (molecule.ecocyc.5-carbo-me-ami-me-ur-34-tRNALeu). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-carboxymethylaminomethyl-2'-O-methyluridine34 in tRNALeu (molecule.ecocyc.5-CarboxyMeAmMe-2-O-MeU34-tRNALeu).

## Annotation

S-ADENOSYLMETHIONINE + 5-carbo-me-ami-me-ur-34-tRNALeu -> 5-CarboxyMeAmMe-2-O-MeU34-tRNALeu + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7421|complex.ecocyc.CPLX0-7421]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.5-CarboxyMeAmMe-2-O-MeU34-tRNALeu|molecule.ecocyc.5-CarboxyMeAmMe-2-O-MeU34-tRNALeu]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.5-carbo-me-ami-me-ur-34-tRNALeu|molecule.ecocyc.5-carbo-me-ami-me-ur-34-tRNALeu]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11865`

## Notes

S-ADENOSYLMETHIONINE + 5-carbo-me-ami-me-ur-34-tRNALeu -> 5-CarboxyMeAmMe-2-O-MeU34-tRNALeu + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
