---
entity_id: "gene.b3346"
entity_type: "gene"
name: "yheO"
source_database: "NCBI RefSeq"
source_id: "gene-b3346"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3346"
  - "yheO"
---

# yheO

`gene.b3346`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3346`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yheO (gene.b3346) is a gene entity. It encodes yheO (protein.P64624). Encoded protein function: Uncharacterized protein YheO EcoCyc product frame: G7715-MONOMER. Genomic coordinates: 3475718-3476440. EcoCyc protein note: YheO was predicted to regulate genes related to tRNA modification . YheO was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . YheO is necessary to overcome a temperature-sensitive phenotype caused by a mutant with a deletion in the gene lapD, which encodes a protein that regulates lipopolysaccharide assembly . Compared to known global TFs, YheO exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA. Third, it binds to more genes with putative functions. Finally, its expression level is lower relative to that of the majority of global TFs . The transcription of the yheO gene is affected by conditions that lead to biofilm formation or RNA degradation...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64624|protein.P64624]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010936,ECOCYC:G7715,GeneID:947851`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3475718-3476440:-; feature_type=gene
