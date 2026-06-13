---
entity_id: "reaction.ecocyc.PEPDEPHOS-RXN"
entity_type: "reaction"
name: "PEPDEPHOS-RXN"
source_database: "EcoCyc"
source_id: "PEPDEPHOS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "pyruvate phosphorylation"
---

# PEPDEPHOS-RXN

`reaction.ecocyc.PEPDEPHOS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PEPDEPHOS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

PYRUVATE + ATP -> PROTON + ADP + PHOSPHO-ENOL-PYRUVATE; direction=PHYSIOL-RIGHT-TO-LEFT EcoCyc reaction equation: PYRUVATE + ATP -> PROTON + ADP + PHOSPHO-ENOL-PYRUVATE; direction=PHYSIOL-RIGHT-TO-LEFT.

## Biological Role

Catalyzed by pyruvate kinase 1 (complex.ecocyc.PKI-COMPLEX), pyruvate kinase 2 (complex.ecocyc.PKII-CPLX). Substrates: ATP (molecule.C00002), Pyruvate (molecule.C00022). Products: ADP (molecule.C00008), Phosphoenolpyruvate (molecule.C00074), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

PYRUVATE + ATP -> PROTON + ADP + PHOSPHO-ENOL-PYRUVATE; direction=PHYSIOL-RIGHT-TO-LEFT

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `activates` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00092|molecule.C00092]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00117|molecule.C00117]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[protein.P0AA04|protein.P0AA04]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.PKI-COMPLEX|complex.ecocyc.PKI-COMPLEX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.PKII-CPLX|complex.ecocyc.PKII-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00074|molecule.C00074]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00002|molecule.C00002]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00044|molecule.C00044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00091|molecule.C00091]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PEPDEPHOS-RXN`

## Notes

PYRUVATE + ATP -> PROTON + ADP + PHOSPHO-ENOL-PYRUVATE; direction=PHYSIOL-RIGHT-TO-LEFT
