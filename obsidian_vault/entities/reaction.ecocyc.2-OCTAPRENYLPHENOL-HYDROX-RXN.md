---
entity_id: "reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN"
entity_type: "reaction"
name: "2-OCTAPRENYLPHENOL-HYDROX-RXN"
source_database: "EcoCyc"
source_id: "2-OCTAPRENYLPHENOL-HYDROX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-OCTAPRENYLPHENOL-HYDROX-RXN

`reaction.ecocyc.2-OCTAPRENYLPHENOL-HYDROX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-OCTAPRENYLPHENOL-HYDROX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fourth step in ubiquinone biosynthesis. The pathway is still under investigation, therefore not all of the steps have been thoroughly characterized. EcoCyc reaction equation: 2-OCTAPRENYLPHENOL + OXYGEN-MOLECULE + NADPH + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fourth step in ubiquinone biosynthesis. The pathway is still under investigation, therefore not all of the steps have been thoroughly characterized.

## Biological Role

Catalyzed by ubiI (protein.P25535). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080), 2-(all-trans-octaprenyl)phenol (molecule.ecocyc.2-OCTAPRENYLPHENOL). Products: H2O (molecule.C00001), NADP+ (molecule.C00006), 3-(all-trans-octaprenyl)benzene-1,2-diol (molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Annotation

This is the fourth step in ubiquinone biosynthesis. The pathway is still under investigation, therefore not all of the steps have been thoroughly characterized.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P25535|protein.P25535]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL|molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-OCTAPRENYLPHENOL|molecule.ecocyc.2-OCTAPRENYLPHENOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-OCTAPRENYLPHENOL-HYDROX-RXN`

## Notes

2-OCTAPRENYLPHENOL + OXYGEN-MOLECULE + NADPH + PROTON -> 2-OCTAPRENYL-6-HYDROXYPHENOL + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT
