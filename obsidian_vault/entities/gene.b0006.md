---
entity_id: "gene.b0006"
entity_type: "gene"
name: "yaaA"
source_database: "NCBI RefSeq"
source_id: "gene-b0006"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0006"
  - "yaaA"
---

# yaaA

`gene.b0006`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0006`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaaA (gene.b0006) is a gene entity. It encodes yaaA (protein.P0A8I3). Encoded protein function: FUNCTION: Involved in the cellular response to hydrogen peroxide (H(2)O(2)) stress (PubMed:21378183). During H(2)O(2) stress, prevents oxidative damage to both DNA and proteins by diminishing the amount of unincorporated iron within the cell (PubMed:21378183). Binds double-stranded, bulge-containing, bubble duplex and Holliday junction DNA with approximately equal affinity and ssDNA with lower affinity (PubMed:32796037). DNA binding shows positive cooperativity (PubMed:32796037). Cofitness analysis suggests it might be involved in DNA repair pathways (Probable) (PubMed:32796037). {ECO:0000269|PubMed:21378183, ECO:0000269|PubMed:32796037, ECO:0000305|PubMed:32796037}. EcoCyc product frame: EG10011-MONOMER. Genomic coordinates: 5683-6459. EcoCyc protein note: YaaA is a DNA-binding protein implicated in the cellular response to peroxide stress. yaaA shows OxyR-dependent induction of expression in response to increased hydrogen peroxide levels . Induction of YaaA in response to H2O2 reduces intracellular iron levels, thus attenuating the Fenton reaction and the DNA damage that would result from it . Deletion of yaaA in a strain engineered to accumulate H2O2 results in a growth defect in aerobic LB medium and cells exhibit a severe filamentous phenotype...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8I3|protein.P0A8I3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000018,ECOCYC:EG10011,GeneID:944749`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:5683-6459:-; feature_type=gene
