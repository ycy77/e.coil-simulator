---
entity_id: "reaction.ecocyc.BADH-RXN"
entity_type: "reaction"
name: "BADH-RXN"
source_database: "EcoCyc"
source_id: "BADH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# BADH-RXN

`reaction.ecocyc.BADH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BADH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the betaine biosynthetic pathway. EcoCyc reaction equation: BETAINE_ALDEHYDE + NAD + WATER -> PROTON + BETAINE + NADH; direction=LEFT-TO-RIGHT. This is the second reaction in the betaine biosynthetic pathway.

## Biological Role

Catalyzed by betaine aldehyde dehydrogenase (complex.ecocyc.BADH-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), Betaine aldehyde (molecule.C00576). Products: NADH (molecule.C00004), H+ (molecule.C00080), Betaine (molecule.C00719).

## Enriched Pathways

- `ecocyc.BETSYN-PWY` glycine betaine biosynthesis I (Gram-negative bacteria) (EcoCyc)

## Annotation

This is the second reaction in the betaine biosynthetic pathway.

## Pathways

- `ecocyc.BETSYN-PWY` glycine betaine biosynthesis I (Gram-negative bacteria) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (22)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.BADH-CPLX|complex.ecocyc.BADH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00719|molecule.C00719]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00576|molecule.C00576]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00114|molecule.C00114]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00261|molecule.C00261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00577|molecule.C00577]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00601|molecule.C00601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5601|molecule.ecocyc.CPD-5601]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5602|molecule.ecocyc.CPD-5602]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7031|molecule.ecocyc.CPD-7031]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7679|molecule.ecocyc.CPD-7679]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1675|molecule.ecocyc.CPD0-1675]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1678|molecule.ecocyc.CPD0-1678]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:BADH-RXN`

## Notes

BETAINE_ALDEHYDE + NAD + WATER -> PROTON + BETAINE + NADH; direction=LEFT-TO-RIGHT
