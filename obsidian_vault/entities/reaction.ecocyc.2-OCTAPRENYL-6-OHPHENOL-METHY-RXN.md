---
entity_id: "reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN"
entity_type: "reaction"
name: "2-octaprenyl-6-hydroxyphenyl methylase"
source_database: "EcoCyc"
source_id: "2-OCTAPRENYL-6-OHPHENOL-METHY-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-octaprenyl-6-hydroxyphenyl methylase

`reaction.ecocyc.2-OCTAPRENYL-6-OHPHENOL-METHY-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:2-OCTAPRENYL-6-OHPHENOL-METHY-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the fifth step in ubiquinone biosynthesis. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + 2-OCTAPRENYL-6-HYDROXYPHENOL -> PROTON + 2-OCTAPRENYL-6-METHOXYPHENOL + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This is the fifth step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiG (protein.P17993). Substrates: S-Adenosyl-L-methionine (molecule.C00019), 3-(all-trans-octaprenyl)benzene-1,2-diol (molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), 2-methoxy-6-(all-trans-octaprenyl)phenol (molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

This is the fifth step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P17993|protein.P17993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL|molecule.ecocyc.2-OCTAPRENYL-6-METHOXYPHENOL]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL|molecule.ecocyc.2-OCTAPRENYL-6-HYDROXYPHENOL]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:2-OCTAPRENYL-6-OHPHENOL-METHY-RXN`

## Notes

S-ADENOSYLMETHIONINE + 2-OCTAPRENYL-6-HYDROXYPHENOL -> PROTON + 2-OCTAPRENYL-6-METHOXYPHENOL + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
