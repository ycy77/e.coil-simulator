---
entity_id: "gene.b3954"
entity_type: "gene"
name: "yijO"
source_database: "NCBI RefSeq"
source_id: "gene-b3954"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3954"
  - "yijO"
---

# yijO

`gene.b3954`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3954`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yijO (gene.b3954) is a gene entity. It encodes yijO (protein.P32677). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YijO EcoCyc product frame: EG11913-MONOMER. Genomic coordinates: 4147466-4148317. EcoCyc protein note: YijO, which contains a helix-turn-helix motif to bind DNA in its C-terminal domain, appears to belong to the AraC family of transcription factors and it was predicted to regulate genes related to metabolism . Upstream of the yijO gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yijO gene is affected by conditions that generate general transcriptional termination or lead to biofilm formation . A mutation affecting yijO was identified as one of several mutations in an evolved strain adapted to osmotic stress by growth in 0.3 M NaCl . The YijO binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32677|protein.P32677]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yijO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012943,ECOCYC:EG11913,GeneID:948451`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4147466-4148317:-; feature_type=gene
