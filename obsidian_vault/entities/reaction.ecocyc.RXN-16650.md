---
entity_id: "reaction.ecocyc.RXN-16650"
entity_type: "reaction"
name: "RXN-16650"
source_database: "EcoCyc"
source_id: "RXN-16650"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-CYTOSOL|CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-16650

`reaction.ecocyc.RXN-16650`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-16650`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-CYTOSOL|CCO-PERI-BAC

## Enriched Summary

Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer EcoCyc reaction equation: CPD-17927 + C6 -> CPD-17927 + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT. Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer

## Biological Role

Catalyzed by peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcB (complex.ecocyc.CPLX0-3951), peptidoglycan glycosyltransferase / peptidoglycan DD-transpeptidase MrcA (complex.ecocyc.CPLX0-7717), ftsW (protein.P0ABG4), mrdB (protein.P0ABG7), mtgA (protein.P46022), pbpC (protein.P76577). Substrates: Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05898), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine) pentapeptide (molecule.ecocyc.CPD-17927). Products: di-trans,poly-cis-Undecaprenyl diphosphate (molecule.C04574), a nascent peptidoglycan with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine) pentapeptide (molecule.ecocyc.CPD-17927).

## Enriched Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Annotation

Peptidoglycan glycosyltransferases add monomer units to the reducing end of the growing polymer

## Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)
- `ecocyc.PWY0-1586` peptidoglycan maturation (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (25)

- `activates` <-- [[protein.P0AB38|protein.P0AB38]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P29131|protein.P29131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P45464|protein.P45464]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-3951|complex.ecocyc.CPLX0-3951]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7717|complex.ecocyc.CPLX0-7717]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABG4|protein.P0ABG4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0ABG7|protein.P0ABG7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P46022|protein.P46022]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76577|protein.P76577]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04574|molecule.C04574]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17927|molecule.ecocyc.CPD-17927]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05898|molecule.C05898]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-17927|molecule.ecocyc.CPD-17927]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C06689|molecule.C06689]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12251|molecule.ecocyc.CPD-12251]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-12301|molecule.ecocyc.CPD-12301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-28121|molecule.ecocyc.CPD-28121]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-5242|molecule.ecocyc.CPD-5242]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2603|molecule.ecocyc.CPD0-2603]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2604|molecule.ecocyc.CPD0-2604]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2605|molecule.ecocyc.CPD0-2605]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2606|molecule.ecocyc.CPD0-2606]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2607|molecule.ecocyc.CPD0-2607]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MOENOMYCIN|molecule.ecocyc.MOENOMYCIN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-16650`

## Notes

CPD-17927 + C6 -> CPD-17927 + UNDECAPRENYL-DIPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
