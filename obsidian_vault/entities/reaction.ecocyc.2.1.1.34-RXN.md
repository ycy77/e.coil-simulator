---
entity_id: "reaction.ecocyc.2.1.1.34-RXN"
entity_type: "reaction"
name: "2.1.1.34-RXN"
source_database: "EcoCyc"
source_id: "2.1.1.34-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2.1.1.34-RXN

`reaction.ecocyc.2.1.1.34-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2.1.1.34-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + tRNA-guanosine18 -> 2-O-Methylguanosine18 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-guanosine18 -> 2-O-Methylguanosine18 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by tRNA (Gm18) 2'-O-methyltransferase (complex.ecocyc.CPLX0-11183). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanosine18 in tRNA (molecule.ecocyc.tRNA-guanosine18). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 2'-O-methylguanosine18 in tRNA (molecule.ecocyc.2-O-Methylguanosine18).

## Annotation

S-ADENOSYLMETHIONINE + tRNA-guanosine18 -> 2-O-Methylguanosine18 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-11183|complex.ecocyc.CPLX0-11183]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-O-Methylguanosine18|molecule.ecocyc.2-O-Methylguanosine18]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-guanosine18|molecule.ecocyc.tRNA-guanosine18]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2.1.1.34-RXN`

## Notes

S-ADENOSYLMETHIONINE + tRNA-guanosine18 -> 2-O-Methylguanosine18 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
