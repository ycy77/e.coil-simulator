---
entity_id: "reaction.ecocyc.RXN0-7081"
entity_type: "reaction"
name: "RXN0-7081"
source_database: "EcoCyc"
source_id: "RXN0-7081"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# RXN0-7081

`reaction.ecocyc.RXN0-7081`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN0-7081`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A tentative reaction mechanism, including production of glyoxylate, was proposed by . EcoCyc reaction equation: tRNA-containing-5-CarbMeAminome-2-ThioU + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + GLYOX + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT. A tentative reaction mechanism, including production of glyoxylate, was proposed by .

## Biological Role

Catalyzed by mnmC (protein.P77182). Substrates: H2O (molecule.C00001), a 5-carboxymethylaminomethyl-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-containing-5-CarbMeAminome-2-ThioU). Products: Glyoxylate (molecule.C00048), a 5-(aminomethyl)-2-thiouridine34 in tRNA (molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines).

## Enriched Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Annotation

A tentative reaction mechanism, including production of glyoxylate, was proposed by .

## Pathways

- `ecocyc.PWY-7892` tRNA-uridine34 modifications (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P77182|protein.P77182]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines|molecule.ecocyc.tRNA-Containing-5AminoMe-2-ThioUrdines]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.tRNA-containing-5-CarbMeAminome-2-ThioU|molecule.ecocyc.tRNA-containing-5-CarbMeAminome-2-ThioU]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:RXN0-7081`

## Notes

tRNA-containing-5-CarbMeAminome-2-ThioU + WATER + Acceptor -> tRNA-Containing-5AminoMe-2-ThioUrdines + GLYOX + Donor-H2; direction=PHYSIOL-LEFT-TO-RIGHT
