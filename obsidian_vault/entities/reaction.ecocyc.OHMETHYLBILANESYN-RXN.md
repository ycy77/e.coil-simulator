---
entity_id: "reaction.ecocyc.OHMETHYLBILANESYN-RXN"
entity_type: "reaction"
name: "OHMETHYLBILANESYN-RXN"
source_database: "EcoCyc"
source_id: "OHMETHYLBILANESYN-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PORPHOBILINOGEN DEAMINASE"
  - "PRE-UROPORPHYRINOGEN SYNTHASE"
---

# OHMETHYLBILANESYN-RXN

`reaction.ecocyc.OHMETHYLBILANESYN-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:OHMETHYLBILANESYN-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This reaction forms the first tetrapyrrole compound. In the presence of a second enzyme, EC 4.2.1.75 (uroporphyrinogen-III synthase), often called co-synthase, the product is cyclized to form uroporphyrinogen-III. EcoCyc reaction equation: WATER + PORPHOBILINOGEN -> AMMONIUM + HYDROXYMETHYLBILANE; direction=PHYSIOL-LEFT-TO-RIGHT. This reaction forms the first tetrapyrrole compound. In the presence of a second enzyme, EC 4.2.1.75 (uroporphyrinogen-III synthase), often called co-synthase, the product is cyclized to form uroporphyrinogen-III.

## Biological Role

Catalyzed by hemC (protein.P06983). Substrates: H2O (molecule.C00001), Porphobilinogen (molecule.C00931). Products: Hydroxymethylbilane (molecule.C01024), ammonium (molecule.ecocyc.AMMONIUM).

## Enriched Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Annotation

This reaction forms the first tetrapyrrole compound. In the presence of a second enzyme, EC 4.2.1.75 (uroporphyrinogen-III synthase), often called co-synthase, the product is cyclized to form uroporphyrinogen-III.

## Pathways

- `ecocyc.PWY-5188` uroporphyrinogen-III I (from glutamate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P06983|protein.P06983]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C01024|molecule.C01024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00931|molecule.C00931]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BH4NA|molecule.ecocyc.BH4NA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:OHMETHYLBILANESYN-RXN`

## Notes

WATER + PORPHOBILINOGEN -> AMMONIUM + HYDROXYMETHYLBILANE; direction=PHYSIOL-LEFT-TO-RIGHT
