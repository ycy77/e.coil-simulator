---
entity_id: "gene.b3454"
entity_type: "gene"
name: "livF"
source_database: "NCBI RefSeq"
source_id: "gene-b3454"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3454"
  - "livF"
---

# livF

`gene.b3454`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3454`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livF (gene.b3454) is a gene entity. It encodes livF (protein.P22731). Encoded protein function: FUNCTION: Component of the leucine-specific transport system. EcoCyc product frame: LIVF-MONOMER. Genomic coordinates: 3592724-3593437. EcoCyc protein note: LivF is an ATP-binding cassette (ABC) protein that is a component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . The LivF predicted protein sequence contains Walker A and Walker B motifs involved in the binding and hydrolysis of ATP, and the ABC signature motif (also called the linker peptide or C-loop) (and see also ). liv: leucine isoleucine valine

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22731|protein.P22731]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011282,ECOCYC:EG10536,GeneID:947961`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3592724-3593437:-; feature_type=gene
