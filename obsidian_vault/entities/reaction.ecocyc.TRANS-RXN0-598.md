---
entity_id: "reaction.ecocyc.TRANS-RXN0-598"
entity_type: "reaction"
name: "TRANS-RXN0-598"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-598"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN0-598

`reaction.ecocyc.TRANS-RXN0-598`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-598`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Glycerol-1-phosphate -> Glycerol-1-phosphate; direction=REVERSIBLE EcoCyc reaction equation: Glycerol-1-phosphate -> Glycerol-1-phosphate; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: glycerol 1-phosphate (molecule.ecocyc.Glycerol-1-phosphate). Products: glycerol 1-phosphate (molecule.ecocyc.Glycerol-1-phosphate).

## Annotation

Glycerol-1-phosphate -> Glycerol-1-phosphate; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Glycerol-1-phosphate|molecule.ecocyc.Glycerol-1-phosphate]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Glycerol-1-phosphate|molecule.ecocyc.Glycerol-1-phosphate]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-598`

## Notes

Glycerol-1-phosphate -> Glycerol-1-phosphate; direction=REVERSIBLE
