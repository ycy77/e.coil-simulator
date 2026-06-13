---
entity_id: "reaction.ecocyc.RXN-14249"
entity_type: "reaction"
name: "RXN-14249"
source_database: "EcoCyc"
source_id: "RXN-14249"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-14249

`reaction.ecocyc.RXN-14249`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-14249`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

THR + NAD -> AMINO-ACETONE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: THR + NAD -> AMINO-ACETONE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by threonine dehydrogenase (complex.ecocyc.THREODEHYD-CPLX), yiaY (protein.P37686). Substrates: NAD+ (molecule.C00003), L-Threonine (molecule.C00188). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Aminoacetone (molecule.C01888).

## Annotation

THR + NAD -> AMINO-ACETONE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (21)

- `activates` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.THREODEHYD-CPLX|complex.ecocyc.THREODEHYD-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P37686|protein.P37686]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C01888|molecule.C01888]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00741|molecule.C00741]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C06105|molecule.C06105]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.2-MERCAPTOETHANOL|molecule.ecocyc.2-MERCAPTOETHANOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.23-PENTANEDIONE|molecule.ecocyc.23-PENTANEDIONE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1486|molecule.ecocyc.CPD-1486]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1492|molecule.ecocyc.CPD-1492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7388|molecule.ecocyc.CPD-7388]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHENYLGLYOXAL|molecule.ecocyc.PHENYLGLYOXAL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-14249`

## Notes

THR + NAD -> AMINO-ACETONE + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
