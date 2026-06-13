---
entity_id: "reaction.ecocyc.ATPSYN-RXN"
entity_type: "reaction"
name: "ATPSYN-RXN"
source_database: "EcoCyc"
source_id: "ATPSYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "H(+)-transporting ATP synthase"
  - "F(0)F(1)-ATPase"
  - "F(1)-ATPase"
  - "H(+)-TRANSPORTING ATPASE"
  - "MITOCHONDRIAL ATPASE"
  - "CHLOROPLAST ATPASE"
  - "COUPLING FACTORS (F(O), F(1) AND CF(1))"
---

# ATPSYN-RXN

`reaction.ecocyc.ATPSYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ATPSYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Under conditions where respiration produces a proton gradient across the plasma membrane, this reaction synthesizes ATP. The energy of electron transport and proton extrusion is in this way captured in the form of ATP. Under low proton gradient conditions the reaction is reversible, hydrolyzing ATP and pumping protons into the periplasmic space, thereby increasing the proton gradient. Pi + H+(periplasm) + ADP = ATP + H+(cytoplasm) + H2O EcoCyc reaction equation: ATP + WATER + PROTON -> ADP + Pi + PROTON; direction=REVERSIBLE. Under conditions where respiration produces a proton gradient across the plasma membrane, this reaction synthesizes ATP. The energy of electron transport and proton extrusion is in this way captured in the form of ATP. Under low proton gradient conditions the reaction is reversible, hydrolyzing ATP and pumping protons into the periplasmic space, thereby increasing the proton gradient. Pi + H+(periplasm) + ADP = ATP + H+(cytoplasm) + H2O

## Biological Role

Catalyzed by ATP synthase / thiamin triphosphate synthase (complex.ecocyc.ATPSYN-CPLX). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), H+ (molecule.C00080). Products: ADP (molecule.C00008), H+ (molecule.C00080), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-7980` ATP biosynthesis (EcoCyc)

## Annotation

Under conditions where respiration produces a proton gradient across the plasma membrane, this reaction synthesizes ATP. The energy of electron transport and proton extrusion is in this way captured in the form of ATP. Under low proton gradient conditions the reaction is reversible, hydrolyzing ATP and pumping protons into the periplasmic space, thereby increasing the proton gradient. Pi + H+(periplasm) + ADP = ATP + H+(cytoplasm) + H2O

## Pathways

- `ecocyc.PWY-7980` ATP biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `catalyzes` <-- [[complex.ecocyc.ATPSYN-CPLX|complex.ecocyc.ATPSYN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00389|molecule.C00389]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-10322|molecule.ecocyc.CPD-10322]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-11925|molecule.ecocyc.CPD-11925]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-16010|molecule.ecocyc.CPD-16010]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-23697|molecule.ecocyc.CPD-23697]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-83|molecule.ecocyc.CPD-83]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1250|molecule.ecocyc.CPD0-1250]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1618|molecule.ecocyc.CPD0-1618]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1620|molecule.ecocyc.CPD0-1620]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1624|molecule.ecocyc.CPD0-1624]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ATPSYN-RXN`

## Notes

ATP + WATER + PROTON -> ADP + Pi + PROTON; direction=REVERSIBLE
