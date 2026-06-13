---
entity_id: "reaction.ecocyc.RXN0-3461"
entity_type: "reaction"
name: "RXN0-3461"
source_database: "EcoCyc"
source_id: "RXN0-3461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-3461

`reaction.ecocyc.RXN0-3461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-3461`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction represents DD endopeptidase activity - hydrolysis of the meso-diaminopimelyl-D-alanyl bond in cross-linked peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12). EcoCyc reaction equation: CPD0-2579 + WATER -> CPD-17931 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents DD endopeptidase activity - hydrolysis of the meso-diaminopimelyl-D-alanyl bond in cross-linked peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12).

## Biological Role

Catalyzed by peptidoglycan DD-endopeptidase/peptidoglycan LD-endopeptidase (complex.ecocyc.CPLX0-3201), peptidoglycan DD endopeptidase DacB (complex.ecocyc.CPLX0-8545), ampH (protein.P0AD70), pbpG (protein.P0AFI5), mepM (protein.P0AFS9), mepS (protein.P0AFV4), mepH (protein.P76190). Substrates: H2O (molecule.C00001), a mature peptidoglycan with D,D cross-links (meso-diaminopimelate containing) (molecule.ecocyc.CPD0-2579). Products: a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.CPD-17931), a peptidoglycan (meso-DAP containing) with GlcNAc-1,6-anhydro-MurNAc terminus (molecule.ecocyc.CPD-17986).

## Annotation

This reaction represents DD endopeptidase activity - hydrolysis of the meso-diaminopimelyl-D-alanyl bond in cross-linked peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12).

## Outgoing Edges (0)

_None._

## Incoming Edges (22)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3201|complex.ecocyc.CPLX0-3201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8545|complex.ecocyc.CPLX0-8545]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AD70|protein.P0AD70]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFI5|protein.P0AFI5]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFS9|protein.P0AFS9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFV4|protein.P0AFV4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76190|protein.P76190]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17931|molecule.ecocyc.CPD-17931]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-17986|molecule.ecocyc.CPD-17986]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-2579|molecule.ecocyc.CPD0-2579]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-19296|molecule.ecocyc.CPD-19296]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9195|molecule.ecocyc.CPD-9195]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9220|molecule.ecocyc.CPD-9220]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9229|molecule.ecocyc.CPD-9229]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-9233|molecule.ecocyc.CPD-9233]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1545|molecule.ecocyc.CPD0-1545]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1546|molecule.ecocyc.CPD0-1546]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2597|molecule.ecocyc.CPD0-2597]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2600|molecule.ecocyc.CPD0-2600]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-2610|molecule.ecocyc.CPD0-2610]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PENICILLIN-G|molecule.ecocyc.PENICILLIN-G]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-3461`

## Notes

CPD0-2579 + WATER -> CPD-17931 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT
