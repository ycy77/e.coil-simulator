---
entity_id: "reaction.ecocyc.DMK-FE-RXN"
entity_type: "reaction"
name: "DMK-FE-RXN"
source_database: "EcoCyc"
source_id: "DMK-FE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DMK-FE-RXN

`reaction.ecocyc.DMK-FE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DMK-FE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PROTON + Ox-Demethylmenaquinone-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Demethylmenaquinol-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT EcoCyc reaction equation: PROTON + Ox-Demethylmenaquinone-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Demethylmenaquinol-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT.

## Biological Role

Substrates: H+ (molecule.C00080). Products: H+ (molecule.C00080).

## Annotation

PROTON + Ox-Demethylmenaquinone-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Demethylmenaquinol-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DMK-FE-RXN`

## Notes

PROTON + Ox-Demethylmenaquinone-Oxidoreductases + FeS-Proteins-Reduced -> PROTON + Red-Demethylmenaquinol-Oxidoreductases + FeS-Proteins; direction=LEFT-TO-RIGHT
