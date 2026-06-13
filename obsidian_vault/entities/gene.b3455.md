---
entity_id: "gene.b3455"
entity_type: "gene"
name: "livG"
source_database: "NCBI RefSeq"
source_id: "gene-b3455"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3455"
  - "livG"
---

# livG

`gene.b3455`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3455`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livG (gene.b3455) is a gene entity. It encodes livG (protein.P0A9S7). Encoded protein function: FUNCTION: Component of the leucine-specific transport system. EcoCyc product frame: LIVG-MONOMER. EcoCyc synonyms: hrbD, hrbC, hrbB. Genomic coordinates: 3593439-3594206. EcoCyc protein note: LivG is an ATP-binding cassette (ABC) protein that is a component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . The LivG predicted protein sequence contains Walker A and Walker B motifs involved in the binding and hydrolysis of ATP . liv: leucine isoleucine valine

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9S7|protein.P0A9S7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011284,ECOCYC:EG10537,GeneID:947967`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3593439-3594206:-; feature_type=gene
