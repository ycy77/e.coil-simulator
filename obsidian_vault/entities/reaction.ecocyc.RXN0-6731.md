---
entity_id: "reaction.ecocyc.RXN0-6731"
entity_type: "reaction"
name: "RXN0-6731"
source_database: "EcoCyc"
source_id: "RXN0-6731"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-6731

`reaction.ecocyc.RXN0-6731`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-6731`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine1516 -> 16S-rRNA-N2methylguanine1516 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 16S-rRNA-guanine1516 -> 16S-rRNA-N2methylguanine1516 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by rsmJ (protein.P68567). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a guanine1516 in 16S rRNA (molecule.ecocyc.16S-rRNA-guanine1516). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), an N2-methylguanine1516 in 16S rRNA (molecule.ecocyc.16S-rRNA-N2methylguanine1516).

## Annotation

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine1516 -> 16S-rRNA-N2methylguanine1516 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P68567|protein.P68567]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.16S-rRNA-N2methylguanine1516|molecule.ecocyc.16S-rRNA-N2methylguanine1516]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.16S-rRNA-guanine1516|molecule.ecocyc.16S-rRNA-guanine1516]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-6731`

## Notes

S-ADENOSYLMETHIONINE + 16S-rRNA-guanine1516 -> 16S-rRNA-N2methylguanine1516 + ADENOSYL-HOMO-CYS + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
