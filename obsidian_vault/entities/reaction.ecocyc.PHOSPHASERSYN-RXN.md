---
entity_id: "reaction.ecocyc.PHOSPHASERSYN-RXN"
entity_type: "reaction"
name: "PHOSPHASERSYN-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHASERSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHASERSYN-RXN

`reaction.ecocyc.PHOSPHASERSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHASERSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is at a branch point and is the committed step for the synthesis of phosphatidylethanolamine. EcoCyc reaction equation: CDPDIACYLGLYCEROL + SER -> CMP + L-1-PHOSPHATIDYL-SERINE + PROTON; direction=LEFT-TO-RIGHT. This reaction is at a branch point and is the committed step for the synthesis of phosphatidylethanolamine.

## Biological Role

Catalyzed by phosphatidylserine synthase (complex.ecocyc.CPLX0-12524). Substrates: L-Serine (molecule.C00065), CDP-diacylglycerol (molecule.C00269). Products: CMP (molecule.C00055), H+ (molecule.C00080), Phosphatidylserine (molecule.C02737).

## Enriched Pathways

- `ecocyc.PWY-5669` phosphatidylserine and phosphatidylethanolamine biosynthesis I (EcoCyc)

## Annotation

This reaction is at a branch point and is the committed step for the synthesis of phosphatidylethanolamine.

## Pathways

- `ecocyc.PWY-5669` phosphatidylserine and phosphatidylethanolamine biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C05980|molecule.C05980]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-7988|molecule.ecocyc.CPD-7988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-2652|molecule.ecocyc.CPD0-2652]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-12524|complex.ecocyc.CPLX0-12524]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C02737|molecule.C02737]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00269|molecule.C00269]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:PHOSPHASERSYN-RXN`

## Notes

CDPDIACYLGLYCEROL + SER -> CMP + L-1-PHOSPHATIDYL-SERINE + PROTON; direction=LEFT-TO-RIGHT
