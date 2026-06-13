---
entity_id: "reaction.ecocyc.RXN0-1861"
entity_type: "reaction"
name: "RXN0-1861"
source_database: "EcoCyc"
source_id: "RXN0-1861"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-1861

`reaction.ecocyc.RXN0-1861`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-1861`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-GLUCURONATE + NAD -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT EcoCyc reaction equation: UDP-GLUCURONATE + NAD -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT.

## Biological Role

Catalyzed by UDP-4-amino-4-deoxy-L-arabinose formyltransferase/UDP-glucuronate dehydrogenase (complex.ecocyc.CPLX0-7718). Substrates: NAD+ (molecule.C00003), UDP-glucuronate (molecule.C00167). Products: NADH (molecule.C00004), CO2 (molecule.C00011), UDP-L-Ara4O (molecule.C16155).

## Enriched Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Annotation

UDP-GLUCURONATE + NAD -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY0-1338` polymyxin resistance (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7718|complex.ecocyc.CPLX0-7718]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16155|molecule.C16155]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00167|molecule.C00167]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-1861`

## Notes

UDP-GLUCURONATE + NAD -> 5-BETA-L-THREO-PENTAPYRANOSYL-4-ULOSE- + CARBON-DIOXIDE + NADH; direction=LEFT-TO-RIGHT
