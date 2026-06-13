---
entity_id: "reaction.ecocyc.PHOSPHOGLUCMUT-RXN"
entity_type: "reaction"
name: "PHOSPHOGLUCMUT-RXN"
source_database: "EcoCyc"
source_id: "PHOSPHOGLUCMUT-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PHOSPHOGLUCMUT-RXN

`reaction.ecocyc.PHOSPHOGLUCMUT-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PHOSPHOGLUCMUT-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Catalyzes the reversible transformation of glucose- 1-phosphate into glucose-6-phosphate. Glucose-1-phosphate is an intermediate in maltose, galactose and glycogen metabolism. EcoCyc reaction equation: GLC-1-P -> D-glucopyranose-6-phosphate; direction=REVERSIBLE. Catalyzes the reversible transformation of glucose- 1-phosphate into glucose-6-phosphate. Glucose-1-phosphate is an intermediate in maltose, galactose and glycogen metabolism.

## Biological Role

Catalyzed by pgm (protein.P36938). Substrates: α-D-glucopyranose 1-phosphate (molecule.ecocyc.GLC-1-P). Products: D-Glucose 6-phosphate (molecule.C00092).

## Enriched Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)
- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)
- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)
- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)
- `ecocyc.PWY-7343` UDP-α-D-glucose biosynthesis (EcoCyc)

## Annotation

Catalyzes the reversible transformation of glucose- 1-phosphate into glucose-6-phosphate. Glucose-1-phosphate is an intermediate in maltose, galactose and glycogen metabolism.

## Pathways

- `ecocyc.GLUCOSE1PMETAB-PWY` glucose and glucose-1-phosphate degradation (EcoCyc)
- `ecocyc.GLYCOCAT-PWY` glycogen degradation I (EcoCyc)
- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)
- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)
- `ecocyc.PWY-7343` UDP-α-D-glucose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00097|molecule.C00097]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C01231|molecule.C01231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P36938|protein.P36938]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00363|molecule.C00363]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01231|molecule.C01231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1484|molecule.ecocyc.CPD-1484]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-1492|molecule.ecocyc.CPD-1492]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-29|molecule.ecocyc.CPD-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.GLC-1-P|molecule.ecocyc.GLC-1-P]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PHOSPHOGLUCMUT-RXN`

## Notes

GLC-1-P -> D-glucopyranose-6-phosphate; direction=REVERSIBLE
