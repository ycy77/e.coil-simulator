---
entity_id: "reaction.ecocyc.RXN0-2023"
entity_type: "reaction"
name: "RXN0-2023"
source_database: "EcoCyc"
source_id: "RXN0-2023"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-2023

`reaction.ecocyc.RXN0-2023`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-2023`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This modification is found at wobble base 34 of tRNA-Lys, tRNA-Glu, and tRNA-Gln . In E. coli, IscS (cysteine desulfurase) and the Tus proteins are necessary to supply the S to MnmA . EcoCyc reaction equation: tRNA-uridine34 + MnmA-Sulfanyl-Cysteine + ATP + Donor-H2 -> tRNA-2-thiouridine34 + MnmA-Cysteine + AMP + PPI + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT. This modification is found at wobble base 34 of tRNA-Lys, tRNA-Glu, and tRNA-Gln . In E. coli, IscS (cysteine desulfurase) and the Tus proteins are necessary to supply the S to MnmA .

## Biological Role

Catalyzed by mnmA (protein.P25745). Substrates: ATP (molecule.C00002), a [tRNA-uridine 2-sulfurtransferase]-S-sulfanyl-L-cysteine (molecule.ecocyc.MnmA-Sulfanyl-Cysteine), a uridine34 in tRNA (molecule.ecocyc.tRNA-uridine34). Products: Diphosphate (molecule.C00013), AMP (molecule.C00020), H+ (molecule.C00080), a [tRNA-uridine 2-sulfurtransferase]-L-cysteine (molecule.ecocyc.MnmA-Cysteine), a 2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-2-thiouridine34).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

This modification is found at wobble base 34 of tRNA-Lys, tRNA-Glu, and tRNA-Gln . In E. coli, IscS (cysteine desulfurase) and the Tus proteins are necessary to supply the S to MnmA .

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[protein.P25745|protein.P25745]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00013|molecule.C00013]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.MnmA-Cysteine|molecule.ecocyc.MnmA-Cysteine]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-2-thiouridine34|molecule.ecocyc.tRNA-2-thiouridine34]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.MnmA-Sulfanyl-Cysteine|molecule.ecocyc.MnmA-Sulfanyl-Cysteine]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-uridine34|molecule.ecocyc.tRNA-uridine34]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN0-2023`

## Notes

tRNA-uridine34 + MnmA-Sulfanyl-Cysteine + ATP + Donor-H2 -> tRNA-2-thiouridine34 + MnmA-Cysteine + AMP + PPI + Acceptor + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
