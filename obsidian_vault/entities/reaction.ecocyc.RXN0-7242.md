---
entity_id: "reaction.ecocyc.RXN0-7242"
entity_type: "reaction"
name: "RXN0-7242"
source_database: "EcoCyc"
source_id: "RXN0-7242"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7242

`reaction.ecocyc.RXN0-7242`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7242`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Aldonic-Acids -> Aldonic-Acids; direction=REVERSIBLE EcoCyc reaction equation: Aldonic-Acids -> Aldonic-Acids; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: an aldonate (molecule.ecocyc.Aldonic-Acids). Products: an aldonate (molecule.ecocyc.Aldonic-Acids).

## Annotation

Aldonic-Acids -> Aldonic-Acids; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Aldonic-Acids|molecule.ecocyc.Aldonic-Acids]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Aldonic-Acids|molecule.ecocyc.Aldonic-Acids]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7242`

## Notes

Aldonic-Acids -> Aldonic-Acids; direction=REVERSIBLE
