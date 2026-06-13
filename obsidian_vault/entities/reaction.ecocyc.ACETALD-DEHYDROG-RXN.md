---
entity_id: "reaction.ecocyc.ACETALD-DEHYDROG-RXN"
entity_type: "reaction"
name: "ACETALD-DEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "ACETALD-DEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACETALD-DEHYDROG-RXN

`reaction.ecocyc.ACETALD-DEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACETALD-DEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

A step in the conversion of acetyl coenzyme-A to ethanol in the fermentation pathway. The reaction is also the terminal step in the 3-(3-hydroxyphenyl)propionate catabolic pathway. EcoCyc reaction equation: NAD + CO-A + ACETALD -> PROTON + NADH + ACETYL-COA; direction=REVERSIBLE. A step in the conversion of acetyl coenzyme-A to ethanol in the fermentation pathway. The reaction is also the terminal step in the 3-(3-hydroxyphenyl)propionate catabolic pathway.

## Biological Role

Catalyzed by fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase (complex.ecocyc.ADHE-CPLX), eutE (protein.P77445), mhpF (protein.P77580). Substrates: NAD+ (molecule.C00003), CoA (molecule.C00010), Acetaldehyde (molecule.C00084). Products: NADH (molecule.C00004), Acetyl-CoA (molecule.C00024), H+ (molecule.C00080).

## Enriched Pathways

- `ecocyc.ETOH-ACETYLCOA-ANA-PWY` ethanol degradation I (EcoCyc)
- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)
- `ecocyc.PWY-5436` L-threonine degradation IV (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Annotation

A step in the conversion of acetyl coenzyme-A to ethanol in the fermentation pathway. The reaction is also the terminal step in the 3-(3-hydroxyphenyl)propionate catabolic pathway.

## Pathways

- `ecocyc.ETOH-ACETYLCOA-ANA-PWY` ethanol degradation I (EcoCyc)
- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5162` 2-hydroxypenta-2,4-dienoate degradation (EcoCyc)
- `ecocyc.PWY-5436` L-threonine degradation IV (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY-7180` 2-deoxy-α-D-ribose 1-phosphate degradation (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1364|molecule.ecocyc.CPD0-1364]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Thiols|molecule.ecocyc.Thiols]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ADHE-CPLX|complex.ecocyc.ADHE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77445|protein.P77445]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[protein.P77580|protein.P77580]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00024|molecule.C00024]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00010|molecule.C00010]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00261|molecule.C00261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01502|molecule.C01502]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ACETALD-DEHYDROG-RXN`

## Notes

NAD + CO-A + ACETALD -> PROTON + NADH + ACETYL-COA; direction=REVERSIBLE
