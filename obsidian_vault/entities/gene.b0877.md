---
entity_id: "gene.b0877"
entity_type: "gene"
name: "ybjX"
source_database: "NCBI RefSeq"
source_id: "gene-b0877"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0877"
  - "ybjX"
---

# ybjX

`gene.b0877`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0877`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybjX (gene.b0877) is a gene entity. It encodes ybjX (protein.P75829). Encoded protein function: Uncharacterized protein YbjX EcoCyc product frame: G6460-MONOMER. Genomic coordinates: 918128-919120. EcoCyc protein note: ybjX is homologous to somA from Salmonella enterica serovar Typhimurium (59% nucleotide homology; 56% protein identity); somA was first identified in a screen for suppressors of a Salmonella mutant (msbB1::Ωtet), that fails to myristoylate lipid A within lipopolysaccharide . ybjX contributes to virulence in Avian pathogenic E. coli . A ybjX nonsynonymous mutation (YbjXM73K) contributes to colistin resistance in a laboratory evolved strain .

## Biological Role

Repressed by nac (protein.Q47005). Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75829|protein.P75829]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ybjX; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002982,ECOCYC:G6460,GeneID:946025`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:918128-919120:-; feature_type=gene
