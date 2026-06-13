---
entity_id: "reaction.ecocyc.PYRUVDEH-RXN"
entity_type: "reaction"
name: "PYRUVDEH-RXN"
source_database: "EcoCyc"
source_id: "PYRUVDEH-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# PYRUVDEH-RXN

`reaction.ecocyc.PYRUVDEH-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:PYRUVDEH-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This complex reaction bridges between the pathway of glycolysis and the TCA cycle. Details of the component reactions are found by querying the pyruvate dehydrogenase multienzyme complex. EcoCyc reaction equation: PYRUVATE + CO-A + NAD -> ACETYL-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT. This complex reaction bridges between the pathway of glycolysis and the TCA cycle. Details of the component reactions are found by querying the pyruvate dehydrogenase multienzyme complex.

## Biological Role

Catalyzed by pyruvate dehydrogenase (complex.ecocyc.PYRUVATEDEH-CPLX). Substrates: NAD+ (molecule.C00003), CoA (molecule.C00010), Pyruvate (molecule.C00022). Products: NADH (molecule.C00004), CO2 (molecule.C00011), Acetyl-CoA (molecule.C00024).

## Enriched Pathways

- `ecocyc.GLYCOLYSIS-TCA-GLYOX-BYPASS` superpathway of glycolysis, pyruvate dehydrogenase, TCA, and glyoxylate bypass (EcoCyc)

## Annotation

This complex reaction bridges between the pathway of glycolysis and the TCA cycle. Details of the component reactions are found by querying the pyruvate dehydrogenase multienzyme complex.

## Pathways

- `ecocyc.GLYCOLYSIS-TCA-GLYOX-BYPASS` superpathway of glycolysis, pyruvate dehydrogenase, TCA, and glyoxylate bypass (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (18)

- `catalyzes` <-- [[complex.ecocyc.PYRUVATEDEH-CPLX|complex.ecocyc.PYRUVATEDEH-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00022|molecule.C00022]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00048|molecule.C00048]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00109|molecule.C00109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00168|molecule.C00168]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.3-BROMOPYRUVATE|molecule.ecocyc.3-BROMOPYRUVATE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD-4544|molecule.ecocyc.CPD-4544]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1352|molecule.ecocyc.CPD0-1352]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1353|molecule.ecocyc.CPD0-1353]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1354|molecule.ecocyc.CPD0-1354]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:PYRUVDEH-RXN`

## Notes

PYRUVATE + CO-A + NAD -> ACETYL-COA + CARBON-DIOXIDE + NADH; direction=PHYSIOL-LEFT-TO-RIGHT
