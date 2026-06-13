---
entity_id: "reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN"
entity_type: "reaction"
name: "2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN"
source_database: "EcoCyc"
source_id: "2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN

`reaction.ecocyc.2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the seventh step in ubiquinone biosynthesis. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + OCTAPRENYL-METHOXY-BENZOQUINONE -> PROTON + OCTAPRENYL-METHYL-METHOXY-BENZQ + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This is the seventh step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiE (protein.P0A887). Substrates: S-Adenosyl-L-methionine (molecule.C00019), 2-methoxy-6-(all trans-octaprenyl)benzene-1,4-diol (molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), 5-methoxy-2-methyl-3-(all-trans-octaprenyl)benzene-1,4-diol (molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

This is the seventh step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P0A887|protein.P0A887]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE|molecule.ecocyc.OCTAPRENYL-METHOXY-BENZOQUINONE]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-OCTAPRENYL-METHOXY-BENZOQ-METH-RXN`

## Notes

S-ADENOSYLMETHIONINE + OCTAPRENYL-METHOXY-BENZOQUINONE -> PROTON + OCTAPRENYL-METHYL-METHOXY-BENZQ + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
