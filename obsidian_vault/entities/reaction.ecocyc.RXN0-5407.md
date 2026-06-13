---
entity_id: "reaction.ecocyc.RXN0-5407"
entity_type: "reaction"
name: "RXN0-5407"
source_database: "EcoCyc"
source_id: "RXN0-5407"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PERI-BAC"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5407

`reaction.ecocyc.RXN0-5407`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5407`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PERI-BAC

## Enriched Summary

This reaction represents hydrolysis of meso-DAP-meso-DAP (3 → 3) cross-links in peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12). EcoCyc reaction equation: CPD0-1185 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + CPD-24859; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction represents hydrolysis of meso-DAP-meso-DAP (3 → 3) cross-links in peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12).

## Biological Role

Catalyzed by peptidoglycan DD-endopeptidase/peptidoglycan LD-endopeptidase (complex.ecocyc.CPLX0-3201), mepK (protein.P0AB06), mepM (protein.P0AFS9), mepS (protein.P0AFV4), mepH (protein.P76190). Substrates: H2O (molecule.C00001), a peptidoglycan internal segment with L,D cross links (meso-diaminopimelate containing) (molecule.ecocyc.CPD0-1185). Products: a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimelate) tripeptide (molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE), a peptidoglycan internal segment with (L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine) tetrapeptide (molecule.ecocyc.CPD-24859).

## Annotation

This reaction represents hydrolysis of meso-DAP-meso-DAP (3 → 3) cross-links in peptidoglycan (see for nomenclature of endopeptidase activity in E. coli K-12).

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-3201|complex.ecocyc.CPLX0-3201]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AB06|protein.P0AB06]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFS9|protein.P0AFS9]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P0AFV4|protein.P0AFV4]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P76190|protein.P76190]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE|molecule.ecocyc.A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24859|molecule.ecocyc.CPD-24859]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1185|molecule.ecocyc.CPD0-1185]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5407`

## Notes

CPD0-1185 + WATER -> A-PEPTIDOGLYCAN-MDAP-TRIPEPTIDE + CPD-24859; direction=PHYSIOL-LEFT-TO-RIGHT
