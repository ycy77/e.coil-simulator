---
entity_id: "gene.b2852"
entity_type: "gene"
name: "ygeH"
source_database: "NCBI RefSeq"
source_id: "gene-b2852"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2852"
  - "ygeH"
---

# ygeH

`gene.b2852`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2852`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeH (gene.b2852) is a gene entity. It encodes ygeH (protein.P76639). Encoded protein function: Uncharacterized protein YgeH EcoCyc product frame: G7472-MONOMER. Genomic coordinates: 2992094-2993470. EcoCyc protein note: ygeH is located within a remnant of an ETT2 (type III secretion system) pathogenicity island that is fully present in pathogenic strains such as E. coli O157:H7 and at least partially present in most sequenced E. coli and Shigella strains . ETT2 has been shown to contribute to pathogenesis . The YgeH binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76639|protein.P76639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009368,ECOCYC:G7472,GeneID:946265`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2992094-2993470:+; feature_type=gene
