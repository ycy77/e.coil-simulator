---
entity_id: "protein.P60955"
entity_type: "protein"
name: "lgt"
source_database: "UniProt"
source_id: "P60955"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22287519, ECO:0000269|PubMed:26729647}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:22287519, ECO:0000269|PubMed:26729647}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lgt umpA b2828 JW2796"
---

# lgt

`protein.P60955`

## Static

- Type: `protein`
- Source: `UniProt:P60955`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22287519, ECO:0000269|PubMed:26729647}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:22287519, ECO:0000269|PubMed:26729647}.

## Enriched Summary

FUNCTION: Catalyzes the transfer of the diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of the N-terminal cysteine of a prolipoprotein, the first step in the formation of mature lipoproteins. {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:26729647, ECO:0000269|PubMed:7896715, ECO:0000269|PubMed:8051048}. Lgt catalyses the transfer of an sn-1,2-diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of the prospective N-terminal cysteine of a proliporotein . It is the first of 3 sequential reactions (catalysed by Lgt, EG10548-MONOMER and EG10168-MONOMER respectively) that result in the formation of mature triacylated lipoproteins, including EG10544-MONOMER. Lgt is an essential inner membrane protein . lgt (formerly umpA) mutants are defective in diacylglycerol modification of prolipoprotein in vitro and in vivo . Lgt contains 7 transmembrane segments; the N-terminus faces the periplasm and the C-terminus faces the cytoplasm . Lgt is a peripheral membrane protein associating loosely with the cytoplasmic face of the inner membrane . A conserved histidine residue, His-103, is essential for enzyme activity ; His-103 is not essential for enzyme activity lgt and thyA form an operon . Lgt is a target for the development of novel antibiotics...

## Biological Role

Catalyzes RXN0-20 (reaction.ecocyc.RXN0-20).

## Annotation

FUNCTION: Catalyzes the transfer of the diacylglyceryl group from phosphatidylglycerol to the sulfhydryl group of the N-terminal cysteine of a prolipoprotein, the first step in the formation of mature lipoproteins. {ECO:0000255|HAMAP-Rule:MF_01147, ECO:0000269|PubMed:26729647, ECO:0000269|PubMed:7896715, ECO:0000269|PubMed:8051048}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-20|reaction.ecocyc.RXN0-20]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2828|gene.b2828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60955`
- `KEGG:ecj:JW2796;eco:b2828;ecoc:C3026_15525;`
- `GeneID:93779170;947303;`
- `GO:GO:0005886; GO:0008961; GO:0009898; GO:0042158`
- `EC:2.5.1.145`

## Notes

Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) (Prolipoprotein diacylglyceryl transferase)
