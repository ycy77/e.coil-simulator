---
entity_id: "reaction.ecocyc.ALCOHOL-DEHYDROG-RXN"
entity_type: "reaction"
name: "ALCOHOL-DEHYDROG-RXN"
source_database: "EcoCyc"
source_id: "ALCOHOL-DEHYDROG-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ALCOHOL-DEHYDROG-RXN

`reaction.ecocyc.ALCOHOL-DEHYDROG-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ALCOHOL-DEHYDROG-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The final reaction in the fermentation pathway leading to ethanol. EcoCyc reaction equation: ETOH + NAD -> ACETALD + NADH + PROTON; direction=REVERSIBLE. The final reaction in the fermentation pathway leading to ethanol.

## Biological Role

Catalyzed by fused acetaldehyde-CoA dehydrogenase and Fe-dependent alcohol dehydrogenase (complex.ecocyc.ADHE-CPLX), ethanol dehydrogenase / alcohol dehydrogenase (complex.ecocyc.CPLX0-8015). Substrates: NAD+ (molecule.C00003), Ethanol (molecule.C00469). Products: NADH (molecule.C00004), H+ (molecule.C00080), Acetaldehyde (molecule.C00084).

## Enriched Pathways

- `ecocyc.ETOH-ACETYLCOA-ANA-PWY` ethanol degradation I (EcoCyc)
- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Annotation

The final reaction in the fermentation pathway leading to ethanol.

## Pathways

- `ecocyc.ETOH-ACETYLCOA-ANA-PWY` ethanol degradation I (EcoCyc)
- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.PWY-5480` pyruvate fermentation to ethanol I (EcoCyc)
- `ecocyc.PWY0-1477` ethanolamine utilization (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (17)

- `activates` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.CPD0-1364|molecule.ecocyc.CPD0-1364]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.Thiols|molecule.ecocyc.Thiols]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.ADHE-CPLX|complex.ecocyc.ADHE-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-8015|complex.ecocyc.CPLX0-8015]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00084|molecule.C00084]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00469|molecule.C00469]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00020|molecule.C00020]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00261|molecule.C00261]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C00301|molecule.C00301]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.C01502|molecule.C01502]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.CPD0-1652|molecule.ecocyc.CPD0-1652]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.PYRAZOLE|molecule.ecocyc.PYRAZOLE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:ALCOHOL-DEHYDROG-RXN`

## Notes

ETOH + NAD -> ACETALD + NADH + PROTON; direction=REVERSIBLE
