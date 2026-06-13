---
entity_id: "reaction.ecocyc.DALADEHYDROG-RXN"
entity_type: "reaction"
name: "D-alanine dehydrogenase"
source_database: "EcoCyc"
source_id: "DALADEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# D-alanine dehydrogenase

`reaction.ecocyc.DALADEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DALADEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

This is one instance of the broad reaction, EC 1.4.99.1. EcoCyc reaction equation: ETR-Quinones + WATER + D-ALANINE -> ETR-Quinols + AMMONIUM + PYRUVATE; direction=LEFT-TO-RIGHT. This is one instance of the broad reaction, EC 1.4.99.1.

## Biological Role

Catalyzed by D-amino acid dehydrogenase (complex.ecocyc.DALADEHYDROG-CPLX). Substrates: H2O (molecule.C00001), D-Alanine (molecule.C00133). Products: Pyruvate (molecule.C00022), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.ALADEG-PWY` L-alanine degradation I (EcoCyc)

## Annotation

This is one instance of the broad reaction, EC 1.4.99.1.

## Pathways

- `ecocyc.ALADEG-PWY` L-alanine degradation I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.DALADEHYDROG-CPLX|complex.ecocyc.DALADEHYDROG-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00133|molecule.C00133]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DALADEHYDROG-RXN`

## Notes

ETR-Quinones + WATER + D-ALANINE -> ETR-Quinols + AMMONIUM + PYRUVATE; direction=LEFT-TO-RIGHT
