---
entity_id: "protein.P31119"
entity_type: "protein"
name: "aas"
source_database: "UniProt"
source_id: "P31119"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aas b2836 JW2804"
---

# aas

`protein.P31119`

## Static

- Type: `protein`
- Source: `UniProt:P31119`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Plays a role in lysophospholipid acylation. Transfers fatty acids to the 1-position via an enzyme-bound acyl-ACP intermediate in the presence of ATP and magnesium. Its physiological function is to regenerate phosphatidylethanolamine from 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) formed by transacylation reactions or degradation by phospholipase A1. {ECO:0000255|HAMAP-Rule:MF_01162, ECO:0000269|PubMed:1649829}. 2-acylglycerophosphoethanolamine (2-acyl-GPE) acyltransferase and acyl-acyl carrier protein (acyl-ACP) synthetase are dual catalytic activities encoded by the aas gene. Both enzymatic activities participate in membrane phospholipid turnover and the uptake and incorporation of exogenous 2-acyllysophospholipids. The function of 2-acyl-GPE acyltransferase is to regenerate phosphatidylethanolamine (PtdEtn) from 2-acyl-GPE formed by transacylation reactions or phospholipase A1 action. In the process enzyme-bound ACP is also regenerated . Acyl-ACP synthetase functions to ligate free fatty acids, with lengths of C-8 to C-18, to ACP . The protein contains bound ACP . Based on sequence similarity, Aas has been predicted to be a hydroxycinnamate-CoA ligase . Review:

## Biological Role

Catalyzes ACYLGPEACYLTRANS-RXN (reaction.ecocyc.ACYLGPEACYLTRANS-RXN), RXN-5741 (reaction.ecocyc.RXN-5741), Long-chain-fatty-acid--acyl-carrier protein ligase (reaction.ecocyc.RXN0-5513). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

FUNCTION: Plays a role in lysophospholipid acylation. Transfers fatty acids to the 1-position via an enzyme-bound acyl-ACP intermediate in the presence of ATP and magnesium. Its physiological function is to regenerate phosphatidylethanolamine from 2-acyl-glycero-3-phosphoethanolamine (2-acyl-GPE) formed by transacylation reactions or degradation by phospholipase A1. {ECO:0000255|HAMAP-Rule:MF_01162, ECO:0000269|PubMed:1649829}.

## Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ACYLGPEACYLTRANS-RXN|reaction.ecocyc.ACYLGPEACYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-5741|reaction.ecocyc.RXN-5741]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5513|reaction.ecocyc.RXN0-5513]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2836|gene.b2836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31119`
- `KEGG:ecj:JW2804;eco:b2836;ecoc:C3026_15575;`
- `GeneID:947315;`
- `GO:GO:0004467; GO:0005524; GO:0005886; GO:0006631; GO:0008654; GO:0008779; GO:0008922; GO:0016020; GO:0044325`
- `EC:2.3.1.40; 6.2.1.20`

## Notes

Bifunctional protein Aas [Includes: 2-acylglycerophosphoethanolamine acyltransferase (EC 2.3.1.40) (2-acyl-GPE acyltransferase) (Acyl-[acyl-carrier-protein]--phospholipid O-acyltransferase); Acyl-[acyl-carrier-protein] synthetase (EC 6.2.1.20) (Acyl-ACP synthetase) (Long-chain-fatty-acid--[acyl-carrier-protein] ligase)]
