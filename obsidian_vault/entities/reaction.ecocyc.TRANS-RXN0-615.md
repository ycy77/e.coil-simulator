---
entity_id: "reaction.ecocyc.TRANS-RXN0-615"
entity_type: "reaction"
name: "TRANS-RXN0-615"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-615"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-615

`reaction.ecocyc.TRANS-RXN0-615`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-615`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

CPD-560 -> CPD-560; direction=REVERSIBLE EcoCyc reaction equation: CPD-560 -> CPD-560; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: 5-Methylthio-D-ribose (molecule.C03089). Products: 5-Methylthio-D-ribose (molecule.C03089).

## Annotation

CPD-560 -> CPD-560; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C03089|molecule.C03089]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C03089|molecule.C03089]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-615`

## Notes

CPD-560 -> CPD-560; direction=REVERSIBLE
