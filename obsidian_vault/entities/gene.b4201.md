---
entity_id: "gene.b4201"
entity_type: "gene"
name: "priB"
source_database: "NCBI RefSeq"
source_id: "gene-b4201"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4201"
  - "priB"
---

# priB

`gene.b4201`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4201`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

priB (gene.b4201) is a gene entity. It encodes priB (protein.P07013). Encoded protein function: FUNCTION: Involved in the restart of stalled replication forks, which reloads the replicative helicase (DnaB) on sites other than the origin of replication; the PriA-PriB pathway is the major replication restart pathway (PubMed:11532137, PubMed:37169801, PubMed:22636770). There are several restart pathways, the PriA-PriB pathway is subdivided into 2 distinct pathways (PubMed:34423481). priB and priC have redundant roles in the cell (PubMed:10540288). During primosome assembly it facilitates complex formation between PriA and DnaT on DNA; stabilizes PriA on DNA, presumably by preventing or inhibiting PriA DNA translocation activity (PubMed:8663104, PubMed:8663105, PubMed:8663106). Forms a branched DNA-PriA-PriB complex when the lagging strand is single-stranded (ss)DNA (PubMed:16188886). Binds ssDNA in the presence and absence of ssDNA DNA-binding protein (SSB), does not bind branched structures (PubMed:8366072, PubMed:16188886). DNA binding, forming spiral filaments on ssDNA, is cooperative (PubMed:16899446). Stimulates the helicase activity of PriA (PubMed:16188886, PubMed:37169801, PubMed:34423481). The homodimer binds 12 nucleotides of ssDNA (PubMed:20156448). Binds homo-pyrimidine tracts better than homo-purine tracts (PubMed:15383524, PubMed:20156448)...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07013|protein.P07013]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=priB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013742,ECOCYC:EG10764,GeneID:948722`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4425520-4425834:+; feature_type=gene
