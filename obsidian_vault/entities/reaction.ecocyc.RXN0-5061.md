---
entity_id: "reaction.ecocyc.RXN0-5061"
entity_type: "reaction"
name: "RXN0-5061"
source_database: "EcoCyc"
source_id: "RXN0-5061"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5061

`reaction.ecocyc.RXN0-5061`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5061`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-929 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-930 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-929 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-930 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaF (protein.P37692). Substrates: ADP-L-glycero-beta-D-manno-heptose (molecule.C06398), α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD0-929). Products: ADP (molecule.C00008), H+ (molecule.C00080), α-Hep-(1→3)-α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD0-930).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD0-929 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-930 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P37692|protein.P37692]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD0-930|molecule.ecocyc.CPD0-930]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C06398|molecule.C06398]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-929|molecule.ecocyc.CPD0-929]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-5061`

## Notes

CPD0-929 + ADP-L-GLYCERO-D-MANNO-HEPTOSE -> PROTON + CPD0-930 + ADP; direction=PHYSIOL-LEFT-TO-RIGHT
