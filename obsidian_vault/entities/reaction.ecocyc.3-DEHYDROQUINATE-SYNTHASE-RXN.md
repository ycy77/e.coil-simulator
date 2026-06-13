---
entity_id: "reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN"
entity_type: "reaction"
name: "3-DEHYDROQUINATE-SYNTHASE-RXN"
source_database: "EcoCyc"
source_id: "3-DEHYDROQUINATE-SYNTHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3-DEHYDROQUINATE-SYNTHASE-RXN

`reaction.ecocyc.3-DEHYDROQUINATE-SYNTHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3-DEHYDROQUINATE-SYNTHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The hydrogen atoms on C-7 of the substrate are retained on C-2 of the product . This is the second step in the shikimate pathway EcoCyc reaction equation: 3-DEOXY-D-ARABINO-HEPTULOSONATE-7-P -> Pi + DEHYDROQUINATE; direction=PHYSIOL-LEFT-TO-RIGHT. The hydrogen atoms on C-7 of the substrate are retained on C-2 of the product . This is the second step in the shikimate pathway

## Biological Role

Catalyzed by aroB (protein.P07639). Substrates: 2-Dehydro-3-deoxy-D-arabino-heptonate 7-phosphate (molecule.C04691). Products: 3-Dehydroquinate (molecule.C00944), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6164` 3-dehydroquinate biosynthesis I (EcoCyc)

## Annotation

The hydrogen atoms on C-7 of the substrate are retained on C-2 of the product . This is the second step in the shikimate pathway

## Pathways

- `ecocyc.PWY-6164` 3-dehydroquinate biosynthesis I (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `catalyzes` <-- [[protein.P07639|protein.P07639]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00944|molecule.C00944]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C04691|molecule.C04691]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C04691|molecule.C04691]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1370|molecule.ecocyc.CPD0-1370]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1372|molecule.ecocyc.CPD0-1372]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1373|molecule.ecocyc.CPD0-1373]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1374|molecule.ecocyc.CPD0-1374]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Oxygen-Substituted-Quinates|molecule.ecocyc.Oxygen-Substituted-Quinates]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:3-DEHYDROQUINATE-SYNTHASE-RXN`

## Notes

3-DEOXY-D-ARABINO-HEPTULOSONATE-7-P -> Pi + DEHYDROQUINATE; direction=PHYSIOL-LEFT-TO-RIGHT
