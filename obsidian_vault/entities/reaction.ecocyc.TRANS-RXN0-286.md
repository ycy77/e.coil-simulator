---
entity_id: "reaction.ecocyc.TRANS-RXN0-286"
entity_type: "reaction"
name: "lipid II flippase"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-286"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# lipid II flippase

`reaction.ecocyc.TRANS-RXN0-286`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-286`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This reaction represents (imperfectly) lipid II flippase activity - the PMF dependent, transbilayer 'flipping' of lipid II across the inner membrane of E. coli. EcoCyc reaction equation: C6 + PROTON -> C6 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents (imperfectly) lipid II flippase activity - the PMF dependent, transbilayer 'flipping' of lipid II across the inner membrane of E. coli.

## Biological Role

Catalyzed by murJ (protein.P0AF16). Substrates: H+ (molecule.C00080), Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05898). Products: H+ (molecule.C00080), Undecaprenyl-diphospho-N-acetylmuramoyl-(N-acetylglucosamine)-L-alanyl-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine (molecule.C05898).

## Enriched Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Annotation

This reaction represents (imperfectly) lipid II flippase activity - the PMF dependent, transbilayer 'flipping' of lipid II across the inner membrane of E. coli.

## Pathways

- `ecocyc.PEPTIDOGLYCANSYN-PWY` peptidoglycan biosynthesis I (meso-diaminopimelate containing) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P0AF16|protein.P0AF16]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C05898|molecule.C05898]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C05898|molecule.C05898]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD-20899|molecule.ecocyc.CPD-20899]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-20920|molecule.ecocyc.CPD-20920]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRANS-RXN0-286`

## Notes

C6 + PROTON -> C6 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
