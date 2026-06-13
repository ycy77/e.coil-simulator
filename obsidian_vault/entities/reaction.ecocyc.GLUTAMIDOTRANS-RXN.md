---
entity_id: "reaction.ecocyc.GLUTAMIDOTRANS-RXN"
entity_type: "reaction"
name: "GLUTAMIDOTRANS-RXN"
source_database: "EcoCyc"
source_id: "GLUTAMIDOTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# GLUTAMIDOTRANS-RXN

`reaction.ecocyc.GLUTAMIDOTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:GLUTAMIDOTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The reactions generally known as the fifth and sixth steps in the histidine synthesis pathway are parts of one overall reaction that has subreactions. The reaction takes place in at least two steps, the first of which is an amidation and the second includes cyclization and ring closure, involving carbon-nitrogen ligation. EcoCyc reaction equation: PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + GLN -> PROTON + GLT + D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR; direction=PHYSIOL-LEFT-TO-RIGHT. The reactions generally known as the fifth and sixth steps in the histidine synthesis pathway are parts of one overall reaction that has subreactions. The reaction takes place in at least two steps, the first of which is an amidation and the second includes cyclization and ring closure, involving carbon-nitrogen ligation.

## Biological Role

Catalyzed by imidazole glycerol phosphate synthase (complex.ecocyc.GLUTAMIDOTRANS-CPLX). Substrates: L-Glutamine (molecule.C00064), N-(5'-Phospho-D-1'-ribulosylformimino)-5-amino-1-(5''-phospho-D-ribosyl)-4-imidazolecarboxamide (molecule.C04916). Products: L-Glutamate (molecule.C00025), H+ (molecule.C00080), D-erythro-1-(Imidazol-4-yl)glycerol 3-phosphate (molecule.C04666), 1-(5'-Phosphoribosyl)-5-amino-4-imidazolecarboxamide (molecule.C04677).

## Enriched Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Annotation

The reactions generally known as the fifth and sixth steps in the histidine synthesis pathway are parts of one overall reaction that has subreactions. The reaction takes place in at least two steps, the first of which is an amidation and the second includes cyclization and ring closure, involving carbon-nitrogen ligation.

## Pathways

- `ecocyc.HISTSYN-PWY` L-histidine biosynthesis (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (9)

- `catalyzes` <-- [[complex.ecocyc.GLUTAMIDOTRANS-CPLX|complex.ecocyc.GLUTAMIDOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04666|molecule.C04666]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C04677|molecule.C04677]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C04916|molecule.C04916]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:GLUTAMIDOTRANS-RXN`

## Notes

PHOSPHORIBULOSYL-FORMIMINO-AICAR-P + GLN -> PROTON + GLT + D-ERYTHRO-IMIDAZOLE-GLYCEROL-P + AICAR; direction=PHYSIOL-LEFT-TO-RIGHT
