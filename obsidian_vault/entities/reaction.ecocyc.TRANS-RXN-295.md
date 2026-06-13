---
entity_id: "reaction.ecocyc.TRANS-RXN-295"
entity_type: "reaction"
name: "TRANS-RXN-295"
source_database: "EcoCyc"
source_id: "TRANS-RXN-295"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: "CCO-PM-BAC-NEG"
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# TRANS-RXN-295

`reaction.ecocyc.TRANS-RXN-295`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRANS-RXN-295`
- Default state: `active`
- Allowed states: `active|blocked`
- Location: CCO-PM-BAC-NEG

## Enriched Summary

Represents (imperfectly) the flipping of lysophospholipids across the inner membrane. EcoCyc reaction equation: Lysophosphatidylglycerols -> Lysophosphatidylglycerols; direction=REVERSIBLE. Represents (imperfectly) the flipping of lysophospholipids across the inner membrane.

## Biological Role

Catalyzed by lplT (protein.P39196). Substrates: a lysophosphatidylglycerol (molecule.ecocyc.Lysophosphatidylglycerols). Products: a lysophosphatidylglycerol (molecule.ecocyc.Lysophosphatidylglycerols).

## Annotation

Represents (imperfectly) the flipping of lysophospholipids across the inner membrane.

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P39196|protein.P39196]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Lysophosphatidylglycerols|molecule.ecocyc.Lysophosphatidylglycerols]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.ecocyc.Lysophosphatidylglycerols|molecule.ecocyc.Lysophosphatidylglycerols]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:TRANS-RXN-295`

## Notes

Lysophosphatidylglycerols -> Lysophosphatidylglycerols; direction=REVERSIBLE
