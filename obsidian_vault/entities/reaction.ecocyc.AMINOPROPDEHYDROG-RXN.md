---
entity_id: "reaction.ecocyc.AMINOPROPDEHYDROG-RXN"
entity_type: "reaction"
name: "AMINOPROPDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "AMINOPROPDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# AMINOPROPDEHYDROG-RXN

`reaction.ecocyc.AMINOPROPDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:AMINOPROPDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

1-AMINO-PROPAN-2-OL + NAD -> PROTON + AMINO-ACETONE + NADH; direction=RIGHT-TO-LEFT EcoCyc reaction equation: 1-AMINO-PROPAN-2-OL + NAD -> PROTON + AMINO-ACETONE + NADH; direction=RIGHT-TO-LEFT.

## Biological Role

Catalyzed by L-1,2-propanediol dehydrogenase / glycerol dehydrogenase (complex.ecocyc.GLYCDEH-CPLX). Substrates: NAD+ (molecule.C00003), (R)-1-Aminopropan-2-ol (molecule.C03194). Products: NADH (molecule.C00004), H+ (molecule.C00080), Aminoacetone (molecule.C01888).

## Annotation

1-AMINO-PROPAN-2-OL + NAD -> PROTON + AMINO-ACETONE + NADH; direction=RIGHT-TO-LEFT

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `catalyzes` <-- [[complex.ecocyc.GLYCDEH-CPLX|complex.ecocyc.GLYCDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01888|molecule.C01888]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C03194|molecule.C03194]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:AMINOPROPDEHYDROG-RXN`

## Notes

1-AMINO-PROPAN-2-OL + NAD -> PROTON + AMINO-ACETONE + NADH; direction=RIGHT-TO-LEFT
