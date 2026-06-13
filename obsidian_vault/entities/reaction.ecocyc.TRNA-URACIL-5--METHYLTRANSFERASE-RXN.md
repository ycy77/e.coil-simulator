---
entity_id: "reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN"
entity_type: "reaction"
name: "TRNA-URACIL-5--METHYLTRANSFERASE-RXN"
source_database: "EcoCyc"
source_id: "TRNA-URACIL-5--METHYLTRANSFERASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRNA-URACIL-5--METHYLTRANSFERASE-RXN

`reaction.ecocyc.TRNA-URACIL-5--METHYLTRANSFERASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRNA-URACIL-5--METHYLTRANSFERASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + tRNA-with-uridine-54 -> tRNA-containing-5Me-uridine54 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-with-uridine-54 -> tRNA-containing-5Me-uridine54 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by trmA (protein.P23003). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a uridine54 in tRNA (molecule.ecocyc.tRNA-with-uridine-54). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-methyluridine54 in tRNA (molecule.ecocyc.tRNA-containing-5Me-uridine54).

## Annotation

S-ADENOSYLMETHIONINE + tRNA-with-uridine-54 -> tRNA-containing-5Me-uridine54 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P23003|protein.P23003]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-containing-5Me-uridine54|molecule.ecocyc.tRNA-containing-5Me-uridine54]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-with-uridine-54|molecule.ecocyc.tRNA-with-uridine-54]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRNA-URACIL-5--METHYLTRANSFERASE-RXN`

## Notes

S-ADENOSYLMETHIONINE + tRNA-with-uridine-54 -> tRNA-containing-5Me-uridine54 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
