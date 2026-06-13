---
entity_id: "protein.P77790"
entity_type: "protein"
name: "ddpX"
source_database: "UniProt"
source_id: "P77790"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:9751644}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ddpX vanX yddT b1488 JW1483"
---

# ddpX

`protein.P77790`

## Static

- Type: `protein`
- Source: `UniProt:P77790`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:9751644}.

## Enriched Summary

FUNCTION: Catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide. May have a role in cell-wall turnover. {ECO:0000255|HAMAP-Rule:MF_01924, ECO:0000269|PubMed:9751644}. VanX is a D-Ala-D-Ala dipeptidase, which catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide required for wild-type peptidoglycan biosynthesis . VanX activity has been characterized . VanX-related proteins are involved in the production of a variant peptidoglycan that results in resistance of pathogenic bacteria to the antibiotic vancomycin; see . VanX may act in murein recycling . VanX allows D-Ala-D-Ala to be utilized as a carbon source, which may have significance with respect to survival at stationary phase . Regulation has been described . The vanX gene has sequences indicative of RpoS regulation . Review: .

## Biological Role

Catalyzes 3.4.13.22-RXN (reaction.ecocyc.3.4.13.22-RXN).

## Enriched Pathways

- `eco01502` Vancomycin resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes hydrolysis of the D-alanyl-D-alanine dipeptide. May have a role in cell-wall turnover. {ECO:0000255|HAMAP-Rule:MF_01924, ECO:0000269|PubMed:9751644}.

## Pathways

- `eco01502` Vancomycin resistance (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.13.22-RXN|reaction.ecocyc.3.4.13.22-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1488|gene.b1488]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77790`
- `KEGG:ecj:JW1483;eco:b1488;ecoc:C3026_08620;`
- `GeneID:93775647;945532;`
- `GO:GO:0005737; GO:0006508; GO:0008270; GO:0009046; GO:0042594; GO:0071555; GO:0160237`
- `EC:3.4.13.22`

## Notes

D-alanyl-D-alanine dipeptidase (D-Ala-D-Ala dipeptidase) (EC 3.4.13.22)
