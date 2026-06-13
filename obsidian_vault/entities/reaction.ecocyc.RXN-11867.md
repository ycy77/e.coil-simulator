---
entity_id: "reaction.ecocyc.RXN-11867"
entity_type: "reaction"
name: "S-adenosyl-L-methionine:tRNA (cytidine32/uridine32-2'-O)-methyltransferase"
source_database: "EcoCyc"
source_id: "RXN-11867"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# S-adenosyl-L-methionine:tRNA (cytidine32/uridine32-2'-O)-methyltransferase

`reaction.ecocyc.RXN-11867`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11867`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + Uridine32-in-tRNA -> 2-O-Methyluridine32-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + Uridine32-in-tRNA -> 2-O-Methyluridine32-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA Cm32/Um32 methyltransferase (complex.ecocyc.CPLX0-7420). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uridine32 in tRNA (molecule.ecocyc.Uridine32-in-tRNA). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 2'-O-methyluridine32 in tRNA (molecule.ecocyc.2-O-Methyluridine32-tRNA).

## Annotation

S-ADENOSYLMETHIONINE + Uridine32-in-tRNA -> 2-O-Methyluridine32-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7420|complex.ecocyc.CPLX0-7420]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-O-Methyluridine32-tRNA|molecule.ecocyc.2-O-Methyluridine32-tRNA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Uridine32-in-tRNA|molecule.ecocyc.Uridine32-in-tRNA]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11867`

## Notes

S-ADENOSYLMETHIONINE + Uridine32-in-tRNA -> 2-O-Methyluridine32-tRNA + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
