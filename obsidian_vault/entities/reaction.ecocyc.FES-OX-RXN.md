---
entity_id: "reaction.ecocyc.FES-OX-RXN"
entity_type: "reaction"
name: "FES-OX-RXN"
source_database: "EcoCyc"
source_id: "FES-OX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# FES-OX-RXN

`reaction.ecocyc.FES-OX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:FES-OX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

FeS-Proteins-Reduced + PROTON + Ox-Ubiquinone-8-Oxidoreductases -> PROTON + FeS-Proteins + Red-Ubiquinol-8-Oxidoreductases; direction=LEFT-TO-RIGHT EcoCyc reaction equation: FeS-Proteins-Reduced + PROTON + Ox-Ubiquinone-8-Oxidoreductases -> PROTON + FeS-Proteins + Red-Ubiquinol-8-Oxidoreductases; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

FeS-Proteins-Reduced + PROTON + Ox-Ubiquinone-8-Oxidoreductases -> PROTON + FeS-Proteins + Red-Ubiquinol-8-Oxidoreductases; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:FES-OX-RXN`

## Notes

FeS-Proteins-Reduced + PROTON + Ox-Ubiquinone-8-Oxidoreductases -> PROTON + FeS-Proteins + Red-Ubiquinol-8-Oxidoreductases; direction=LEFT-TO-RIGHT
