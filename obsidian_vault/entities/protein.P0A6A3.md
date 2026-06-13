---
entity_id: "protein.P0A6A3"
entity_type: "protein"
name: "ackA"
source_database: "UniProt"
source_id: "P0A6A3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ackA ack b2296 JW2293"
---

# ackA

`protein.P0A6A3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6A3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Catalyzes the formation of acetyl phosphate from acetate and ATP. Can also catalyze the reverse reaction. During anaerobic growth of the organism, this enzyme is also involved in the synthesis of most of the ATP formed catabolically. The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:16080684}. AckA has propionate kinase activity as well as acetate kinase activity. The ackA-encoded propionate kinase 2 has an important role in propionyl-CoA metabolism . Acetate kinase can also catalyze acetylation of CheY, increasing signal strength for flagellar rotation . A second gene encoding acetate kinase, G14, was thought to exist . Transcription of ackA is induced by the CreBC two-component system by minimal media growth conditions . Several metabolic genes, including ackA, were found upregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . E. coli double mutants deficient in AckA and Pta activity, or AckA and TdcD activity, were unable to metabolize threonine to propionate. This suggested the participation of this enzyme in pathway PWY-5437. An ackA mutant showed a significant reduction in the conversion of threonine to propionate, as well as a 75% reduction in acetate production . In E...

## Biological Role

Catalyzes ATP:acetate phosphotransferase (reaction.R00315), ACETATEKIN-RXN (reaction.ecocyc.ACETATEKIN-RXN), PROPKIN-RXN (reaction.ecocyc.PROPKIN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of acetyl phosphate from acetate and ATP. Can also catalyze the reverse reaction. During anaerobic growth of the organism, this enzyme is also involved in the synthesis of most of the ATP formed catabolically. The main pathway for acetate production during exponential phase (PubMed:16080684). {ECO:0000269|PubMed:16080684}.

## Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00315|reaction.R00315]] `KEGG` `database` - via EC:2.7.2.1
- `catalyzes` --> [[reaction.ecocyc.ACETATEKIN-RXN|reaction.ecocyc.ACETATEKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.PROPKIN-RXN|reaction.ecocyc.PROPKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2296|gene.b2296]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6A3`
- `KEGG:ecj:JW2293;eco:b2296;ecoc:C3026_12810;`
- `GeneID:93774878;946775;`
- `GO:GO:0000287; GO:0005524; GO:0005829; GO:0006083; GO:0006085; GO:0008270; GO:0008776; GO:0016020; GO:0019413; GO:0019542; GO:0044011`
- `EC:2.7.2.1`

## Notes

Acetate kinase (EC 2.7.2.1) (Acetokinase)
