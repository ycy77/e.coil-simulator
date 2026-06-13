---
entity_id: "gene.b2157"
entity_type: "gene"
name: "yeiE"
source_database: "NCBI RefSeq"
source_id: "gene-b2157"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2157"
  - "yeiE"
---

# yeiE

`gene.b2157`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2157`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yeiE (gene.b2157) is a gene entity. It encodes yeiE (protein.P0ACR4). Encoded protein function: FUNCTION: Transcription factor, which is probably involved in maintaining iron homeostasis under iron-limited conditions (PubMed:30137486). It shows over 100 binding sites across the E.coli K12 MG1655 genome (PubMed:30137486). Target genes are involved in diverse biological processes, including transport and metabolism, cell wall/membrane biogenesis, signal transduction and transcriptional regulation, suggesting that YeiE may play multiple biological roles (PubMed:30137486). It may function as a positive regulator of lysP expression, leading to the increase of lysine uptake (PubMed:12400704). {ECO:0000269|PubMed:12400704, ECO:0000269|PubMed:30137486}. EcoCyc product frame: EG12105-MONOMER. Genomic coordinates: 2248737-2249618. EcoCyc protein note: YeiE is a LysR-related protein that appears to activate transcription of lysP . YeiE was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . YeiE is involved in iron uptake under iron-limited conditions . Expression of yeiE increases yield from a strain engineered to produce L-pipecolic acid from L-lysine . Compared to known global TFs, YeiE exhibits some interesting regulatory features...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACR4|protein.P0ACR4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yeiE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007138,ECOCYC:EG12105,GeneID:946657`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2248737-2249618:-; feature_type=gene
