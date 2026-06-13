---
entity_id: "reaction.ecocyc.TRANS-RXN0-513"
entity_type: "reaction"
name: "TRANS-RXN0-513"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-513"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-513

`reaction.ecocyc.TRANS-RXN0-513`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-513`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Auxotrophy for diaminopimelic acid (DAP) can be complemented by exogenous lanthionine. Lanthionine, supplied in the growth media of a dapAmetA mutant strain replaces meso-DAP in the peptidoglycan . Analysis of E. coli K-12 on Biolog microplates indicates that lanthionine is able to serve as the sole source of sulfur. The transporter responsible has not been identified. EcoCyc reaction equation: CPD-3736 + ATP + WATER -> CPD-3736 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. Auxotrophy for diaminopimelic acid (DAP) can be complemented by exogenous lanthionine. Lanthionine, supplied in the growth media of a dapAmetA mutant strain replaces meso-DAP in the peptidoglycan . Analysis of E. coli K-12 on Biolog microplates indicates that lanthionine is able to serve as the sole source of sulfur. The transporter responsible has not been identified.

## Biological Role

Catalyzed by cystine ABC transporter (complex.ecocyc.CPLX0-8152). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), lanthionine (molecule.ecocyc.CPD-3736). Products: ADP (molecule.C00008), H+ (molecule.C00080), lanthionine (molecule.ecocyc.CPD-3736), phosphate (molecule.ecocyc.Pi).

## Annotation

Auxotrophy for diaminopimelic acid (DAP) can be complemented by exogenous lanthionine. Lanthionine, supplied in the growth media of a dapAmetA mutant strain replaces meso-DAP in the peptidoglycan . Analysis of E. coli K-12 on Biolog microplates indicates that lanthionine is able to serve as the sole source of sulfur. The transporter responsible has not been identified.

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-8152|complex.ecocyc.CPLX0-8152]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-3736|molecule.ecocyc.CPD-3736]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-3736|molecule.ecocyc.CPD-3736]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-513`

## Notes

CPD-3736 + ATP + WATER -> CPD-3736 + ADP + Pi + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
