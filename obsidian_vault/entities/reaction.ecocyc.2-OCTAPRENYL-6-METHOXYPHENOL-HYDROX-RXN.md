---
entity_id: "reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN"
entity_type: "reaction"
name: "2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN"
source_database: "EcoCyc"
source_id: "2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN

`reaction.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the sixth step in ubiquinone biosynthesis. EcoCyc reaction equation: 2-OCTAPRENYL-6-METHOXYPHENOL + OXYGEN-MOLECULE + NADPH + PROTON -> OCTAPRENYL-METHOXY-BENZOQUINONE + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the sixth step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiH (protein.P25534). Substrates: NADPH (molecule.C00005), Oxygen (molecule.C00007), H+ (molecule.C00080), 2-methoxy-6-(all-trans-octaprenyl)phenol (molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL). Products: H2O (molecule.C00001), NADP+ (molecule.C00006), 2-methoxy-6-(all trans-octaprenyl)benzene-1,4-diol (molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Annotation

This is the sixth step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (8)

- `catalyzes` <-- [[protein.P25534|protein.P25534]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00006|molecule.C00006]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE|molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00005|molecule.C00005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00007|molecule.C00007]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL|molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-OCTAPRENYL-6-METHOXYPHENOL-HYDROX-RXN`

## Notes

2-OCTAPRENYL-6-METHOXYPHENOL + OXYGEN-MOLECULE + NADPH + PROTON -> OCTAPRENYL-METHOXY-BENZOQUINONE + WATER + NADP; direction=PHYSIOL-LEFT-TO-RIGHT
