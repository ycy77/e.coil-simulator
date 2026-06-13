---
entity_id: "gene.b2948"
entity_type: "gene"
name: "yqgE"
source_database: "NCBI RefSeq"
source_id: "gene-b2948"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2948"
  - "yqgE"
---

# yqgE

`gene.b2948`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2948`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yqgE (gene.b2948) is a gene entity. It encodes yqgE (protein.P0A8W5). Encoded protein function: UPF0301 protein YqgE EcoCyc product frame: G7524-MONOMER. Genomic coordinates: 3092937-3093500. EcoCyc protein note: yqgE belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . The close position of yqgE and yqgF (1 nt overlap found in E. coli) is highly conserved across most γ- and β-proteobacteria pointing to a possible functional partnership of these genes . The molecular function of YqgE is predicted to be a protein disulfide isomerase based on in silico analysis using COFACTOR as stated in . Deletion of yqgE in METG-MONOMER MetG* hyper-persister cells significantly reduced the survival to antibiotics starting in early stationary phase with the effect being influenced by the length of stationary phase of the parent culture; this was not seen in ΔyqgE in wild-type cells. However, overexpression of yqgE in wild-type cells increased lag phase and lag-dependent persistence, thus inducing cell dormancy. YqgE also plays a role in reducing protein expression in MetG* and wild-type lag phase cells; it also may play a role in modulating proteolysis by CPLX0-2881, another major driver of lag-dependent persistence .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8W5|protein.P0A8W5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009669,ECOCYC:G7524,GeneID:947442`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3092937-3093500:+; feature_type=gene
