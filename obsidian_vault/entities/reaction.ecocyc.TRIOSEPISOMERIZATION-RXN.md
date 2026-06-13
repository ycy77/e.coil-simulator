---
entity_id: "reaction.ecocyc.TRIOSEPISOMERIZATION-RXN"
entity_type: "reaction"
name: "TRIOSEPISOMERIZATION-RXN"
source_database: "EcoCyc"
source_id: "TRIOSEPISOMERIZATION-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
  - "PHOSPHOTRIOSE ISOMERASE"
  - "TRIOSEPHOSPHATE MUTASE"
---

# TRIOSEPISOMERIZATION-RXN

`reaction.ecocyc.TRIOSEPISOMERIZATION-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:TRIOSEPISOMERIZATION-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

GAP -> DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE EcoCyc reaction equation: GAP -> DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE.

## Biological Role

Catalyzed by triose-phosphate isomerase (complex.ecocyc.TPI). Substrates: D-Glyceraldehyde 3-phosphate (molecule.C00118). Products: Glycerone phosphate (molecule.C00111).

## Enriched Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Annotation

GAP -> DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE

## Pathways

- `ecocyc.GLUCONEO-PWY` gluconeogenesis I (EcoCyc)
- `ecocyc.GLYCOLYSIS` glycolysis I (from glucose 6-phosphate) (EcoCyc)
- `ecocyc.PWY-5484` glycolysis II (from fructose 6-phosphate) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[complex.ecocyc.TPI|complex.ecocyc.TPI]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00111|molecule.C00111]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00118|molecule.C00118]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` <-- [[molecule.C00988|molecule.C00988]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## External IDs

- `EcoCyc:TRIOSEPISOMERIZATION-RXN`

## Notes

GAP -> DIHYDROXY-ACETONE-PHOSPHATE; direction=REVERSIBLE
