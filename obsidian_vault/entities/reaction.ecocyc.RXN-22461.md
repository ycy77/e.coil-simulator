---
entity_id: "reaction.ecocyc.RXN-22461"
entity_type: "reaction"
name: "RXN-22461"
source_database: "EcoCyc"
source_id: "RXN-22461"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN-22461

`reaction.ecocyc.RXN-22461`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-22461`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

CPD0-930 + ATP -> CPD-24487 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: CPD0-930 + ATP -> CPD-24487 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by waaP (protein.P25741). Substrates: ATP (molecule.C00002), α-Hep-(1→3)-α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD0-930). Products: ADP (molecule.C00008), H+ (molecule.C00080), α-Hep-(1→3)-4-O-phospho-α-Hep-(1→5)-[α-Kdo-(2→4)]-α-Kdo-(2→6)-lipid A (E. coli) (molecule.ecocyc.CPD-24487).

## Enriched Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Annotation

CPD0-930 + ATP -> CPD-24487 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.LIPA-CORESYN-PWY` lipid A-core biosynthesis (E. coli K-12) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25741|protein.P25741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-24487|molecule.ecocyc.CPD-24487]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.CPD0-930|molecule.ecocyc.CPD0-930]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-22461`

## Notes

CPD0-930 + ATP -> CPD-24487 + ADP + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
