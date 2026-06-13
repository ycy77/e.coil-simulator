---
entity_id: "reaction.ecocyc.RXN0-7200"
entity_type: "reaction"
name: "RXN0-7200"
source_database: "EcoCyc"
source_id: "RXN0-7200"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-OUTER-MEM"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7200

`reaction.ecocyc.RXN0-7200`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7200`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-OUTER-MEM

## Enriched Summary

Nucleotides -> Nucleotides; direction=REVERSIBLE EcoCyc reaction equation: Nucleotides -> Nucleotides; direction=REVERSIBLE.

## Biological Role

Catalyzed by outer membrane porin PhoE (complex.ecocyc.CPLX0-7530), outer membrane porin C (complex.ecocyc.CPLX0-7533), outer membrane porin F (complex.ecocyc.CPLX0-7534). Substrates: a nucleotide (molecule.ecocyc.Nucleotides). Products: a nucleotide (molecule.ecocyc.Nucleotides).

## Annotation

Nucleotides -> Nucleotides; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7530|complex.ecocyc.CPLX0-7530]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7533|complex.ecocyc.CPLX0-7533]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7534|complex.ecocyc.CPLX0-7534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Nucleotides|molecule.ecocyc.Nucleotides]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Nucleotides|molecule.ecocyc.Nucleotides]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-7200`

## Notes

Nucleotides -> Nucleotides; direction=REVERSIBLE
