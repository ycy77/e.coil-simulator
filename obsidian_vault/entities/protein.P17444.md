---
entity_id: "protein.P17444"
entity_type: "protein"
name: "betA"
source_database: "UniProt"
source_id: "P17444"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:3512525}; Peripheral membrane protein {ECO:0000269|PubMed:3512525}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "betA b0311 JW0303"
---

# betA

`protein.P17444`

## Static

- Type: `protein`
- Source: `UniProt:P17444`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:3512525}; Peripheral membrane protein {ECO:0000269|PubMed:3512525}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the oxidation of choline to betaine aldehyde and betaine aldehyde to glycine betaine at the same rate. {ECO:0000255|HAMAP-Rule:MF_00750, ECO:0000269|PubMed:3512525, ECO:0000269|PubMed:3512526}. Choline dehydrogenase (CHD) catalyzes the first step in the biosynthesis of the osmoprotectant glycine betaine from choline. CHD is associated with the membrane, is electron transfer-linked and oxygen dependent . Based on sequence similarity, BetA was predicted to be a hydroxynitrile lyase . A betA mutant does not grow at high osmotic strength in the presence of choline, but is able to grow when the media is supplemented with glycine betaine . Expression of the bet operon is regulated by oxygen, choline, osmotic stress, and temperature . High-purity CHD proteins were obtained with the copolymer styrene maleic acid (SMA) and with the sugar surfactant n-Dodecyl-β-d-Maltopyranoside (DDM). Structural and enzymatic analysis found the CHD formed a trimer and could oxidize choline to betaine aldehyde but not further to betaine. Mutant analysis found H473 to play a critical role in the catalytic activity of CHD . BetA: "betaine"

## Biological Role

Catalyzes CHD-RXN (reaction.ecocyc.CHD-RXN), RXN0-7230 (reaction.ecocyc.RXN0-7230), RXN0-7231 (reaction.ecocyc.RXN0-7231).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the osmoprotectant glycine betaine. Catalyzes the oxidation of choline to betaine aldehyde and betaine aldehyde to glycine betaine at the same rate. {ECO:0000255|HAMAP-Rule:MF_00750, ECO:0000269|PubMed:3512525, ECO:0000269|PubMed:3512526}.

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.CHD-RXN|reaction.ecocyc.CHD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7230|reaction.ecocyc.RXN0-7230]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7231|reaction.ecocyc.RXN0-7231]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0311|gene.b0311]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17444`
- `KEGG:ecj:JW0303;eco:b0311;ecoc:C3026_01520;ecoc:C3026_24695;`
- `GeneID:945716;`
- `GO:GO:0005886; GO:0006970; GO:0008802; GO:0008812; GO:0016020; GO:0019285; GO:0050660`
- `EC:1.1.99.1; 1.2.1.8`

## Notes

Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8)
