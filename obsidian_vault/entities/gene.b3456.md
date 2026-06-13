---
entity_id: "gene.b3456"
entity_type: "gene"
name: "livM"
source_database: "NCBI RefSeq"
source_id: "gene-b3456"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3456"
  - "livM"
---

# livM

`gene.b3456`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3456`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livM (gene.b3456) is a gene entity. It encodes livM (protein.P22729). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for branched-chain amino acids. Probably responsible for the translocation of the substrates across the membrane. EcoCyc product frame: LIVM-MONOMER. Genomic coordinates: 3594203-3595480. EcoCyc protein note: LivM is an integral membrane component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . livM encodes a very hydrophobic protein with 9 predicted transmembrane regions . liv: leucine isoleucine valine

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22729|protein.P22729]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livM; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=livM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011287,ECOCYC:EG10541,GeneID:947966`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3594203-3595480:-; feature_type=gene
