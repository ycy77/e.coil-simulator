---
entity_id: "reaction.ecocyc.RXN-21204"
entity_type: "reaction"
name: "RXN-21204"
source_database: "EcoCyc"
source_id: "RXN-21204"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-21204

`reaction.ecocyc.RXN-21204`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-21204`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD-22802 + WATER -> CPD-22805 + Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD-22802 + WATER -> CPD-22805 + Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by metalloprotease TldDE (complex.ecocyc.CPLX0-8539). Substrates: H2O (molecule.C00001), microcin B17 precursor peptide containing azole residues (molecule.ecocyc.CPD-22802). Products: microcin B17 (molecule.ecocyc.CPD-22805).

## Annotation

CPD-22802 + WATER -> CPD-22805 + Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8539|complex.ecocyc.CPLX0-8539]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD-22805|molecule.ecocyc.CPD-22805]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-22802|molecule.ecocyc.CPD-22802]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-21204`

## Notes

CPD-22802 + WATER -> CPD-22805 + Peptides-holder; direction=PHYSIOL-LEFT-TO-RIGHT
