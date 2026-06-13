---
entity_id: "reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN"
entity_type: "reaction"
name: "ALCOHOL-DEHYDROG-GENERIC-RXN"
source_database: "EcoCyc"
source_id: "ALCOHOL-DEHYDROG-GENERIC-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALCOHOL-DEHYDROG-GENERIC-RXN

`reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALCOHOL-DEHYDROG-GENERIC-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Acts on primary or secondary alcohols or hemiacetals. EcoCyc reaction equation: Primary-Alcohols + NAD -> Aldehydes + NADH + PROTON; direction=REVERSIBLE. Acts on primary or secondary alcohols or hemiacetals.

## Biological Role

Catalyzed by fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase (complex.ecocyc.ADHE-CPLX), ethanol dehydrogenase / alcohol dehydrogenase (complex.ecocyc.CPLX0-8015). Substrates: NAD+ (molecule.C00003), Primary alcohol (molecule.C00226). Products: NADH (molecule.C00004), Aldehyde (molecule.C00071), H+ (molecule.C00080).

## Annotation

Acts on primary or secondary alcohols or hemiacetals.

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.ADHE-CPLX|complex.ecocyc.ADHE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8015|complex.ecocyc.CPLX0-8015]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00071|molecule.C00071]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00226|molecule.C00226]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ALCOHOL-DEHYDROG-GENERIC-RXN`

## Notes

Primary-Alcohols + NAD -> Aldehydes + NADH + PROTON; direction=REVERSIBLE
