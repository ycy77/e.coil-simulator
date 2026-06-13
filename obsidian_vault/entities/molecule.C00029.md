---
entity_id: "molecule.C00029"
entity_type: "small_molecule"
name: "UDP-glucose"
source_database: "KEGG"
source_id: "C00029"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-glucose"
  - "UDPglucose"
  - "UDP-D-glucose"
  - "Uridine diphosphate glucose"
  - "UDP-alpha-D-glucose"
---

# UDP-glucose

`molecule.C00029`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00029`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-glucose; UDPglucose; UDP-D-glucose; Uridine diphosphate glucose; UDP-alpha-D-glucose EcoCyc common name: UDP-α-D-glucose. UDP-glucose is an activated form of glucose that participates in a variety of enzymatic reactions, including: 1. Biosynthesis of glucose-containing compounds, such as polysaccharaides (glycogen, starch, laminarin and cellulose), disaccharides (sucrose, trehalose), β-glucosides, and glucosyl-ceramides. 2. Channeling galactose into the glycolytic pathway It has also been suggested that UDP-D-glucose can act as an extracellular signaling molecule .

## Biological Role

Consumed as substrate in 16 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)

## Annotation

KEGG compound: UDP-glucose; UDPglucose; UDP-D-glucose; Uridine diphosphate glucose; UDP-alpha-D-glucose

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00566` Sulfoquinovose metabolism (KEGG)

## Outgoing Edges (21)

- `activates` --> [[reaction.ecocyc.ADPSUGPPHOSPHAT-RXN|reaction.ecocyc.ADPSUGPPHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00289|reaction.R00289]] `KEGG` `database` - C00075 + C00103 <=> C00013 + C00029
- `is_product_of` --> [[reaction.ecocyc.GLUC1PURIDYLTRANS-RXN|reaction.ecocyc.GLUC1PURIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00286|reaction.R00286]] `KEGG` `database` - C00029 + C00001 + 2 C00003 <=> C00167 + 2 C00004 + 2 C00080
- `is_substrate_of` --> [[reaction.R00287|reaction.R00287]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_substrate_of` --> [[reaction.R00291|reaction.R00291]] `KEGG` `database` - C00029 <=> C00052
- `is_substrate_of` --> [[reaction.R00836|reaction.R00836]] `KEGG` `database` - C00029 + C00092 <=> C00015 + C00689
- `is_substrate_of` --> [[reaction.R02889|reaction.R02889]] `KEGG` `database` - C00029 + C00760 <=> C00015 + C00760
- `is_substrate_of` --> [[reaction.ecocyc.2.4.1.78-RXN|reaction.ecocyc.2.4.1.78-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN|reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.GALACTURIDYLYLTRANS-RXN|reaction.ecocyc.GALACTURIDYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-11791|reaction.ecocyc.RXN-11791]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22463|reaction.ecocyc.RXN-22463]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5120|reaction.ecocyc.RXN0-5120]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5125|reaction.ecocyc.RXN0-5125]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5126|reaction.ecocyc.RXN0-5126]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TREHALOSE6PSYN-RXN|reaction.ecocyc.TREHALOSE6PSYN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPGLUCEPIM-RXN|reaction.ecocyc.UDPGLUCEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UGD-RXN|reaction.ecocyc.UGD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DTDPGLUCOSEPP-RXN|reaction.ecocyc.DTDPGLUCOSEPP-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00029`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
