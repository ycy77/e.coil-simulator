---
entity_id: "reaction.ecocyc.IMP-DEHYDROG-RXN"
entity_type: "reaction"
name: "IMP-DEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "IMP-DEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# IMP-DEHYDROG-RXN

`reaction.ecocyc.IMP-DEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:IMP-DEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first reaction unique to GMP biosynthesis. EcoCyc reaction equation: WATER + NAD + IMP -> PROTON + NADH + XANTHOSINE-5-PHOSPHATE; direction=REVERSIBLE. This is the first reaction unique to GMP biosynthesis.

## Biological Role

Catalyzed by inosine 5'-monophosphate dehydrogenase (complex.ecocyc.IMP-DEHYDROG-CPLX). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), IMP (molecule.C00130). Products: NADH (molecule.C00004), H+ (molecule.C00080), Xanthosine 5'-phosphate (molecule.C00655).

## Enriched Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Annotation

This is the first reaction unique to GMP biosynthesis.

## Pathways

- `ecocyc.PWY-7221` guanosine ribonucleotides de novo biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (19)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-2|molecule.ecocyc.CPD-2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.RB|molecule.ecocyc.RB_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.IMP-DEHYDROG-CPLX|complex.ecocyc.IMP-DEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00130|molecule.C00130]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00144|molecule.C00144]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00533|molecule.C00533]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00633|molecule.C00633]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00655|molecule.C00655]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01228|molecule.C01228]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1492|molecule.ecocyc.CPD0-1492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1493|molecule.ecocyc.CPD0-1493]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:IMP-DEHYDROG-RXN`

## Notes

WATER + NAD + IMP -> PROTON + NADH + XANTHOSINE-5-PHOSPHATE; direction=REVERSIBLE
