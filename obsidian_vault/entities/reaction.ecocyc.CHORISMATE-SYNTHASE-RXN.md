---
entity_id: "reaction.ecocyc.CHORISMATE-SYNTHASE-RXN"
entity_type: "reaction"
name: "CHORISMATE-SYNTHASE-RXN"
source_database: "EcoCyc"
source_id: "CHORISMATE-SYNTHASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# CHORISMATE-SYNTHASE-RXN

`reaction.ecocyc.CHORISMATE-SYNTHASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:CHORISMATE-SYNTHASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Shikimate is numbered so that the double-bond is between C-1 and C-2, but some earlier papers numbered the ring in the reverse direction. This reaction is the seventh and final reaction of the shikimate pathway. EcoCyc reaction equation: 3-ENOLPYRUVYL-SHIKIMATE-5P -> Pi + CHORISMATE; direction=PHYSIOL-LEFT-TO-RIGHT. Shikimate is numbered so that the double-bond is between C-1 and C-2, but some earlier papers numbered the ring in the reverse direction. This reaction is the seventh and final reaction of the shikimate pathway.

## Biological Role

Catalyzed by chorismate synthase (complex.ecocyc.AROC-CPLX). Substrates: 5-O-(1-Carboxyvinyl)-3-phosphoshikimate (molecule.C01269). Products: Chorismate (molecule.C00251), phosphate (molecule.ecocyc.Pi).

## Enriched Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Annotation

Shikimate is numbered so that the double-bond is between C-1 and C-2, but some earlier papers numbered the ring in the reverse direction. This reaction is the seventh and final reaction of the shikimate pathway.

## Pathways

- `ecocyc.PWY-6163` chorismate biosynthesis from 3-dehydroquinate (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[complex.ecocyc.AROC-CPLX|complex.ecocyc.AROC-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00251|molecule.C00251]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.Pi|molecule.ecocyc.Pi]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C01269|molecule.C01269]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.ecocyc.6R-6-FLUORO-EPSP|molecule.ecocyc.6R-6-FLUORO-EPSP]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.6S-6-FLUORO-EPSP|molecule.ecocyc.6S-6-FLUORO-EPSP]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:CHORISMATE-SYNTHASE-RXN`

## Notes

3-ENOLPYRUVYL-SHIKIMATE-5P -> Pi + CHORISMATE; direction=PHYSIOL-LEFT-TO-RIGHT
