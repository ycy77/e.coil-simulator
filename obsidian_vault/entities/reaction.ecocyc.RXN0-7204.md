---
entity_id: "reaction.ecocyc.RXN0-7204"
entity_type: "reaction"
name: "RXN0-7204"
source_database: "EcoCyc"
source_id: "RXN0-7204"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7204

`reaction.ecocyc.RXN0-7204`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7204`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Trisaccharides -> Trisaccharides; direction=REVERSIBLE EcoCyc reaction equation: Trisaccharides -> Trisaccharides; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: a trisaccharide (molecule.ecocyc.Trisaccharides). Products: a trisaccharide (molecule.ecocyc.Trisaccharides).

## Annotation

Trisaccharides -> Trisaccharides; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Trisaccharides|molecule.ecocyc.Trisaccharides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Trisaccharides|molecule.ecocyc.Trisaccharides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7204`

## Notes

Trisaccharides -> Trisaccharides; direction=REVERSIBLE
