---
entity_id: "gene.b3238"
entity_type: "gene"
name: "yhcN"
source_database: "NCBI RefSeq"
source_id: "gene-b3238"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3238"
  - "yhcN"
---

# yhcN

`gene.b3238`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3238`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhcN (gene.b3238) is a gene entity. It encodes yhcN (protein.P64614). Encoded protein function: Uncharacterized protein YhcN EcoCyc product frame: G7683-MONOMER. Genomic coordinates: 3385538-3385801. EcoCyc protein note: YhcN is involved in the response to hydrogen peroxide stress . A yhcN mutant is significantly more sensitive to hydrogen peroxide and cadmium than wild type and shows increased biofilm formation compared to wild type . Expression of yhcN is upregulated in response to cytoplasmic acid stress . In an E. coli strain engineered to degrade the pollutant cis-dichloroethylene (cis-DCE), deletion of yhcN results in reduced cis-DCE degradation . A strain with a transposon insertion in yhcN shows increased fitness during selection for thiamine diphosphate (TPP) production in a competitive growth assay; a yhcN null mutant produces a higher extracellular TPP titer . yhcN was in the top 20 genes with increased translation in response to extreme acid stress (pH 4.4 and 5.8 compared to pH 7.6) and increased transcription in response to H2O oxidative stress as measured by mRNA levels by RT-qPCR, confirming previous studies .

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64614|protein.P64614]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010623,ECOCYC:G7683,GeneID:947835`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3385538-3385801:+; feature_type=gene
