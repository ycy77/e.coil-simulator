---
entity_id: "protein.P42593"
entity_type: "protein"
name: "fadH"
source_database: "UniProt"
source_id: "P42593"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadH ygjL b3081 JW3052"
---

# fadH

`protein.P42593`

## Static

- Type: `protein`
- Source: `UniProt:P42593`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Functions as an auxiliary enzyme in the beta-oxidation of unsaturated fatty acids with double bonds at even carbon positions. Catalyzes the NADPH-dependent reduction of the C4-C5 double bond of the acyl chain of 2,4-dienoyl-CoA to yield 2-trans-enoyl-CoA (PubMed:6363415, PubMed:9346310). Acts on both isomers, 2-trans,4-cis- and 2-trans,4-trans-decadienoyl-CoA, with almost equal efficiency (PubMed:6363415). Is not active with NADH instead of NADPH (PubMed:6363415). Does not show cis->trans isomerase activity (PubMed:10933894). {ECO:0000269|PubMed:10933894, ECO:0000269|PubMed:6363415, ECO:0000269|PubMed:9346310}. 2,4-Dienoyl-CoA reductase functions in the reductive removal of double bonds extending from even-numbered carbon atoms in unsaturated and polyunsaturated fatty acids. The product of the reaction catalyzed by E. coli FadH is 2-trans-enoyl-CoA, in contrast with the bovine enzyme, which produces 3-trans-enoyl-CoA. FadH is able to catalyze the reduction of 2-trans,4-cis and 2-trans,4-trans isomers with almost equal efficiency . This is not due to a cis-trans isomerase activity of the enzyme . Kinetic data first suggested that the reaction proceeds via a ping-pong mechanism . A crystal structure of the enzyme has been solved at 2.2 Å resolution...

## Biological Role

Catalyzes (2E)-2-enoyl-CoA:NADP+ 4-oxidoreductase (reaction.R12620), DIENOYLCOAREDUCT-RXN (reaction.ecocyc.DIENOYLCOAREDUCT-RXN). Bound by FAD (molecule.C00016), FMN (molecule.C00061), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

FUNCTION: Functions as an auxiliary enzyme in the beta-oxidation of unsaturated fatty acids with double bonds at even carbon positions. Catalyzes the NADPH-dependent reduction of the C4-C5 double bond of the acyl chain of 2,4-dienoyl-CoA to yield 2-trans-enoyl-CoA (PubMed:6363415, PubMed:9346310). Acts on both isomers, 2-trans,4-cis- and 2-trans,4-trans-decadienoyl-CoA, with almost equal efficiency (PubMed:6363415). Is not active with NADH instead of NADPH (PubMed:6363415). Does not show cis->trans isomerase activity (PubMed:10933894). {ECO:0000269|PubMed:10933894, ECO:0000269|PubMed:6363415, ECO:0000269|PubMed:9346310}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R12620|reaction.R12620]] `KEGG` `database` - via EC:1.3.1.34
- `catalyzes` --> [[reaction.ecocyc.DIENOYLCOAREDUCT-RXN|reaction.ecocyc.DIENOYLCOAREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3081|gene.b3081]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42593`
- `KEGG:ecj:JW3052;eco:b3081;ecoc:C3026_16825;`
- `GeneID:947594;`
- `GO:GO:0008670; GO:0010181; GO:0033543; GO:0046872; GO:0051539; GO:0071949`
- `EC:1.3.1.34`

## Notes

2,4-dienoyl-CoA reductase [(2E)-enoyl-CoA-producing] (DCR) (EC 1.3.1.34) (2,4-dienoyl-coenzyme A reductase [NADPH])
