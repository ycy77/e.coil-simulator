---
entity_id: "reaction.ecocyc.RXN-22462"
entity_type: "reaction"
name: "RXN-22462"
source_database: "EcoCyc"
source_id: "RXN-22462"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22462

`reaction.ecocyc.RXN-22462`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22462`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

ADP-L-GLYCERO-D-MANNO-HEPTOSE + CPD-24487 -> CPD-24488 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: ADP-L-GLYCERO-D-MANNO-HEPTOSE + CPD-24487 -> CPD-24488 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaQ (protein.P25742). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398), α-Hep-(1→3)-4-O-phospho-α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD-24487). Products: ADP (molecule.C00008), H+ (molecule.C00080), (heptosyl)3-Kdo2-lipid A-phosphate (E. coli) (molecule.ecocyc.CPD-24488).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

ADP-L-GLYCERO-D-MANNO-HEPTOSE + CPD-24487 -> CPD-24488 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25742|protein.P25742]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24488|molecule.ecocyc.CPD-24488]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD-24487|molecule.ecocyc.CPD-24487]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22462`

## Notes

ADP-L-GLYCERO-D-MANNO-HEPTOSE + CPD-24487 -> CPD-24488 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
