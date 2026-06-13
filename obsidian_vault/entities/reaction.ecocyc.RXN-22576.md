---
entity_id: "reaction.ecocyc.RXN-22576"
entity_type: "reaction"
name: "RXN-22576"
source_database: "EcoCyc"
source_id: "RXN-22576"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCI-PERI-BAC-GN"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22576

`reaction.ecocyc.RXN-22576`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22576`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCI-PERI-BAC-GN

## Enriched Summary

CPD-24805 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + GLY; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-24805 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + GLY; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by dpaA (protein.P0AA99). Substrates: H2O (molecule.C00001), a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-glycine) tetrapeptide (molecule.ecocyc.CPD-24805). Products: Glycine (molecule.C00037), a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimelate) tripeptide (molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE).

## Annotation

CPD-24805 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + GLY; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0AA99|protein.P0AA99]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00037|molecule.C00037]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE|molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24805|molecule.ecocyc.CPD-24805]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22576`

## Notes

CPD-24805 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + GLY; direction=PHYSIOL-LEFT-TO-RIGHT
