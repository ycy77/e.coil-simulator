---
entity_id: "reaction.ecocyc.RXN-11832"
entity_type: "reaction"
name: "RXN-11832"
source_database: "EcoCyc"
source_id: "RXN-11832"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-11832

`reaction.ecocyc.RXN-11832`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-11832`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ATP + CMP -> ADP + CDP; direction=REVERSIBLE EcoCyc reaction equation: ATP + CMP -> ADP + CDP; direction=REVERSIBLE.

## Biological Role

Catalyzed by cmk (protein.P0A6I0). Substrates: ATP (molecule.C00002), CMP (molecule.C00055). Products: ADP (molecule.C00008), CDP (molecule.C00112).

## Enriched Pathways

- `ecocyc.PWY-7205` CMP phosphorylation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Annotation

ATP + CMP -> ADP + CDP; direction=REVERSIBLE

## Pathways

- `ecocyc.PWY-7205` CMP phosphorylation (EcoCyc)
- `ecocyc.PWY0-163` salvage pathways of pyrimidine ribonucleotides (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A6I0|protein.P0A6I0]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00112|molecule.C00112]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00055|molecule.C00055]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-11832`

## Notes

ATP + CMP -> ADP + CDP; direction=REVERSIBLE
