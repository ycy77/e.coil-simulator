---
entity_id: "reaction.ecocyc.NADH-DEHYDROG-A-RXN"
entity_type: "reaction"
name: "NADH-DEHYDROG-A-RXN"
source_database: "EcoCyc"
source_id: "NADH-DEHYDROG-A-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# NADH-DEHYDROG-A-RXN

`reaction.ecocyc.NADH-DEHYDROG-A-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:NADH-DEHYDROG-A-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

A reaction in the electron transport chain of E. coli. EcoCyc reaction equation: NADH + PROTON + Ubiquinones -> PROTON + NAD + Ubiquinols; direction=REVERSIBLE. A reaction in the electron transport chain of E. coli.

## Biological Role

Catalyzed by NADH:quinone oxidoreductase I (complex.ecocyc.NADH-DHI-CPLX). Substrates: NADH (molecule.C00004), H+ (molecule.C00080), a ubiquinone (molecule.ecocyc.Ubiquinones). Products: NAD+ (molecule.C00003), H+ (molecule.C00080), Ubiquinol (molecule.C00390).

## Enriched Pathways

- `ecocyc.PWY0-1334` NADH to cytochrome bd oxidase electron transfer I (EcoCyc)
- `ecocyc.PWY0-1335` NADH to cytochrome bo oxidase electron transfer I (EcoCyc)

## Annotation

A reaction in the electron transport chain of E. coli.

## Pathways

- `ecocyc.PWY0-1334` NADH to cytochrome bd oxidase electron transfer I (EcoCyc)
- `ecocyc.PWY0-1335` NADH to cytochrome bo oxidase electron transfer I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (16)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.NADH-DHI-CPLX|complex.ecocyc.NADH-DHI-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00390|molecule.C00390]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.Ubiquinones|molecule.ecocyc.Ubiquinones]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CAPSAICIN|molecule.ecocyc.CAPSAICIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1233|molecule.ecocyc.CPD0-1233]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1244|molecule.ecocyc.CPD0-1244]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1689|molecule.ecocyc.CPD0-1689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2356|molecule.ecocyc.CPD0-2356]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.O-PHENANTHROLINE|molecule.ecocyc.O-PHENANTHROLINE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:NADH-DEHYDROG-A-RXN`

## Notes

NADH + PROTON + Ubiquinones -> PROTON + NAD + Ubiquinols; direction=REVERSIBLE
