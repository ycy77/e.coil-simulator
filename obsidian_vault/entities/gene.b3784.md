---
entity_id: "gene.b3784"
entity_type: "gene"
name: "wecA"
source_database: "NCBI RefSeq"
source_id: "gene-b3784"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3784"
  - "wecA"
---

# wecA

`gene.b3784`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3784`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wecA (gene.b3784) is a gene entity. It encodes wecA (protein.P0AC78). Encoded protein function: FUNCTION: Catalyzes the transfer of the GlcNAc-1-phosphate moiety from UDP-GlcNAc onto the carrier lipid undecaprenyl phosphate (C55-P), yielding GlcNAc-pyrophosphoryl-undecaprenyl (GlcNAc-PP-C55). It is the first lipid-linked intermediate involved in enterobacterial common antigen (ECA) synthesis, and an acceptor for the addition of subsequent sugars to complete the biosynthesis of O-antigen lipopolysaccharide (LPS) in many E.coli O types. The apparent affinity of WecA for the polyisoprenyl phosphate substrates increases with the polyisoprenyl chain length. WecA is unable to utilize dolichyl phosphate (Dol-P). {ECO:0000269|PubMed:11700352, ECO:0000269|PubMed:17237164, ECO:0000269|PubMed:1730666, ECO:0000269|PubMed:9134438}. EcoCyc product frame: GLCNACPTRANS-MONOMER. EcoCyc synonyms: rfe. Genomic coordinates: 3967916-3969019.

## Biological Role

Repressed by DNA-binding transcriptional dual regulator/c-di-GMP phosphodiesterase PdeL (complex.ecocyc.CPLX0-8109), pdeL (protein.P21514).

## Enriched Pathways

- `eco00542` O-Antigen repeat unit biosynthesis (KEGG)
- `eco00543` Exopolysaccharide biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC78|protein.P0AC78]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[complex.ecocyc.CPLX0-8109|complex.ecocyc.CPLX0-8109]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P21514|protein.P21514]] `RegulonDB` `S` - regulator=PdeL; target=wecA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012366,ECOCYC:EG10840,GeneID:948789`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3967916-3969019:+; feature_type=gene
