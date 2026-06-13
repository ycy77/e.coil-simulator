---
entity_id: "reaction.ecocyc.DHHB-METHYLTRANSFER-RXN"
entity_type: "reaction"
name: "DHHB-METHYLTRANSFER-RXN"
source_database: "EcoCyc"
source_id: "DHHB-METHYLTRANSFER-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# DHHB-METHYLTRANSFER-RXN

`reaction.ecocyc.DHHB-METHYLTRANSFER-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:DHHB-METHYLTRANSFER-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the ninth and final step in ubiquinone biosynthesis. EcoCyc reaction equation: S-ADENOSYLMETHIONINE + OCTAPRENYL-METHYL-OH-METHOXY-BENZQ -> PROTON + CPD-9956 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT. This is the ninth and final step in ubiquinone biosynthesis.

## Biological Role

Catalyzed by ubiG (protein.P17993). Substrates: S-Adenosyl-L-methionine (molecule.C00019), 3-demethylubiquinol-8 (molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ). Products: S-Adenosyl-L-homocysteine (molecule.C00021), H+ (molecule.C00080), ubiquinol-8 (molecule.ecocyc.CPD-9956).

## Enriched Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Annotation

This is the ninth and final step in ubiquinone biosynthesis.

## Pathways

- `ecocyc.PWY-6708` ubiquinol-8 biosynthesis (early decarboxylation) (EcoCyc)
- `ecocyc.PWY-8533` ubiquinol-8 biosynthesis (anaerobic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `activates` <-- [[molecule.ecocyc.DITHIOTHREITOL|molecule.ecocyc.DITHIOTHREITOL]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[protein.P17993|protein.P17993]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00021|molecule.C00021]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-9956|molecule.ecocyc.CPD-9956]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ|molecule.ecocyc.OCTAPRENYL-METHYL-OH-METHOXY-BENZQ]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:DHHB-METHYLTRANSFER-RXN`

## Notes

S-ADENOSYLMETHIONINE + OCTAPRENYL-METHYL-OH-METHOXY-BENZQ -> PROTON + CPD-9956 + ADENOSYL-HOMO-CYS; direction=PHYSIOL-LEFT-TO-RIGHT
