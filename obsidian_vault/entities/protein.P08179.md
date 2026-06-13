---
entity_id: "protein.P08179"
entity_type: "protein"
name: "purN"
source_database: "UniProt"
source_id: "P08179"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purN b2500 JW2485"
---

# purN

`protein.P08179`

## Static

- Type: `protein`
- Source: `UniProt:P08179`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of a formyl group from 10-formyltetrahydrofolate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) and tetrahydrofolate. {ECO:0000255|HAMAP-Rule:MF_01930, ECO:0000269|PubMed:2185839, ECO:0000269|PubMed:350869}. E. coli contains two different phosphoribosylglycinamide (GAR) transformylases, both of which can catalyze the third step in de novo purine biosynthesis. The transformylase encoded by purN utilizes 10-formyl-tetrahydrofolate as the formyl donor. The second transformylase encoded by purT utilizes formate, which is provided by PurU-catalyzed hydrolysis of 10-formyl-tetrahydrofolate . The existence of these two transformylase enzymes was determined by mutant studies. A strain containing a knockout insertion in purN did not result in purine auxotrophy . Only mutants defective in both purN and purT required exogenously added purine for growth . There is no significant homology between the two transformylases . In early work using E. coli B, 10-formyltetrahydrofolate was identified as the formyl donor for this enzyme . Later work using E...

## Biological Role

Catalyzes GART-RXN (reaction.ecocyc.GART-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of a formyl group from 10-formyltetrahydrofolate to 5-phospho-ribosyl-glycinamide (GAR), producing 5-phospho-ribosyl-N-formylglycinamide (FGAR) and tetrahydrofolate. {ECO:0000255|HAMAP-Rule:MF_01930, ECO:0000269|PubMed:2185839, ECO:0000269|PubMed:350869}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GART-RXN|reaction.ecocyc.GART-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2500|gene.b2500]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08179`
- `KEGG:ecj:JW2485;eco:b2500;ecoc:C3026_13865;`
- `GeneID:946973;`
- `GO:GO:0004644; GO:0005737; GO:0005829; GO:0006189; GO:0006974`
- `EC:2.1.2.2`

## Notes

Phosphoribosylglycinamide formyltransferase (EC 2.1.2.2) (5'-phosphoribosylglycinamide transformylase) (GAR transformylase) (GART)
