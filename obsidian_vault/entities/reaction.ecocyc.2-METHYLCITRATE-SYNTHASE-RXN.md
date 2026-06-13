---
entity_id: "reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN"
entity_type: "reaction"
name: "2-METHYLCITRATE-SYNTHASE-RXN"
source_database: "EcoCyc"
source_id: "2-METHYLCITRATE-SYNTHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-METHYLCITRATE-SYNTHASE-RXN

`reaction.ecocyc.2-METHYLCITRATE-SYNTHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-METHYLCITRATE-SYNTHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

OXALACETIC_ACID + WATER + PROPIONYL-COA -> PROTON + CPD-622 + CO-A; direction=LEFT-TO-RIGHT EcoCyc reaction equation: OXALACETIC_ACID + WATER + PROPIONYL-COA -> PROTON + CPD-622 + CO-A; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by 2-methylcitrate synthase (complex.ecocyc.CPLX0-251). Substrates: H2O (molecule.C00001), Oxaloacetate (molecule.C00036), Propanoyl-CoA (molecule.C00100). Products: CoA (molecule.C00010), H+ (molecule.C00080), (2S,3S)-2-methylcitrate (molecule.ecocyc.CPD-622).

## Enriched Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Annotation

OXALACETIC_ACID + WATER + PROPIONYL-COA -> PROTON + CPD-622 + CO-A; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-42` 2-methylcitrate cycle I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-251|complex.ecocyc.CPLX0-251]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-622|molecule.ecocyc.CPD-622]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00100|molecule.C00100]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-METHYLCITRATE-SYNTHASE-RXN`

## Notes

OXALACETIC_ACID + WATER + PROPIONYL-COA -> PROTON + CPD-622 + CO-A; direction=LEFT-TO-RIGHT
