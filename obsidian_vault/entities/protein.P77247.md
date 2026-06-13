---
entity_id: "protein.P77247"
entity_type: "protein"
name: "hxpB"
source_database: "UniProt"
source_id: "P77247"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hxpB yniC b1727 JW1716"
---

# hxpB

`protein.P77247`

## Static

- Type: `protein`
- Source: `UniProt:P77247`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sugar-phosphate phosphohydrolase that catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Also catalyzes the dephosphorylation of 2-deoxyglucose 6-phosphate (2dGlu6P); this is a biologically important activity in vivo since it contributes to the elimination of this toxic compound and plays an important role in the resistance of E.coli to 2-deoxyglucose (PubMed:16990279). To a lesser extent, is also able to dephosphorylate mannose 6-phosphate (Man6P), erythrose-4-phosphate, 2-deoxyribose-5-phosphate (2dRib5P), ribose-5-phosphate (Rib5P) and glucose-6-phosphate (Glu6P) in vitro (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}. The hexitol phosphatase activity of HxpB was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HxpB is a sugar phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. Its preferred substrate is 2-deoxyglucose-6-phosphate . The phosphatase activity of HxpB was first discovered in a high-throughput screen of purified proteins . Phosphatase activity of HxpB is dependent on the presence of a divalent cation such as Mg2+, which appears to affect substrate binding...

## Biological Role

Catalyzes sugar-phosphate phosphohydrolase (reaction.R00804), sorbitol-6-phosphate phosphohydrolase (reaction.R02866), 3.1.3.68-RXN (reaction.ecocyc.3.1.3.68-RXN), MANNITOL-1-PHOSPHATASE-RXN (reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN), SORBITOL-6-PHOSPHATASE-RXN (reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Sugar-phosphate phosphohydrolase that catalyzes the dephosphorylation of D-mannitol 1-phosphate and D-sorbitol 6-phosphate (PubMed:27941785). Also catalyzes the dephosphorylation of 2-deoxyglucose 6-phosphate (2dGlu6P); this is a biologically important activity in vivo since it contributes to the elimination of this toxic compound and plays an important role in the resistance of E.coli to 2-deoxyglucose (PubMed:16990279). To a lesser extent, is also able to dephosphorylate mannose 6-phosphate (Man6P), erythrose-4-phosphate, 2-deoxyribose-5-phosphate (2dRib5P), ribose-5-phosphate (Rib5P) and glucose-6-phosphate (Glu6P) in vitro (PubMed:16990279). {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00804|reaction.R00804]] `KEGG` `database` - via EC:3.1.3.23
- `catalyzes` --> [[reaction.R02866|reaction.R02866]] `KEGG` `database` - via EC:3.1.3.50
- `catalyzes` --> [[reaction.ecocyc.3.1.3.68-RXN|reaction.ecocyc.3.1.3.68-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN|reaction.ecocyc.MANNITOL-1-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN|reaction.ecocyc.SORBITOL-6-PHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1727|gene.b1727]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77247`
- `KEGG:ecj:JW1716;eco:b1727;ecoc:C3026_09875;`
- `GeneID:945632;`
- `GO:GO:0000287; GO:0003850; GO:0004346; GO:0005829; GO:0016791; GO:0046872; GO:0050084; GO:0050286; GO:0050308`
- `EC:3.1.3.22; 3.1.3.23; 3.1.3.50; 3.1.3.68`

## Notes

Hexitol phosphatase B (2-deoxyglucose-6-phosphate phosphatase) (EC 3.1.3.68) (Mannitol-1-phosphatase) (EC 3.1.3.22) (Sorbitol-6-phosphatase) (EC 3.1.3.50) (Sugar-phosphatase) (EC 3.1.3.23)
