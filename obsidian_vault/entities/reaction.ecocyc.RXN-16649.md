---
entity_id: "reaction.ecocyc.RXN-16649"
entity_type: "reaction"
name: "RXN-16649"
source_database: "EcoCyc"
source_id: "RXN-16649"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "DD-peptidase"
  - "D-alanyl-D-alanine carboxypeptidase"
---

# RXN-16649

`reaction.ecocyc.RXN-16649`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16649`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN|CCO-PERI-BAC

## Enriched Summary

CPD-17927 + WATER -> CPD-17926 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-17927 + WATER -> CPD-17926 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB (complex.ecocyc.CPLX0-3951), peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA (complex.ecocyc.CPLX0-7717), D-alanyl-D-alanine carboxypeptidase DacA (complex.ecocyc.CPLX0-8252), D-alanyl-D-alanine carboxypeptidase DacC (complex.ecocyc.CPLX0-8254), peptidoglycan DD endopeptidase DacB (complex.ecocyc.CPLX0-8545), ampH (protein.P0AD70), dacD (protein.P33013), yfeW (protein.P77619). Substrates: H2O (molecule.C00001), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine) pentapeptide (molecule.ecocyc.CPD-17927). Products: D-Alanine (molecule.C00133), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.CPD-17926).

## Enriched Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

CPD-17927 + WATER -> CPD-17926 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (22)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3951|complex.ecocyc.CPLX0-3951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7717|complex.ecocyc.CPLX0-7717]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8252|complex.ecocyc.CPLX0-8252]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8254|complex.ecocyc.CPLX0-8254]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8545|complex.ecocyc.CPLX0-8545]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AD70|protein.P0AD70]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P33013|protein.P33013]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77619|protein.P77619]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17926|molecule.ecocyc.CPD-17926]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17927|molecule.ecocyc.CPD-17927]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-9195|molecule.ecocyc.CPD-9195]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9220|molecule.ecocyc.CPD-9220]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9224|molecule.ecocyc.CPD-9224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9226|molecule.ecocyc.CPD-9226]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9227|molecule.ecocyc.CPD-9227]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9231|molecule.ecocyc.CPD-9231]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2600|molecule.ecocyc.CPD0-2600]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2608|molecule.ecocyc.CPD0-2608]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2611|molecule.ecocyc.CPD0-2611]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PENICILLIN-G|molecule.ecocyc.PENICILLIN-G]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-16649`

## Notes

CPD-17927 + WATER -> CPD-17926 + D-ALANINE; direction=PHYSIOL-LEFT-TO-RIGHT
