---
entity_id: "reaction.ecocyc.RXN-22575"
entity_type: "reaction"
name: "RXN-22575"
source_database: "EcoCyc"
source_id: "RXN-22575"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22575

`reaction.ecocyc.RXN-22575`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22575`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD0-1171 + WATER -> a-murein-lipoprotein + A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1171 + WATER -> a-murein-lipoprotein + A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dpaA (protein.P0AA99). Substrates: H2O (molecule.C00001), a peptidoglycan crosslinked to murein lipoprotein (molecule.ecocyc.CPD0-1171). Products: a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimelate) tripeptide (molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE).

## Annotation

CPD0-1171 + WATER -> a-murein-lipoprotein + A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA99|protein.P0AA99]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE|molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1171|molecule.ecocyc.CPD0-1171]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN-22575`

## Notes

CPD0-1171 + WATER -> a-murein-lipoprotein + A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE; direction=PHYSIOL-LEFT-TO-RIGHT
