---
entity_id: "reaction.ecocyc.RXN0-7244"
entity_type: "reaction"
name: "RXN0-7244"
source_database: "EcoCyc"
source_id: "RXN0-7244"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7244

`reaction.ecocyc.RXN0-7244`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7244`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

All-Amines -> All-Amines; direction=REVERSIBLE EcoCyc reaction equation: All-Amines -> All-Amines; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: an amine (molecule.ecocyc.All-Amines). Products: an amine (molecule.ecocyc.All-Amines).

## Annotation

All-Amines -> All-Amines; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.All-Amines|molecule.ecocyc.All-Amines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.All-Amines|molecule.ecocyc.All-Amines]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7244`

## Notes

All-Amines -> All-Amines; direction=REVERSIBLE
