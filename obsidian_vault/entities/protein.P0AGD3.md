---
entity_id: "protein.P0AGD3"
entity_type: "protein"
name: "sodB"
source_database: "UniProt"
source_id: "P0AGD3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sodB b1656 JW1648"
---

# sodB

`protein.P0AGD3`

## Static

- Type: `protein`
- Source: `UniProt:P0AGD3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems. SodB, or FeSOD, is one of three superoxide dismutases in E. coli . The three enzymes differ in their metal cofactor requirement; FeSOD contains iron. Superoxide dismutase is implicated in the response to a large number of environmental changes that lead to the generation of superoxide radicals. FeSOD and the manganese-containing enzyme MnSOD (SodA) are not functionally equivalent; MnSOD is more effective than FeSOD in preventing damage to DNA, while FeSOD seems more effective in protecting a cytoplasmic superoxide-sensitive enzyme . However, both enzymes were shown to protect dihydroxy acid dehydratase from inactivation by oxidative stress . The reaction mechanism involves cycling of the metal ion between the +3 and +2 oxidation states; the midpoint potential of the metal ion determines what redox reactions are possible, and is thus precisely tuned . Crystal structures of FeSOD have been solved . Tyr34 is required for maximal activity ; its contribution to substrate binding has been evaluated . The enzyme is highly specific for the iron cofactor; a manganese-substituted FeSOD is catalytically inactive . Mutations in Q69 and A141 alter metal selectivity and catalytic activity...

## Biological Role

Catalyzes superoxide:superoxide oxidoreductase (reaction.R00275). Component of superoxide dismutase (Fe) (complex.ecocyc.SUPEROX-DISMUTFE-CPLX).

## Enriched Pathways

- `eco04146` Peroxisome (KEGG)

## Annotation

FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems.

## Pathways

- `eco04146` Peroxisome (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00275|reaction.R00275]] `KEGG` `database` - via EC:1.15.1.1
- `is_component_of` --> [[complex.ecocyc.SUPEROX-DISMUTFE-CPLX|complex.ecocyc.SUPEROX-DISMUTFE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1656|gene.b1656]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGD3`
- `KEGG:ecj:JW1648;eco:b1656;ecoc:C3026_09500;`
- `GeneID:93775810;944953;`
- `GO:GO:0000303; GO:0004784; GO:0005506; GO:0005737; GO:0005829; GO:0006801; GO:0016020; GO:0016491; GO:0019430`
- `EC:1.15.1.1`

## Notes

Superoxide dismutase [Fe] (EC 1.15.1.1)
