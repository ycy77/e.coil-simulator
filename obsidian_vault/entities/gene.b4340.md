---
entity_id: "gene.b4340"
entity_type: "gene"
name: "yjiR"
source_database: "NCBI RefSeq"
source_id: "gene-b4340"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4340"
  - "yjiR"
---

# yjiR

`gene.b4340`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4340`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjiR (gene.b4340) is a gene entity. It encodes yjiR (protein.P39389). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YjiR EcoCyc product frame: G7936-MONOMER. Genomic coordinates: 4570162-4571574. EcoCyc protein note: YjiR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the DeoR family of transcription factors, and it was predicted to regulate genes related to antibiotic sensibility . YjiR may have a positive role in csgD expression . Upstream of the yjiR gene, a sequence was found that could work as a transcriptional promoter, and the transcription of the yjiR gene is affected by DNA damage . The YjiR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9), arcA (protein.P0A9Q1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39389|protein.P39389]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yjiR; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=yjiR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014232,ECOCYC:G7936,GeneID:949089`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4570162-4571574:-; feature_type=gene
