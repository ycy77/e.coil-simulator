---
entity_id: "reaction.ecocyc.RXN-17392"
entity_type: "reaction"
name: "RXN-17392"
source_database: "EcoCyc"
source_id: "RXN-17392"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17392

`reaction.ecocyc.RXN-17392`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17392`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

CPD-18804 -> CPD-18805 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-18804 -> CPD-18805 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mltD (protein.P0AEZ7), slt (protein.P0AGC3), mltC (protein.P0C066), emtA (protein.P0C960), mltB (protein.P41052). Substrates: a peptidoglycan internal segment (with L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine tetrapeptide) (molecule.ecocyc.CPD-18804). Products: a peptidoglycan (meso-DAP containing) with GlcNAc-1,6-anhydro-MurNAc terminus (molecule.ecocyc.CPD-17986), a peptidoglycan (meso-DAP containing) with GlcNAc non-reducing terminus (molecule.ecocyc.CPD-18805).

## Annotation

CPD-18804 -> CPD-18805 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P0AEZ7|protein.P0AEZ7]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AGC3|protein.P0AGC3]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C066|protein.P0C066]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0C960|protein.P0C960]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P41052|protein.P41052]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-17986|molecule.ecocyc.CPD-17986]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-18805|molecule.ecocyc.CPD-18805]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-18804|molecule.ecocyc.CPD-18804]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CPD0-1888|molecule.ecocyc.CPD0-1888]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-17392`

## Notes

CPD-18804 -> CPD-18805 + CPD-17986; direction=PHYSIOL-LEFT-TO-RIGHT
