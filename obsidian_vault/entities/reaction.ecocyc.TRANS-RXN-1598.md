---
entity_id: "reaction.ecocyc.TRANS-RXN-1598"
entity_type: "reaction"
name: "TRANS-RXN-1598"
source_database: "EcoCyc"
source_id: "TRANS-RXN-1598"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-EXTRACELLULAR-CCO-CYTOSOL"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-1598

`reaction.ecocyc.TRANS-RXN-1598`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-1598`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-EXTRACELLULAR-CCO-CYTOSOL

## Enriched Summary

CPD-21612 + PROTON -> CPD-21612 + PROTON; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD-21612 + PROTON -> CPD-21612 + PROTON; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ferric enterobactin outer membrane transport complex (complex.ecocyc.CPLX0-1941), ferric catecholate outer membrane transport complex I (complex.ecocyc.CPLX0-8541), ferric catecholate outer membrane transport complex II (complex.ecocyc.CPLX0-8553). Substrates: H+ (molecule.C00080), iron(III)-[(2,3-dihydroxybenzoylserine)2] complex (molecule.ecocyc.CPD-21612). Products: H+ (molecule.C00080), iron(III)-[(2,3-dihydroxybenzoylserine)2] complex (molecule.ecocyc.CPD-21612).

## Annotation

CPD-21612 + PROTON -> CPD-21612 + PROTON; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-1941|complex.ecocyc.CPLX0-1941]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8541|complex.ecocyc.CPLX0-8541]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8553|complex.ecocyc.CPLX0-8553]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21612|molecule.ecocyc.CPD-21612]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-21612|molecule.ecocyc.CPD-21612]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-1598`

## Notes

CPD-21612 + PROTON -> CPD-21612 + PROTON; direction=LEFT-TO-RIGHT
