---
entity_id: "reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN"
entity_type: "reaction"
name: "OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN"
source_database: "EcoCyc"
source_id: "OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN

`reaction.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the eighth step in ubiquinone biosynthesis. EcoCyc reaction equation: OCTAPRENYL-METHYL-METHOXY-BENZQ + OXYGEN-MOLECULE + Donor-H2 -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT. This is the eighth step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiF (protein.P75728). Substrates: Oxygen (molecule.C00007), 5-methoxy-2-methyl-3-(all-trans-octaprenyl)benzene-1,4-diol (molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ). Products: H2O (molecule.C00001), 3-demethylubiquinol-8 (molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Annotation

This is the eighth step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P75728|protein.P75728]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:OCTAPRENYL-METHYL-METHOXY-BENZOQ-OH-RXN`

## Notes

OCTAPRENYL-METHYL-METHOXY-BENZQ + OXYGEN-MOLECULE + Donor-H2 -> OCTAPRENYL-METHYL-OH-METHOXY-BENZQ + WATER + Acceptor; direction=PHYSIOL-LEFT-TO-RIGHT
