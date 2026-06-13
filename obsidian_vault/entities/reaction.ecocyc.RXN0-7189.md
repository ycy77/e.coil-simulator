---
entity_id: "reaction.ecocyc.RXN0-7189"
entity_type: "reaction"
name: "RXN0-7189"
source_database: "EcoCyc"
source_id: "RXN0-7189"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7189

`reaction.ecocyc.RXN0-7189`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7189`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Sugar-alcohols -> Sugar-alcohols; direction=REVERSIBLE EcoCyc reaction equation: Sugar-alcohols -> Sugar-alcohols; direction=REVERSIBLE.

## Biological Role

Catalyzed by glycerol facilitator (complex.ecocyc.CPLX0-7654). Substrates: an alditol (molecule.ecocyc.Sugar-alcohols). Products: an alditol (molecule.ecocyc.Sugar-alcohols).

## Annotation

Sugar-alcohols -> Sugar-alcohols; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7654|complex.ecocyc.CPLX0-7654]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Sugar-alcohols|molecule.ecocyc.Sugar-alcohols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Sugar-alcohols|molecule.ecocyc.Sugar-alcohols]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.HG_2|molecule.ecocyc.HG_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7189`

## Notes

Sugar-alcohols -> Sugar-alcohols; direction=REVERSIBLE
