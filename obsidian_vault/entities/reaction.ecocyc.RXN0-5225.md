---
entity_id: "reaction.ecocyc.RXN0-5225"
entity_type: "reaction"
name: "RXN0-5225"
source_database: "EcoCyc"
source_id: "RXN0-5225"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5225

`reaction.ecocyc.RXN0-5225`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5225`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-1080 + WATER -> CPD0-1081 + CPD0-1082; direction=LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-1080 + WATER -> CPD0-1081 + CPD0-1082; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by ampD (protein.P13016), amiD (protein.P75820). Substrates: H2O (molecule.C00001), GlcNAc-1,6-anhMurNAc-L-Ala-γ-D-Glu-meso-DAP-D-Ala (molecule.ecocyc.CPD0-1080). Products: N-acetyl-β-D-glucosamine-1,6-anhydro-N-acetyl-β-D-muramate (molecule.ecocyc.CPD0-1081), L-alanyl-γ-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanine (molecule.ecocyc.CPD0-1082).

## Enriched Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Annotation

CPD0-1080 + WATER -> CPD0-1081 + CPD0-1082; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1261` peptidoglycan recycling I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P13016|protein.P13016]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P75820|protein.P75820]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1081|molecule.ecocyc.CPD0-1081]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-1082|molecule.ecocyc.CPD0-1082]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-1080|molecule.ecocyc.CPD0-1080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5225`

## Notes

CPD0-1080 + WATER -> CPD0-1081 + CPD0-1082; direction=LEFT-TO-RIGHT
