---
entity_id: "reaction.ecocyc.TRANS-RXN0-590"
entity_type: "reaction"
name: "deoxycholate diffusion"
source_database: "EcoCyc"
source_id: "TRANS-RXN0-590"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# deoxycholate diffusion

`reaction.ecocyc.TRANS-RXN0-590`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN0-590`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and thus should be able to cross the cytoplasmic membrane . EcoCyc reaction equation: DEOXYCHOLATE -> DEOXYCHOLATE; direction=LEFT-TO-RIGHT. In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and thus should be able to cross the cytoplasmic membrane .

## Biological Role

Substrates: Deoxycholic acid (molecule.C04483). Products: Deoxycholic acid (molecule.C04483).

## Annotation

In the acidic pH of the bacterial periplasm, unconjugated bile acids exist largely in an uncharged, protonated form and thus should be able to cross the cytoplasmic membrane .

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN0-590`

## Notes

DEOXYCHOLATE -> DEOXYCHOLATE; direction=LEFT-TO-RIGHT
