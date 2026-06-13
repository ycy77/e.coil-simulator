---
entity_id: "reaction.ecocyc.1PFRUCTPHOSN-RXN"
entity_type: "reaction"
name: "1PFRUCTPHOSN-RXN"
source_database: "EcoCyc"
source_id: "1PFRUCTPHOSN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "FRUCTOSE 1-PHOSPHATE KINASE"
---

# 1PFRUCTPHOSN-RXN

`reaction.ecocyc.1PFRUCTPHOSN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1PFRUCTPHOSN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

E.coli grows readily on fructose as a sole source of carbon. It was long assumed that the manner in which this sugar is utilized is analogous to that by which glucose enters the main metabolic pathways of the cells; this would imply the occurrence of an initial enzymatic phosphorylation by ATP of fructose to fructose-6-phosphate and ADP, followed by a second phosphorylation to fructose-1,6-bisphosphate. Enzymes catalyzing both these reactions have been demonstrated to be present in E.coli. However, studies in several labs have cast doubt on this view and have suggested that fructose is initially phosphorylated to fructose-1-phosphate with concomitant conversion of PEP to pyruvate. Fructose-1-phosphate is then further phosphorylated to fructose-1,6-diphosphate through the agency of an ATP-linked fructose-1-phosphate-kinase. This reaction is part of a pathway for fructose metabolism in E.coli: fructose = fructose-1-p = fructose-16p. The first reaction, catalyzed by a phosphotransferase system,involves a phosphoenolpyruvate-dependent phosphorylation of D-fructose at C-1. The second reaction is an ATP dependent phosphorylation of D-fructose-1-phosphate at C-6. The enzyme involved in the latter is 1-phosphofructokinase. EcoCyc reaction equation: ATP + FRU1P -> PROTON + ADP + FRUCTOSE-16-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. E...

## Biological Role

Catalyzed by 1-phosphofructokinase (complex.ecocyc.1-PFK). Substrates: ATP (molecule.C00002), β-D-fructofuranose 1-phosphate (molecule.ecocyc.FRU1P). Products: ADP (molecule.C00008), H+ (molecule.C00080), D-Fructose 1,6-bisphosphate (molecule.C00354).

## Enriched Pathways

- `ecocyc.PWY0-1314` fructose degradation (EcoCyc)

## Annotation

E.coli grows readily on fructose as a sole source of carbon. It was long assumed that the manner in which this sugar is utilized is analogous to that by which glucose enters the main metabolic pathways of the cells; this would imply the occurrence of an initial enzymatic phosphorylation by ATP of fructose to fructose-6-phosphate and ADP, followed by a second phosphorylation to fructose-1,6-bisphosphate. Enzymes catalyzing both these reactions have been demonstrated to be present in E.coli. However, studies in several labs have cast doubt on this view and have suggested that fructose is initially phosphorylated to fructose-1-phosphate with concomitant conversion of PEP to pyruvate. Fructose-1-phosphate is then further phosphorylated to fructose-1,6-diphosphate through the agency of an ATP-linked fructose-1-phosphate-kinase. This reaction is part of a pathway for fructose metabolism in E.coli: fructose = fructose-1-p = fructose-16p. The first reaction, catalyzed by a phosphotransferase system,involves a phosphoenolpyruvate-dependent phosphorylation of D-fructose at C-1. The second reaction is an ATP dependent phosphorylation of D-fructose-1-phosphate at C-6. The enzyme involved in the latter is 1-phosphofructokinase.

## Pathways

- `ecocyc.PWY0-1314` fructose degradation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `activates` <-- [[molecule.ecocyc.KCL|molecule.ecocyc.KCL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.1-PFK|complex.ecocyc.1-PFK]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.FRU1P|molecule.ecocyc.FRU1P]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5541|molecule.ecocyc.CPD-5541]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1PFRUCTPHOSN-RXN`

## Notes

ATP + FRU1P -> PROTON + ADP + FRUCTOSE-16-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
