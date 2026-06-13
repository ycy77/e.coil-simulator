---
entity_id: "reaction.ecocyc.UDPGLUCEPIM-RXN"
entity_type: "reaction"
name: "UDPGLUCEPIM-RXN"
source_database: "EcoCyc"
source_id: "UDPGLUCEPIM-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPGLUCEPIM-RXN

`reaction.ecocyc.UDPGLUCEPIM-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPGLUCEPIM-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Part of galactose, galactoside and glucose catabolism. EcoCyc reaction equation: CPD-12575 -> CPD-14553; direction=REVERSIBLE. Part of galactose, galactoside and glucose catabolism.

## Biological Role

Catalyzed by UDP-glucose 4-epimerase (complex.ecocyc.UDPGLUCEPIM-CPLX). Substrates: UDP-glucose (molecule.C00029). Products: UDP-alpha-D-galactose (molecule.C00052).

## Enriched Pathways

- `ecocyc.COLANSYN-PWY` colanic acid building blocks biosynthesis (EcoCyc)
- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)
- `ecocyc.PWY-7344` UDP-α-D-galactose biosynthesis (EcoCyc)

## Annotation

Part of galactose, galactoside and glucose catabolism.

## Pathways

- `ecocyc.COLANSYN-PWY` colanic acid building blocks biosynthesis (EcoCyc)
- `ecocyc.PWY-6317` D-galactose degradation I (Leloir pathway) (EcoCyc)
- `ecocyc.PWY-7344` UDP-α-D-galactose biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[complex.ecocyc.UDPGLUCEPIM-CPLX|complex.ecocyc.UDPGLUCEPIM-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00052|molecule.C00052]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00029|molecule.C00029]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00105|molecule.C00105]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-13245|molecule.ecocyc.CPD-13245]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1314|molecule.ecocyc.CPD0-1314]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1315|molecule.ecocyc.CPD0-1315]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1324|molecule.ecocyc.CPD0-1324]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1325|molecule.ecocyc.CPD0-1325]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1326|molecule.ecocyc.CPD0-1326]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1898|molecule.ecocyc.CPD0-1898]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:UDPGLUCEPIM-RXN`

## Notes

CPD-12575 -> CPD-14553; direction=REVERSIBLE
