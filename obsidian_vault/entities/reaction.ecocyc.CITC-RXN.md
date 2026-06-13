---
entity_id: "reaction.ecocyc.CITC-RXN"
entity_type: "reaction"
name: "CITC-RXN"
source_database: "EcoCyc"
source_id: "CITC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "CITRATE LYASE SYNTHETASE"
  - "CITRATE LYASE LIGASE"
---

# CITC-RXN

`reaction.ecocyc.CITC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CITC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction activates citrate lyase by acetylation. EcoCyc reaction equation: HOLO-CITRATE-LYASE + ACET + ATP -> CITRATE-LYASE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction activates citrate lyase by acetylation.

## Biological Role

Catalyzed by citC (protein.P77390). Substrates: ATP (molecule.C00002), Acetate (molecule.C00033). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020).

## Enriched Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Annotation

This reaction activates citrate lyase by acetylation.

## Pathways

- `ecocyc.P2-PWY` citrate lyase activation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P77390|protein.P77390]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00033|molecule.C00033]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:CITC-RXN`

## Notes

HOLO-CITRATE-LYASE + ACET + ATP -> CITRATE-LYASE + PPI + AMP; direction=PHYSIOL-LEFT-TO-RIGHT
