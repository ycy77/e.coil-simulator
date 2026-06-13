---
entity_id: "reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN"
entity_type: "reaction"
name: "3-ISOPROPYLMALDEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "3-ISOPROPYLMALDEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-ISOPROPYLMALDEHYDROG-RXN

`reaction.ecocyc.3-ISOPROPYLMALDEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-ISOPROPYLMALDEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the third step in leucine biosynthesis after the fork from valine synthesis. It is an oxidative decarboxylation. EcoCyc reaction equation: 2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> CPD-7100 + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This is the third step in leucine biosynthesis after the fork from valine synthesis. It is an oxidative decarboxylation.

## Biological Role

Substrates: NAD+ (molecule.C00003), (2R,3S)-3-Isopropylmalate (molecule.C04411). Products: NADH (molecule.C00004), H+ (molecule.C00080), (2S)-2-Isopropyl-3-oxosuccinate (molecule.C04236).

## Enriched Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Annotation

This is the third step in leucine biosynthesis after the fork from valine synthesis. It is an oxidative decarboxylation.

## Pathways

- `ecocyc.LEUSYN-PWY` L-leucine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04236|molecule.C04236]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04411|molecule.C04411]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3-ISOPROPYLMALDEHYDROG-RXN`

## Notes

2-D-THREO-HYDROXY-3-CARBOXY-ISOCAPROATE + NAD -> CPD-7100 + NADH + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
