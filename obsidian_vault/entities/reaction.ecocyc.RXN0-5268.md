---
entity_id: "reaction.ecocyc.RXN0-5268"
entity_type: "reaction"
name: "RXN0-5268"
source_database: "EcoCyc"
source_id: "RXN0-5268"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5268

`reaction.ecocyc.RXN0-5268`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5268`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Involved in the electron transport chain of E. coli. Electrons are passed from ubiquinol to cytochrome, and from cytochrome to oxygen. The first reaction is technically 1.10.2.- and the second is 1.10.3.-. EcoCyc reaction equation: OXYGEN-MOLECULE + PROTON + Ubiquinols -> WATER + Ubiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. Involved in the electron transport chain of E. coli. Electrons are passed from ubiquinol to cytochrome, and from cytochrome to oxygen. The first reaction is technically 1.10.2.- and the second is 1.10.3.-.

## Biological Role

Catalyzed by cytochrome bo3 ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-O-UBIOX-CPLX). Substrates: Oxygen (molecule.C00007), H+ (molecule.C00080), Ubiquinol (molecule.C00390). Products: H2O (molecule.C00001), H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones).

## Enriched Pathways

- `ecocyc.PWY-7544` pyruvate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1329` succinate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1335` NADH to cytochrome bo oxidase electron transfer I (EcoCyc)
- `ecocyc.PWY0-1544` proline to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1561` glycerol-3-phosphate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1565` D-lactate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1567` NADH to cytochrome bo oxidase electron transfer II (EcoCyc)

## Annotation

Involved in the electron transport chain of E. coli. Electrons are passed from ubiquinol to cytochrome, and from cytochrome to oxygen. The first reaction is technically 1.10.2.- and the second is 1.10.3.-.

## Pathways

- `ecocyc.PWY-7544` pyruvate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1329` succinate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1335` NADH to cytochrome bo oxidase electron transfer I (EcoCyc)
- `ecocyc.PWY0-1544` proline to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1561` glycerol-3-phosphate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1565` D-lactate to cytochrome bo oxidase electron transfer (EcoCyc)
- `ecocyc.PWY0-1567` NADH to cytochrome bo oxidase electron transfer II (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (24)

- `activates` <-- [[molecule.C00865|molecule.C00865]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CYT-O-UBIOX-CPLX|complex.ecocyc.CYT-O-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00192|molecule.C00192]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00237|molecule.C00237]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00283|molecule.C00283]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00488|molecule.C00488]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13584|molecule.ecocyc.CPD-13584]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-2841|molecule.ecocyc.CPD-2841]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-581|molecule.ecocyc.CPD-581]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7733|molecule.ecocyc.CPD-7733]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7975|molecule.ecocyc.CPD-7975]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1232|molecule.ecocyc.CPD0-1232]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1233|molecule.ecocyc.CPD0-1233]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5268`

## Notes

OXYGEN-MOLECULE + PROTON + Ubiquinols -> WATER + Ubiquinones + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
