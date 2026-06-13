---
entity_id: "gene.b0835"
entity_type: "gene"
name: "rimO"
source_database: "NCBI RefSeq"
source_id: "gene-b0835"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0835"
  - "rimO"
---

# rimO

`gene.b0835`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0835`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rimO (gene.b0835) is a gene entity. It encodes rimO (protein.P0AEI4). Encoded protein function: FUNCTION: Catalyzes the methylthiolation of the residue Asp-89 of ribosomal protein uS12. {ECO:0000269|PubMed:18252828, ECO:0000269|PubMed:21169565}. EcoCyc product frame: G6435-MONOMER. EcoCyc synonyms: yliG. Genomic coordinates: 876710-878035. EcoCyc protein note: RimO was identified as the methyltransferase responsible for methylthiolation of the β carbon of the D88 residue of EG10911-MONOMER . RimO belongs to the methylthiotransferase (MTTase) family of the superfamily of radical-SAM proteins and is the only MTTase known to catalyze methylthiolation of a protein substrate . RimO interacts directly with a ribonucleoprotein complex containing S12; it seems likely that the enzyme is only able to modify S12 efficiently in the context of the small ribosomal subunit . RimO contains two spectroscopically distinguishable [4Fe-4S] clusters . The reaction is thought to take place in two steps , however this has not been shown for RimO in E. coli. It is thought that the G7511 YgfZ protein is involved in the repair/exchange of the spent cluster of both RimO and the homologous enzyme G6364 MiaB. The in vivo activity of RimO is very low in the absence of YgfZ . A rimO mutant contains the unmodified form of S12 and grows more slowly than the wild-type strain...

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEI4|protein.P0AEI4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002843,ECOCYC:G6435,GeneID:945465`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:876710-878035:-; feature_type=gene
