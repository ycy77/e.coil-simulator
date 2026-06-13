---
entity_id: "reaction.ecocyc.RXN-17897"
entity_type: "reaction"
name: "RXN-17897"
source_database: "EcoCyc"
source_id: "RXN-17897"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-17897

`reaction.ecocyc.RXN-17897`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-17897`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Reduced-ferredoxins + NADP + PROTON -> Oxidized-ferredoxins + NADPH; direction=REVERSIBLE EcoCyc reaction equation: Reduced-ferredoxins + NADP + PROTON -> Oxidized-ferredoxins + NADPH; direction=REVERSIBLE.

## Biological Role

Catalyzed by fpr (protein.P28861). Substrates: NADP+ (molecule.C00006), H+ (molecule.C00080). Products: NADPH (molecule.C00005).

## Annotation

Reduced-ferredoxins + NADP + PROTON -> Oxidized-ferredoxins + NADPH; direction=REVERSIBLE

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P28861|protein.P28861]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-17897`

## Notes

Reduced-ferredoxins + NADP + PROTON -> Oxidized-ferredoxins + NADPH; direction=REVERSIBLE
