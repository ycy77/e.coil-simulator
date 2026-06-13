---
entity_id: "reaction.ecocyc.RXN0-5144"
entity_type: "reaction"
name: "RXN0-5144"
source_database: "EcoCyc"
source_id: "RXN0-5144"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-5144

`reaction.ecocyc.RXN0-5144`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-5144`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-ADENOSYLMETHIONINE + tRNA-Containing-5AminoMe-2-ThioUrdines -> ADENOSYL-HOMO-CYS + tRNA-Containing-5MeAminoMe-2-ThioU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: S-ADENOSYLMETHIONINE + tRNA-Containing-5AminoMe-2-ThioUrdines -> ADENOSYL-HOMO-CYS + tRNA-Containing-5MeAminoMe-2-ThioU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mnmC (protein.P77182). Substrates: S-Adenosyl-L-methionine (molecule.C00019), a 5-(aminomethyl)-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), a 5-[(methylamino)methyl]-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

S-ADENOSYLMETHIONINE + tRNA-Containing-5AminoMe-2-ThioUrdines -> ADENOSYL-HOMO-CYS + tRNA-Containing-5MeAminoMe-2-ThioU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P77182|protein.P77182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU|molecule.ecocyc.tRNA-Containing-5MeAminoMe-2-ThioU]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines|molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-5144`

## Notes

S-ADENOSYLMETHIONINE + tRNA-Containing-5AminoMe-2-ThioUrdines -> ADENOSYL-HOMO-CYS + tRNA-Containing-5MeAminoMe-2-ThioU + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
