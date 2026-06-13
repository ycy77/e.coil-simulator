---
entity_id: "protein.P24205"
entity_type: "protein"
name: "lpxM"
source_database: "UniProt"
source_id: "P24205"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01944, ECO:0000269|PubMed:9099672}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01944}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpxM msbB b1855 JW1844"
---

# lpxM

`protein.P24205`

## Static

- Type: `protein`
- Source: `UniProt:P24205`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01944, ECO:0000269|PubMed:9099672}; Single-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01944}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of myristate from myristoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-(lauroyl)-lipid IV(A) to form Kdo(2)-lipid A. Can probably also catalyze the transfer of myristate to Kdo(2)-(palmitoleoyl)-lipid IV(A) to form the cold-adapted Kdo(2)-lipid A. In vitro, can acylate Kdo(2)-lipid IV(A), but acylation of (KDO)2-(lauroyl)-lipid IV(A) is about 100 times faster. In vitro, can use lauroyl-ACP but displays a slight kinetic preference for myristoyl-ACP. {ECO:0000269|PubMed:9099672, ECO:0000305|PubMed:10092655}. Myristoyl-acyl carrier protein (ACP)-dependent acyltransferase (LpxM) catalyzes the transfer of myristate from myristoyl-ACP to the 3'-R-3-hydroxymyristoyl chain of KDO2-(lauroyl)-lipid IVA. This is one of the last two acylation reactions needed to synthesize KDO2-lipid A. LpxM functions optimally after laurate incorporation by LpxL has taken place . LpxM shares sequence homology and functional similarity to LpxL . Mutants of lpxM are characterized by attenuated cytokine induction and with an LPS that lacked the myristoyl fatty acid moiety of the lipid A . Overexpression of lpxM (msbB) suppresses the temperature sensitive growth associated with mutations in the lpxL gene. Mutations in lpxM have caused reduced acylation of LPS, resulting in constitutive expression of the sigma(E) regulon above wild-type levels...

## Biological Role

Catalyzes MYRISTOYLACYLTRAN-RXN (reaction.ecocyc.MYRISTOYLACYLTRAN-RXN), MYRPALMTRAN-RXN (reaction.ecocyc.MYRPALMTRAN-RXN).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of myristate from myristoyl-[acyl-carrier-protein] (ACP) to Kdo(2)-(lauroyl)-lipid IV(A) to form Kdo(2)-lipid A. Can probably also catalyze the transfer of myristate to Kdo(2)-(palmitoleoyl)-lipid IV(A) to form the cold-adapted Kdo(2)-lipid A. In vitro, can acylate Kdo(2)-lipid IV(A), but acylation of (KDO)2-(lauroyl)-lipid IV(A) is about 100 times faster. In vitro, can use lauroyl-ACP but displays a slight kinetic preference for myristoyl-ACP. {ECO:0000269|PubMed:9099672, ECO:0000305|PubMed:10092655}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.MYRISTOYLACYLTRAN-RXN|reaction.ecocyc.MYRISTOYLACYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MYRPALMTRAN-RXN|reaction.ecocyc.MYRPALMTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1855|gene.b1855]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24205`
- `KEGG:ecj:JW1844;eco:b1855;ecoc:C3026_10570;`
- `GeneID:93776129;945143;`
- `GO:GO:0005886; GO:0009103; GO:0009247; GO:0009276; GO:0016020; GO:0016746; GO:0016747; GO:0019107; GO:0036104`
- `EC:2.3.1.243`

## Notes

Lipid A biosynthesis myristoyltransferase (EC 2.3.1.243) (Kdo(2)-lauroyl-lipid IV(A) myristoyltransferase)
