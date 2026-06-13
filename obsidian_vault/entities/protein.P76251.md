---
entity_id: "protein.P76251"
entity_type: "protein"
name: "dmlA"
source_database: "UniProt"
source_id: "P76251"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dmlA yeaU b1800 JW1789"
---

# dmlA

`protein.P76251`

## Static

- Type: `protein`
- Source: `UniProt:P76251`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: Catalyzes the NAD(+)-dependent oxidative decarboxylation of D-malate into pyruvate. Is essential for aerobic growth on D-malate as the sole carbon source. But is not required for anaerobic D-malate utilization, although DmlA is expressed and active in those conditions. Appears to be not able to use L-tartrate as a substrate for dehydrogenation instead of D-malate. {ECO:0000269|PubMed:20233924}. DmlA is a D-malate dehydrogenase that is essential for aerobic growth on D-malate as the sole carbon source . DmlA also catalyses the oxidative decarboxylation of 3-isopropylmalate in vitro and in vivo and the non-decarboxylating oxidation of L(+)-tartrate in vitro. DmlA is a generalist enzyme and displays relatively high activity on 3 differing substrates . Expression of dmlA is increased more than 500-fold during growth on D-malate compared to growth on L-lactate , L-malate, glucose or glycerol . Under anaerobic conditions, expression of dmlA is increased even further by the presence of D-malate; however, anaerobic growth on D-malate requires the presence of an additional electron donor such as glycerol . Chromosomal expression of dmlA is able to complement cells lacking leuB-encoded 3-ISOPROPYLMALDEHYDROG-CPLX (IPMDH) activity. Purified DmlA is active on D-malate, 3-isopropylmalate and L(+)-tartrate; D-lactate, isocitrate and D-tartrate are poor substrates...

## Biological Role

Catalyzes (R)-malate:NAD+ oxidoreductase (decarboxylating) (reaction.R00215), R06180 (reaction.R06180), 1.1.1.83-RXN (reaction.ecocyc.1.1.1.83-RXN), RXN-13158 (reaction.ecocyc.RXN-13158), TARTRATE-DEHYDROGENASE-RXN (reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN). Bound by Potassium cation (molecule.C00238), Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(+)-dependent oxidative decarboxylation of D-malate into pyruvate. Is essential for aerobic growth on D-malate as the sole carbon source. But is not required for anaerobic D-malate utilization, although DmlA is expressed and active in those conditions. Appears to be not able to use L-tartrate as a substrate for dehydrogenation instead of D-malate. {ECO:0000269|PubMed:20233924}.

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.R00215|reaction.R00215]] `KEGG` `database` - via EC:1.1.1.83
- `catalyzes` --> [[reaction.R06180|reaction.R06180]] `KEGG` `database` - via EC:1.1.1.93
- `catalyzes` --> [[reaction.ecocyc.1.1.1.83-RXN|reaction.ecocyc.1.1.1.83-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-13158|reaction.ecocyc.RXN-13158]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN|reaction.ecocyc.TARTRATE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b1800|gene.b1800]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76251`
- `KEGG:ecj:JW1789;eco:b1800;ecoc:C3026_10260;`
- `GeneID:75202626;946319;`
- `GO:GO:0000287; GO:0003862; GO:0005737; GO:0006108; GO:0009027; GO:0046553; GO:0051287`
- `EC:1.1.1.83`

## Notes

D-malate dehydrogenase [decarboxylating] (EC 1.1.1.83) (D-malate degradation protein A) (D-malate oxidase)
