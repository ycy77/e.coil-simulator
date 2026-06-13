---
entity_id: "reaction.ecocyc.GLYCOGEN-BRANCH-RXN"
entity_type: "reaction"
name: "GLYCOGEN-BRANCH-RXN"
source_database: "EcoCyc"
source_id: "GLYCOGEN-BRANCH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLYCOGEN-BRANCH-RXN

`reaction.ecocyc.GLYCOGEN-BRANCH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLYCOGEN-BRANCH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Converts amylose into amylopectin. The accepted name requires a qualification depending on the product, glycogen or amylopectin, e.g. glycogen branching enzyme, amylopectin branching enzyme. The latter has frequently been termed Q-enzyme. EcoCyc reaction equation: 1-4-alpha-D-Glucan -> Glycogens; direction=PHYSIOL-LEFT-TO-RIGHT. Converts amylose into amylopectin. The accepted name requires a qualification depending on the product, glycogen or amylopectin, e.g. glycogen branching enzyme, amylopectin branching enzyme. The latter has frequently been termed Q-enzyme.

## Biological Role

Catalyzed by glgB (protein.P07762). Substrates: Amylose (molecule.C00718). Products: a glycogen (molecule.ecocyc.Glycogens).

## Enriched Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Annotation

Converts amylose into amylopectin. The accepted name requires a qualification depending on the product, glycogen or amylopectin, e.g. glycogen branching enzyme, amylopectin branching enzyme. The latter has frequently been termed Q-enzyme.

## Pathways

- `ecocyc.GLYCOGENSYNTH-PWY` glycogen biosynthesis I (from ADP-D-Glucose) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[protein.P07762|protein.P07762]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.Glycogens|molecule.ecocyc.Glycogens]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00718|molecule.C00718]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:GLYCOGEN-BRANCH-RXN`

## Notes

1-4-alpha-D-Glucan -> Glycogens; direction=PHYSIOL-LEFT-TO-RIGHT
