---
entity_id: "gene.b1790"
entity_type: "gene"
name: "nimR"
source_database: "NCBI RefSeq"
source_id: "gene-b1790"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1790"
  - "nimR"
---

# nimR

`gene.b1790`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1790`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nimR (gene.b1790) is a gene entity. It encodes nimR (protein.P76241). Encoded protein function: FUNCTION: Negatively regulates expression of the nimT operon and its own expression. Acts by binding to the nimR-nimT intergenic region. {ECO:0000269|PubMed:25790494}. EcoCyc product frame: G6976-MONOMER. EcoCyc synonyms: yeaM. Genomic coordinates: 1874755-1875576. EcoCyc protein note: NimR, formerly called YeaM, belongs to the AraC/XylS superfamily . It confers resistance to 2-nitroimidazole, an antibacterial and antifungal agent . NimR plays a regulatory role in divergent transcription of the nimT and nimR genes . Genome-wide NimR binding sites were determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . A negative correlation between cellular growth and the copy number of the proteins NimR has been reported . NimR: regulator of nimT . The NimR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Repressed by nimR (protein.P76241).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76241|protein.P76241]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P76241|protein.P76241]] `RegulonDB` `C` - regulator=NimR; target=nimR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005956,ECOCYC:G6976,GeneID:946590`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1874755-1875576:-; feature_type=gene
