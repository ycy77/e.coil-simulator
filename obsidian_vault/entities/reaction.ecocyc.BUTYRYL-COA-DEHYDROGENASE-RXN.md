---
entity_id: "reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN"
entity_type: "reaction"
name: "butanoyl-CoA:electron-transfer flavoprotein 2,3-oxidoreductase"
source_database: "EcoCyc"
source_id: "BUTYRYL-COA-DEHYDROGENASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# butanoyl-CoA:electron-transfer flavoprotein 2,3-oxidoreductase

`reaction.ecocyc.BUTYRYL-COA-DEHYDROGENASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:BUTYRYL-COA-DEHYDROGENASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

BUTYRYL-COA + ETF-Oxidized + PROTON -> CROTONYL-COA + ETF-Reduced; direction=REVERSIBLE EcoCyc reaction equation: BUTYRYL-COA + ETF-Oxidized + PROTON -> CROTONYL-COA + ETF-Reduced; direction=REVERSIBLE.

## Biological Role

Substrates: H+ (molecule.C00080), Butanoyl-CoA (molecule.C00136). Products: Crotonoyl-CoA (molecule.C00877).

## Enriched Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Annotation

BUTYRYL-COA + ETF-Oxidized + PROTON -> CROTONYL-COA + ETF-Reduced; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY0-1337` oleate β-oxidation (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_product_of` <-- [[molecule.C00877|molecule.C00877]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00136|molecule.C00136]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:BUTYRYL-COA-DEHYDROGENASE-RXN`

## Notes

BUTYRYL-COA + ETF-Oxidized + PROTON -> CROTONYL-COA + ETF-Reduced; direction=REVERSIBLE
