---
entity_id: "reaction.ecocyc.RXN0-5118"
entity_type: "reaction"
name: "RXN0-5118"
source_database: "EcoCyc"
source_id: "RXN0-5118"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5118

`reaction.ecocyc.RXN0-5118`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5118`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

KDO2-LIPID-A + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD0-929 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: KDO2-LIPID-A + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD0-929 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaC (protein.P24173). Substrates: KDO2-lipid A (molecule.C06026), ADP-L-glycero-beta-D-manno-heptose (molecule.C06398). Products: ADP (molecule.C00008), H+ (molecule.C00080), α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD0-929).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

KDO2-LIPID-A + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD0-929 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P24173|protein.P24173]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-929|molecule.ecocyc.CPD0-929]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06026|molecule.C06026]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5118`

## Notes

KDO2-LIPID-A + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> CPD0-929 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
