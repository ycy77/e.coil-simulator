---
entity_id: "reaction.ecocyc.1.13.11.16-RXN"
entity_type: "reaction"
name: "1.13.11.16-RXN"
source_database: "EcoCyc"
source_id: "1.13.11.16-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 1.13.11.16-RXN

`reaction.ecocyc.1.13.11.16-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:1.13.11.16-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction is where the branched meta-cleavage degradation pathway for 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate meet. EcoCyc reaction equation: 2-3-DIHYDROXYPHENYL-PROPIONATE + OXYGEN-MOLECULE -> PROTON + CPD-157; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction is where the branched meta-cleavage degradation pathway for 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate meet.

## Biological Role

Catalyzed by 3-carboxyethylcatechol 2,3-dioxygenase (complex.ecocyc.DHPDIOXYGEN-CPLX). Substrates: Oxygen (molecule.C00007), 3-(2,3-Dihydroxyphenyl)propanoate (molecule.C04044). Products: H+ (molecule.C00080), 2-Hydroxy-6-oxonona-2,4-diene-1,9-dioate (molecule.C04479).

## Enriched Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Annotation

This reaction is where the branched meta-cleavage degradation pathway for 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate meet.

## Pathways

- `ecocyc.HCAMHPDEG-PWY` 3-phenylpropanoate and 3-(3-hydroxyphenyl)propanoate degradation to 2-hydroxypentadienoate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[complex.ecocyc.DHPDIOXYGEN-CPLX|complex.ecocyc.DHPDIOXYGEN-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04479|molecule.C04479]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04044|molecule.C04044]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.DITHIO-NITROBENZOATE|molecule.ecocyc.DITHIO-NITROBENZOATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PHMB|molecule.ecocyc.PHMB]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:1.13.11.16-RXN`

## Notes

2-3-DIHYDROXYPHENYL-PROPIONATE + OXYGEN-MOLECULE -> PROTON + CPD-157; direction=PHYSIOL-LEFT-TO-RIGHT
