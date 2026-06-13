---
entity_id: "reaction.ecocyc.ACONITATEDEHYDR-RXN"
entity_type: "reaction"
name: "ACONITATEDEHYDR-RXN"
source_database: "EcoCyc"
source_id: "ACONITATEDEHYDR-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# ACONITATEDEHYDR-RXN

`reaction.ecocyc.ACONITATEDEHYDR-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:ACONITATEDEHYDR-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

The nonoxidizable tertiary alcohol in citrate is converted to an oxidizable secondary alcohol in isocitrate. Cis-aconitate is the unsaturated intermediate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant . EcoCyc reaction equation: CIT -> CIS-ACONITATE + WATER; direction=REVERSIBLE. The nonoxidizable tertiary alcohol in citrate is converted to an oxidizable secondary alcohol in isocitrate. Cis-aconitate is the unsaturated intermediate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Biological Role

Catalyzed by aconitate hydratase A (complex.ecocyc.CPLX0-7760), bifunctional aconitate hydratase B/2-methylisocitrate dehydratase (complex.ecocyc.CPLX0-7761). Substrates: Citrate (molecule.C00158). Products: H2O (molecule.C00001), cis-Aconitate (molecule.C00417).

## Enriched Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Annotation

The nonoxidizable tertiary alcohol in citrate is converted to an oxidizable secondary alcohol in isocitrate. Cis-aconitate is the unsaturated intermediate. The prpD gene encodes 2-methylcitrate dehydratase activity and also encodes the minor aconitase activity, aconitase C , which constitutes 5% or less of cellular activity and is observed in an acnA acnB double mutant .

## Pathways

- `ecocyc.FERMENTATION-PWY` mixed acid fermentation (EcoCyc)
- `ecocyc.GLYOXYLATE-BYPASS` glyoxylate cycle (EcoCyc)
- `ecocyc.TCA` TCA cycle I (prokaryotic) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[complex.ecocyc.CPLX0-7760|complex.ecocyc.CPLX0-7760]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.CPLX0-7761|complex.ecocyc.CPLX0-7761]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00417|molecule.C00417]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:ACONITATEDEHYDR-RXN`

## Notes

CIT -> CIS-ACONITATE + WATER; direction=REVERSIBLE
