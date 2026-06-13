---
entity_id: "protein.P37051"
entity_type: "protein"
name: "purU"
source_database: "UniProt"
source_id: "P37051"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purU tgs ychI b1232 JW1220"
---

# purU

`protein.P37051`

## Static

- Type: `protein`
- Source: `UniProt:P37051`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 10-formyltetrahydrofolate (formyl-FH4) to formate and tetrahydrofolate (FH4). Provides the major source of formate for the PurT-dependent synthesis of 5'-phosphoribosyl-N-formylglycinamide (FGAR) during aerobic growth. Has a role in regulating the one-carbon pool. {ECO:0000255|HAMAP-Rule:MF_01927, ECO:0000269|PubMed:7868604}.

## Biological Role

Component of formyltetrahydrofolate deformylase (complex.ecocyc.FORMYLTHFDEFORMYL-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 10-formyltetrahydrofolate (formyl-FH4) to formate and tetrahydrofolate (FH4). Provides the major source of formate for the PurT-dependent synthesis of 5'-phosphoribosyl-N-formylglycinamide (FGAR) during aerobic growth. Has a role in regulating the one-carbon pool. {ECO:0000255|HAMAP-Rule:MF_01927, ECO:0000269|PubMed:7868604}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.FORMYLTHFDEFORMYL-CPLX|complex.ecocyc.FORMYLTHFDEFORMYL-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b1232|gene.b1232]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37051`
- `KEGG:ecj:JW1220;eco:b1232;ecoc:C3026_07250;`
- `GeneID:945827;`
- `GO:GO:0005829; GO:0006164; GO:0006189; GO:0006730; GO:0008864; GO:0034214; GO:0042802`
- `EC:3.5.1.10`

## Notes

Formyltetrahydrofolate deformylase (EC 3.5.1.10) (Formyl-FH(4) hydrolase)
