---
entity_id: "reaction.ecocyc.DEPHOSICITDEHASE-RXN"
entity_type: "reaction"
name: "dephosphorylation of isocitrate dehydrogenase enzyme"
source_database: "EcoCyc"
source_id: "DEPHOSICITDEHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# dephosphorylation of isocitrate dehydrogenase enzyme

`reaction.ecocyc.DEPHOSICITDEHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DEPHOSICITDEHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

WATER + Iso-Cit -> isocitrate-dehydrogenase + Pi; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: WATER + Iso-Cit -> isocitrate-dehydrogenase + Pi; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by isocitrate dehydrogenase kinase / isocitrate dehydrogenase phosphatase (complex.ecocyc.CPLX0-230). Substrates: H2O (molecule.C00001). Products: phosphate (molecule.ecocyc.Pi).

## Annotation

WATER + Iso-Cit -> isocitrate-dehydrogenase + Pi; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (13)

- `activates` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00036|molecule.C00036]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00197|molecule.C00197]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00311|molecule.C00311]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.CPLX0-230|complex.ecocyc.CPLX0-230]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:DEPHOSICITDEHASE-RXN`

## Notes

WATER + Iso-Cit -> isocitrate-dehydrogenase + Pi; direction=PHYSIOL-LEFT-TO-RIGHT
