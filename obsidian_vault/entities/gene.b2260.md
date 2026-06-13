---
entity_id: "gene.b2260"
entity_type: "gene"
name: "menE"
source_database: "NCBI RefSeq"
source_id: "gene-b2260"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2260"
  - "menE"
---

# menE

`gene.b2260`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2260`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

menE (gene.b2260) is a gene entity. It encodes menE (protein.P37353). Encoded protein function: FUNCTION: Converts 2-succinylbenzoate (OSB) to 2-succinylbenzoyl-CoA (OSB-CoA). {ECO:0000255|HAMAP-Rule:MF_00731, ECO:0000269|PubMed:8626063}. EcoCyc product frame: O-SUCCINYLBENZOATE-COA-LIG-MONOMER. Genomic coordinates: 2373648-2375003. EcoCyc protein note: O-succinylbenzoate-CoA ligase (MenE) catalyzes the formation of an intermediate in menaquinone biosynthesis, o-succinylbenzoyl-CoA . Inhibition of the enzymatic activity by diethylpyrocarbonate suggested that a histidine residue located near the active site is essential for catalysis; mutagenesis of the His341 residue located in the predicted ATP binding region leads to loss of 65% of enzymatic activity . Mutagenesis of the conserved R195 residue results in reduced catalytic activity due to an increase in KM for O-succinylbenzoate . A crystal structure of the R195K mutant in a complex with the inhibitor OSB-AMS has been solved . Menaquinone biosynthesis provides an attractive antibacterial drug target. Inhibitors of MenE activity have been identified and tested . A menE mutant lacks o-succinylbenzoate-CoA ligase activity . Deletion of menC, menD or menE leads to loss of the ability to reduce selenate . Review:

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37353|protein.P37353]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007471,ECOCYC:EG12437,GeneID:946741`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2373648-2375003:-; feature_type=gene
