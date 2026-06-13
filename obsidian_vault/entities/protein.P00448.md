---
entity_id: "protein.P00448"
entity_type: "protein"
name: "sodA"
source_database: "UniProt"
source_id: "P00448"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sodA b3908 JW3879"
---

# sodA

`protein.P00448`

## Static

- Type: `protein`
- Source: `UniProt:P00448`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems. SodA, or MnSOD, is one of three superoxide dismutases in E. coli . The three enzymes differ in their metal cofactor requirement; MnSOD contains manganese. Superoxide dismutase is implicated in the response to a large number of environmental changes that lead to the generation of superoxide radicals. MnSOD and the iron-containing enzyme SUPEROX-DISMUTFE-MONOMER FeSOD (SodB) are not functionally equivalent; MnSOD is more effective than FeSOD in preventing damage to DNA, while FeSOD seems more effective in protecting a cytoplasmic superoxide-sensitive enzyme . However, both enzymes were shown to protect dihydroxy acid dehydratase from inactivation by oxidative stress . MnSOD binds DNA non-specifically with a Ka of 3 x 105 M-1 . The superoxide dismutases contribute to reducing iron toxicity . The enzyme is highly specific for the manganese cofactor; an iron-substituted MnSOD is catalytically inactive , although it was recently suggested that iron-substituted MnSOD has peroxidase/catalase activity . The binding constant for Mn(II) is 3.2 x 108 M-1 , and the process of manganese acquisition has been studied . Metal uptake appears to be cooperative and requires dimer dissociation...

## Biological Role

Catalyzes superoxide:superoxide oxidoreductase (reaction.R00275). Component of superoxide dismutase (Mn) (complex.ecocyc.SUPEROX-DISMUTMN-CPLX).

## Enriched Pathways

- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems.

## Pathways

- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00275|reaction.R00275]] `KEGG` `database` - via EC:1.15.1.1
- `is_component_of` --> [[complex.ecocyc.SUPEROX-DISMUTMN-CPLX|complex.ecocyc.SUPEROX-DISMUTMN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3908|gene.b3908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00448`
- `KEGG:ecj:JW3879;eco:b3908;ecoc:C3026_21130;`
- `GeneID:948403;`
- `GO:GO:0003677; GO:0004784; GO:0005737; GO:0005829; GO:0006801; GO:0006979; GO:0009408; GO:0010447; GO:0016209; GO:0019430; GO:0030145; GO:0042803; GO:0046872; GO:0071291`
- `EC:1.15.1.1`

## Notes

Superoxide dismutase [Mn] (EC 1.15.1.1) (MnSOD)
