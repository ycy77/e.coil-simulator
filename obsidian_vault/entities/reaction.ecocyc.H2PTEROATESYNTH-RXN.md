---
entity_id: "reaction.ecocyc.H2PTEROATESYNTH-RXN"
entity_type: "reaction"
name: "H2PTEROATESYNTH-RXN"
source_database: "EcoCyc"
source_id: "H2PTEROATESYNTH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# H2PTEROATESYNTH-RXN

`reaction.ecocyc.H2PTEROATESYNTH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:H2PTEROATESYNTH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is a reaction in folic acid biosynthesis biosynthesis. EcoCyc reaction equation: P-AMINO-BENZOATE + DIHYDROPTERIN-CH2OH-PP -> 7-8-DIHYDROPTEROATE + PPI; direction=LEFT-TO-RIGHT. This is a reaction in folic acid biosynthesis biosynthesis.

## Biological Role

Catalyzed by dihydropteroate synthase (complex.ecocyc.H2PTEROATESYNTH-CPLX). Substrates: 4-Aminobenzoate (molecule.C00568), 6-Hydroxymethyl-7,8-dihydropterin diphosphate (molecule.C04807). Products: Diphosphate (molecule.C00013), Dihydropteroate (molecule.C00921).

## Enriched Pathways

- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Annotation

This is a reaction in folic acid biosynthesis biosynthesis.

## Pathways

- `ecocyc.PWY-6614` tetrahydrofolate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[complex.ecocyc.H2PTEROATESYNTH-CPLX|complex.ecocyc.H2PTEROATESYNTH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00921|molecule.C00921]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00568|molecule.C00568]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04807|molecule.C04807]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00921|molecule.C00921]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.5-Nitroisocytosine-Derivatives|molecule.ecocyc.5-Nitroisocytosine-Derivatives]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-889|molecule.ecocyc.CPD0-889]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Diaryl-Sulfone-Derivatives|molecule.ecocyc.Diaryl-Sulfone-Derivatives]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Sulfonamides|molecule.ecocyc.Sulfonamides]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:H2PTEROATESYNTH-RXN`

## Notes

P-AMINO-BENZOATE + DIHYDROPTERIN-CH2OH-PP -> 7-8-DIHYDROPTEROATE + PPI; direction=LEFT-TO-RIGHT
