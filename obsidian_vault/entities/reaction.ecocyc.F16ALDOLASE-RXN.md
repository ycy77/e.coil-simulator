---
entity_id: "reaction.ecocyc.F16ALDOLASE-RXN"
entity_type: "reaction"
name: "F16ALDOLASE-RXN"
source_database: "EcoCyc"
source_id: "F16ALDOLASE-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "FRUCTOSE-1,6-BISPHOSPHATE TRIOSEPHOSPHATE-LYASE"
  - "ALDOLASE"
---

# F16ALDOLASE-RXN

`reaction.ecocyc.F16ALDOLASE-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:F16ALDOLASE-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Dihydroxyacetone phosphate is also called glycerone phosphate. Of the total aldolase activity in cell-free extracts of E.coli grown on pyruvate and lactate, approx. 60 % was accounted for by aldolase 1. On the other hand, E.coli grown on glucose showed no aldolase 1 activity but had an increased aldolase 2 activity. During growth with CO2 as a carbon source, only class I aldolase is produced but when acetate replaces CO2 the class II aldolase is made. Similarly, in E.coli the putative class I aldolase is only synthesized during growth on C3 compounds and not on glucose, implying that a class I aldolase is preferred for gluconeogenesis EcoCyc reaction equation: FRUCTOSE-16-DIPHOSPHATE -> DIHYDROXY-ACETONE-PHOSPHATE + GAP; direction=REVERSIBLE. Dihydroxyacetone phosphate is also called glycerone phosphate. Of the total aldolase activity in cell-free extracts of E.coli grown on pyruvate and lactate, approx. 60 % was accounted for by aldolase 1. On the other hand, E.coli grown on glucose showed no aldolase 1 activity but had an increased aldolase 2 activity. During growth with CO2 as a carbon source, only class I aldolase is produced but when acetate replaces CO2 the class II aldolase is made. Similarly, in E.coli the putative class I aldolase is only synthesized during growth on C3 compounds and not on glucose, implying that a class I aldolase is preferred for gluconeogenesis

## Biological Role

Catalyzed by fructose-bisphosphate aldolase class I (complex.ecocyc.FRUCBISALD-CLASSI), fructose-bisphosphate aldolase class II (complex.ecocyc.FRUCBISALD-CLASSII). Substrates: D-Fructose 1,6-bisphosphate (molecule.C00354). Products: Glycerone phosphate (molecule.C00111), D-Glyceraldehyde 3-phosphate (molecule.C00118).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

Dihydroxyacetone phosphate is also called glycerone phosphate. Of the total aldolase activity in cell-free extracts of E.coli grown on pyruvate and lactate, approx. 60 % was accounted for by aldolase 1. On the other hand, E.coli grown on glucose showed no aldolase 1 activity but had an increased aldolase 2 activity. During growth with CO2 as a carbon source, only class I aldolase is produced but when acetate replaces CO2 the class II aldolase is made. Similarly, in E.coli the putative class I aldolase is only synthesized during growth on C3 compounds and not on glucose, implying that a class I aldolase is preferred for gluconeogenesis

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (11)

- `activates` <-- [[molecule.C00158|molecule.C00158]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` <-- [[molecule.ecocyc.AMMONIUM|molecule.ecocyc.AMMONIUM]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` <-- [[complex.ecocyc.FRUCBISALD-CLASSI|complex.ecocyc.FRUCBISALD-CLASSI]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` <-- [[complex.ecocyc.FRUCBISALD-CLASSII|complex.ecocyc.FRUCBISALD-CLASSII]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00354|molecule.C00354]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.BOROHYDRIDE|molecule.ecocyc.BOROHYDRIDE]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` <-- [[molecule.ecocyc.EDTA|molecule.ecocyc.EDTA]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:F16ALDOLASE-RXN`

## Notes

FRUCTOSE-16-DIPHOSPHATE -> DIHYDROXY-ACETONE-PHOSPHATE + GAP; direction=REVERSIBLE
