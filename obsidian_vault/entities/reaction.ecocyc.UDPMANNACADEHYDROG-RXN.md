---
entity_id: "reaction.ecocyc.UDPMANNACADEHYDROG-RXN"
entity_type: "reaction"
name: "UDPMANNACADEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "UDPMANNACADEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPMANNACADEHYDROG-RXN

`reaction.ecocyc.UDPMANNACADEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPMANNACADEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis. EcoCyc reaction equation: UDP-MANNAC + NAD + WATER -> UDP-MANNACA + NADH + PROTON; direction=LEFT-TO-RIGHT. This is the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis.

## Biological Role

Catalyzed by UDP-N-acetyl-D-mannosamine dehydrogenase (complex.ecocyc.CPLX0-8013). Substrates: H2O (molecule.C00001), NAD+ (molecule.C00003), UDP-N-acetyl-D-mannosamine (molecule.C01170). Products: NADH (molecule.C00004), H+ (molecule.C00080), UDP-N-acetyl-α-D-mannosaminuronate (molecule.ecocyc.UDP-MANNACA).

## Enriched Pathways

- `ecocyc.PWY-7335` UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)
- `ecocyc.PWY0-1611` superpathway of UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)

## Annotation

This is the second reaction in the synthesis of UDP-N-acetyl-mannosaminuronic acid, which is utilized in ECA biosynthesis.

## Pathways

- `ecocyc.PWY-7335` UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)
- `ecocyc.PWY0-1611` superpathway of UDP-N-acetyl-α-D-mannosaminouronate biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8013|complex.ecocyc.CPLX0-8013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.UDP-MANNACA|molecule.ecocyc.UDP-MANNACA]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C01170|molecule.C01170]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPMANNACADEHYDROG-RXN`

## Notes

UDP-MANNAC + NAD + WATER -> UDP-MANNACA + NADH + PROTON; direction=LEFT-TO-RIGHT
