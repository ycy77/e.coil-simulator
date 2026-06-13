---
entity_id: "gene.b0208"
entity_type: "gene"
name: "yafC"
source_database: "NCBI RefSeq"
source_id: "gene-b0208"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0208"
  - "yafC"
---

# yafC

`gene.b0208`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0208`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafC (gene.b0208) is a gene entity. It encodes yafC (protein.P30864). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YafC EcoCyc product frame: EG11649-MONOMER. Genomic coordinates: 229967-230881. EcoCyc protein note: YafC, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the LysR family of transcription factors (TFs), and it was predicted to regulate genes related to metabolism and chlorine resistance . YafC was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . Compared to known global TFs, YafC exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA. Third, it binds to more genes with putative functions. Finally, its expression level is lower relative to that of the majority of global TFs . The most common binding mode for YafC is downstream of the RNAP binding region . Upstream of the yafC gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yafC gene is affected by temperature...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30864|protein.P30864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yafC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000694,ECOCYC:EG11649,GeneID:947507`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:229967-230881:-; feature_type=gene
