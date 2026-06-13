---
entity_id: "gene.b3383"
entity_type: "gene"
name: "yhfZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3383"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3383"
  - "yhfZ"
---

# yhfZ

`gene.b3383`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3383`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhfZ (gene.b3383) is a gene entity. It encodes yhfZ (protein.P45552). Encoded protein function: Uncharacterized protein YhfZ EcoCyc product frame: G7735-MONOMER. Genomic coordinates: 3511439-3512344. EcoCyc protein note: The YhfZ binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45552|protein.P45552]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yhfZ; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011052,ECOCYC:G7735,GeneID:947897`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3511439-3512344:-; feature_type=gene
