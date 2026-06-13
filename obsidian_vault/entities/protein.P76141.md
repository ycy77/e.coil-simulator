---
entity_id: "protein.P76141"
entity_type: "protein"
name: "lsrR"
source_database: "UniProt"
source_id: "P76141"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lsrR ydeW b1512 JW1505"
---

# lsrR

`protein.P76141`

## Static

- Type: `protein`
- Source: `UniProt:P76141`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Transcriptional regulator that represses the expression of the lsr operon (lsrACDBFG-tam) in the absence of the quorum-sensing signaling molecule autoinducer 2 (AI-2) (PubMed:15743955, PubMed:16321939, PubMed:19636340). It also represses the expression of the lsrRK operon (PubMed:15743955, PubMed:16321939, PubMed:19636340). Acts by binding directly to the lsrA and lsrR promoter regions (PubMed:19636340). In the presence of phosphorylated autoinducer-2 (phospho-AI-2), LsrR is inactivated, leading to the transcription of the genes (PubMed:15743955, PubMed:16321939, PubMed:19636340). In addition to controlling the transcription of the lsr and lsrRK operons, LsrR may act as a global regulator that regulates the expression of a variety of genes, including genes involved in biofilm formation, host invasion and stress responses (PubMed:17557827). It also regulates the expression of several small RNAs (sRNAs), including DsrA (PubMed:17557827). {ECO:0000269|PubMed:15743955, ECO:0000269|PubMed:16321939, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:19636340}.

## Biological Role

Component of LsrR-autoinducer 2 (complex.ecocyc.CPLX0-7749), LsrR-(2S)-2-hydroxy-3,4-dioxopentyl phosphate (complex.ecocyc.CPLX0-7750), DNA-binding transcriptional repressor LsrR (complex.ecocyc.CPLX0-8043), LsrR-(2R,4S)-2-methyl-2,3,3,4-tetrahydroxytetrahydrofuran (complex.ecocyc.CPLX0-8088).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Transcriptional regulator that represses the expression of the lsr operon (lsrACDBFG-tam) in the absence of the quorum-sensing signaling molecule autoinducer 2 (AI-2) (PubMed:15743955, PubMed:16321939, PubMed:19636340). It also represses the expression of the lsrRK operon (PubMed:15743955, PubMed:16321939, PubMed:19636340). Acts by binding directly to the lsrA and lsrR promoter regions (PubMed:19636340). In the presence of phosphorylated autoinducer-2 (phospho-AI-2), LsrR is inactivated, leading to the transcription of the genes (PubMed:15743955, PubMed:16321939, PubMed:19636340). In addition to controlling the transcription of the lsr and lsrRK operons, LsrR may act as a global regulator that regulates the expression of a variety of genes, including genes involved in biofilm formation, host invasion and stress responses (PubMed:17557827). It also regulates the expression of several small RNAs (sRNAs), including DsrA (PubMed:17557827). {ECO:0000269|PubMed:15743955, ECO:0000269|PubMed:16321939, ECO:0000269|PubMed:17557827, ECO:0000269|PubMed:19636340}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (13)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7749|complex.ecocyc.CPLX0-7749]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7750|complex.ecocyc.CPLX0-7750]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8043|complex.ecocyc.CPLX0-8043]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.CPLX0-8088|complex.ecocyc.CPLX0-8088]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1511|gene.b1511]] `RegulonDB` `C` - regulator=LsrR; target=lsrK; function=-
- `represses` --> [[gene.b1512|gene.b1512]] `RegulonDB` `C` - regulator=LsrR; target=lsrR; function=-
- `represses` --> [[gene.b1513|gene.b1513]] `RegulonDB` `C` - regulator=LsrR; target=lsrA; function=-
- `represses` --> [[gene.b1514|gene.b1514]] `RegulonDB` `C` - regulator=LsrR; target=lsrC; function=-
- `represses` --> [[gene.b1515|gene.b1515]] `RegulonDB` `C` - regulator=LsrR; target=lsrD; function=-
- `represses` --> [[gene.b1516|gene.b1516]] `RegulonDB` `C` - regulator=LsrR; target=lsrB; function=-
- `represses` --> [[gene.b1517|gene.b1517]] `RegulonDB` `C` - regulator=LsrR; target=lsrF; function=-
- `represses` --> [[gene.b1518|gene.b1518]] `RegulonDB` `C` - regulator=LsrR; target=lsrG; function=-
- `represses` --> [[gene.b1519|gene.b1519]] `RegulonDB` `C` - regulator=LsrR; target=tam; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1512|gene.b1512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76141`
- `KEGG:ecj:JW1505;eco:b1512;ecoc:C3026_08745;`
- `GeneID:946070;`
- `GO:GO:0000987; GO:0005829; GO:0006351; GO:0009408; GO:0030246; GO:0042802; GO:2000142`

## Notes

Transcriptional regulator LsrR (lsr regulator)
