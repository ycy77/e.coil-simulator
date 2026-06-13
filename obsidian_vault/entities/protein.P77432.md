---
entity_id: "protein.P77432"
entity_type: "protein"
name: "lsrK"
source_database: "UniProt"
source_id: "P77432"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02053}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrK ydeV b1511 JW1504"
---

# lsrK

`protein.P77432`

## Static

- Type: `protein`
- Source: `UniProt:P77432`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_02053}.

## Enriched Summary

FUNCTION: Catalyzes the phosphorylation of autoinducer-2 (AI-2) to phospho-AI-2, which subsequently inactivates the transcriptional regulator LsrR and leads to the transcription of the lsr operon. Phosphorylates the ring-open form of (S)-4,5-dihydroxypentane-2,3-dione (DPD), which is the precursor to all AI-2 signaling molecules, at the C5 position. Required for the regulation of the lsr operon and many other genes. {ECO:0000269|PubMed:15601708, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:20025244}. LsrK is a kinase that is able to phosphorylate the quorum-sensing autoinducer molecule AI-2 . Based on its similarity to LsrK from Salmonella typhimurium, LsrK was already predicted to have AI-2 kinase activity . Phosphorylation of AI-2 by LsrK is essential for internalization and sequestration of AI-2 . Kinetic analysis of LsrK from Salmonella was most consistent with a rapid equilibrium ordered reaction mechanism with ATP binding first . LsrK has been overexpressed and crystallized . LsrK copurifies with PTSH-MONOMER, and co-crystal structures have been solved; LsrK domain I binds HPr, and domain II binds ATP . HPr inhibits LsrK activity in vitro; phosphorylated HPr has a reduced ability to inhibit LsrK activity. HPr-mediated regulation of LsrK may link sugar metabolism to quorum sensing activity . An lsrK mutant accumulates AI-2 in the culture fluid...

## Biological Role

Catalyzes RXN0-5461 (reaction.ecocyc.RXN0-5461).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorylation of autoinducer-2 (AI-2) to phospho-AI-2, which subsequently inactivates the transcriptional regulator LsrR and leads to the transcription of the lsr operon. Phosphorylates the ring-open form of (S)-4,5-dihydroxypentane-2,3-dione (DPD), which is the precursor to all AI-2 signaling molecules, at the C5 position. Required for the regulation of the lsr operon and many other genes. {ECO:0000269|PubMed:15601708, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:20025244}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5461|reaction.ecocyc.RXN0-5461]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1511|gene.b1511]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77432`
- `KEGG:ecj:JW1504;eco:b1511;ecoc:C3026_08740;`
- `GeneID:946069;`
- `GO:GO:0005737; GO:0005975; GO:0009372; GO:0016301; GO:0044010; GO:0071518`
- `EC:2.7.1.189`

## Notes

Autoinducer-2 kinase (AI-2 kinase) (EC 2.7.1.189)
