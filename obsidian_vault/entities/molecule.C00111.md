---
entity_id: "molecule.C00111"
entity_type: "small_molecule"
name: "Glycerone phosphate"
source_database: "KEGG"
source_id: "C00111"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Glycerone phosphate"
  - "Dihydroxyacetone phosphate"
  - "3-Hydroxy-2-oxopropyl phosphate"
---

# Glycerone phosphate

`molecule.C00111`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00111`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Glycerone phosphate; Dihydroxyacetone phosphate; 3-Hydroxy-2-oxopropyl phosphate

## Biological Role

Consumed as substrate in 7 reaction(s). Produced in 20 reaction(s).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Annotation

KEGG compound: Glycerone phosphate; Dihydroxyacetone phosphate; 3-Hydroxy-2-oxopropyl phosphate

## Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00562` Inositol phosphate metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)

## Outgoing Edges (29)

- `is_product_of` --> [[reaction.R00842|reaction.R00842]] `KEGG` `database` - C00093 + C00003 <=> C00111 + C00004 + C00080
- `is_product_of` --> [[reaction.R00844|reaction.R00844]] `KEGG` `database` - C00093 + C00006 <=> C00111 + C00005 + C00080
- `is_product_of` --> [[reaction.R00848|reaction.R00848]] `KEGG` `database` - C00093 + C00016 <=> C00111 + C01352
- `is_product_of` --> [[reaction.R00849|reaction.R00849]] `KEGG` `database` - C00093 + C15602 <=> C00111 + C15603
- `is_product_of` --> [[reaction.R01012|reaction.R01012]] `KEGG` `database` - C00074 + C00184 <=> C00022 + C00111
- `is_product_of` --> [[reaction.R01015|reaction.R01015]] `KEGG` `database` - C00118 <=> C00111
- `is_product_of` --> [[reaction.ecocyc.2.7.1.121-RXN|reaction.ecocyc.2.7.1.121-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.DARABALDOL-RXN|reaction.ecocyc.DARABALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.FUCPALDOL-RXN|reaction.ecocyc.FUCPALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN|reaction.ecocyc.GLYC3PDEHYDROGBIOSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RHAMNULPALDOL-RXN|reaction.ecocyc.RHAMNULPALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15298|reaction.ecocyc.RXN-15298]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-15740|reaction.ecocyc.RXN-15740]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-21532|reaction.ecocyc.RXN-21532]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7169|reaction.ecocyc.RXN0-7169]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.SEDOBISALDOL-RXN|reaction.ecocyc.SEDOBISALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TAGAALDOL-RXN|reaction.ecocyc.TAGAALDOL-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRIOSEPISOMERIZATION-RXN|reaction.ecocyc.TRIOSEPISOMERIZATION-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R01010|reaction.R01010]] `KEGG` `database` - C00111 + C00001 <=> C00184 + C00009
- `is_substrate_of` --> [[reaction.R01016|reaction.R01016]] `KEGG` `database` - C00111 <=> C00546 + C00009
- `is_substrate_of` --> [[reaction.ecocyc.METHGLYSYN-RXN|reaction.ecocyc.METHGLYSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.QUINOLINATE-SYNTHA-RXN|reaction.ecocyc.QUINOLINATE-SYNTHA-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-15943|reaction.ecocyc.RXN-15943]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5257|reaction.ecocyc.RXN0-5257]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7249|reaction.ecocyc.RXN0-7249]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN-1381|reaction.ecocyc.RXN-1381]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-5260|reaction.ecocyc.RXN0-5260]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00111`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
