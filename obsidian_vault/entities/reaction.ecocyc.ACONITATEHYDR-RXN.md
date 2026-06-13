---
entity_id: "reaction.ecocyc.ACONITATEHYDR-RXN"
entity_type: "reaction"
name: "cis-aconitate hydratase"
source_database: "EcoCyc"
source_id: "ACONITATEHYDR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# cis-aconitate hydratase

`reaction.ecocyc.ACONITATEHYDR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACONITATEHYDR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Cis-aconitate, after dehydration of citrate, is rehydrated to yield isocitrate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant . EcoCyc reaction equation: CIS-ACONITATE + WATER -> THREO-DS-ISO-CITRATE; direction=REVERSIBLE. Cis-aconitate, after dehydration of citrate, is rehydrated to yield isocitrate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Biological Role

Catalyzed by aconitate hydratase A (complex.ecocyc.CPLX0-7760), bifunctional aconitate hydratase B/2-methylisocitrate dehydratase (complex.ecocyc.CPLX0-7761). Substrates: H2O (molecule.C00001), cis-Aconitate (molecule.C00417). Products: D-threo-isocitrate (molecule.ecocyc.THREO-DS-ISO-CITRATE).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

Cis-aconitate, after dehydration of citrate, is rehydrated to yield isocitrate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7760|complex.ecocyc.CPLX0-7760]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7761|complex.ecocyc.CPLX0-7761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.ecocyc.THREO-DS-ISO-CITRATE|molecule.ecocyc.THREO-DS-ISO-CITRATE]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C00417|molecule.C00417]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACONITATEHYDR-RXN`

## Notes

CIS-ACONITATE + WATER -> THREO-DS-ISO-CITRATE; direction=REVERSIBLE
