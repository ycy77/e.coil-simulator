---
entity_id: "reaction.ecocyc.TRANS-RXN-86"
entity_type: "reaction"
name: "TRANS-RXN-86"
source_database: "EcoCyc"
source_id: "TRANS-RXN-86"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-86

`reaction.ecocyc.TRANS-RXN-86`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-86`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=REVERSIBLE EcoCyc reaction equation: Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=REVERSIBLE.

## Biological Role

Catalyzed by small conductance mechanosensitive channel MscS (complex.ecocyc.CPLX0-7626), large conductance mechanosensitive channel (complex.ecocyc.CPLX0-7627), mscK (protein.P77338). Substrates: non-specific ion/solute (molecule.ecocyc.Unspecified-Ion-Or-Solute). Products: non-specific ion/solute (molecule.ecocyc.Unspecified-Ion-Or-Solute).

## Annotation

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `activates` <-- [[molecule.ecocyc.CPD-3781|molecule.ecocyc.CPD-3781]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-3782|molecule.ecocyc.CPD-3782]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD-3783|molecule.ecocyc.CPD-3783]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.a-methyl-beta-cyclodextrin|molecule.ecocyc.a-methyl-beta-cyclodextrin]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7626|complex.ecocyc.CPLX0-7626]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7627|complex.ecocyc.CPLX0-7627]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77338|protein.P77338]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Unspecified-Ion-Or-Solute|molecule.ecocyc.Unspecified-Ion-Or-Solute]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Unspecified-Ion-Or-Solute|molecule.ecocyc.Unspecified-Ion-Or-Solute]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-86`

## Notes

Unspecified-Ion-Or-Solute -> Unspecified-Ion-Or-Solute; direction=REVERSIBLE
