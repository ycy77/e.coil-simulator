---
entity_id: "gene.b3638"
entity_type: "gene"
name: "yicR"
source_database: "NCBI RefSeq"
source_id: "gene-b3638"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3638"
  - "yicR"
---

# yicR

`gene.b3638`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3638`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yicR (gene.b3638) is a gene entity. It encodes yicR (protein.P25531). Encoded protein function: UPF0758 protein YicR EcoCyc product frame: EG11312-MONOMER. EcoCyc synonyms: radC. Genomic coordinates: 3811891-3812559. EcoCyc protein note: A ΔyicR mutant has aggravating genetic interactions with genes involved in DNA recombination . The radC102 mutation was originally thought to be allelic with yicR; however, it is shown to be allelic with recG . yicR supplied on a low-copy-number vector did not alter UV sensitivities of recG mutants or their background strain . In a previous experiment, the cloned yicR gene partially complemented the radC102 allele for UV resistance, but made the wild-type strain more sensitive . The YicR open reading frame encodes interacting sequence tags, suggesting that the protein may assemble into multisubunit complexes . yicR is the first gene in an operon with rpmB, rpmG, and fpg . The yicR gene is thought to be a member of the CreBC regulon; expression is induced during growth in miminal medium with glucose . 4,5-dihydroxy-2-cyclopenten-1-one altered the expression of several CreBC-regulated genes, but not radC .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25531|protein.P25531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011889,ECOCYC:EG11312,GeneID:948968`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3811891-3812559:-; feature_type=gene
