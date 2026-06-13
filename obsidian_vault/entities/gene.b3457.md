---
entity_id: "gene.b3457"
entity_type: "gene"
name: "livH"
source_database: "NCBI RefSeq"
source_id: "gene-b3457"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3457"
  - "livH"
---

# livH

`gene.b3457`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3457`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

livH (gene.b3457) is a gene entity. It encodes livH (protein.P0AEX7). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for branched-chain amino acids. Probably responsible for the translocation of the substrates across the membrane. EcoCyc product frame: LIVH-MONOMER. EcoCyc synonyms: hrbD, hrbC, hrbB. Genomic coordinates: 3595477-3596403. EcoCyc protein note: LivH is an integral membrane component of the LIV-I (LivJHMGF) and LS (LivKHMGF) branched chain amino acid and phenylalanine ABC transport system in E. coli K-12. The LivFGHM proteins interact with either of two periplasmic binding proteins, LivJ or LivK, and catalyse the uptake of the branched chain amino acids, L-leucine, L-isoleucine and L-valine and the nonpolar, aromatic amino acid, phenylalanine . livH encodes a very hydrophobic protein with 7 or 9 predicted transmembrane regions . livH mutant strains (livR livH::Mu) show significantly reduced uptake of L-valine, L-isoleucine and L-leucine . liv: leucine isoleucine valine

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEX7|protein.P0AEX7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=livH; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=livH; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011290,ECOCYC:EG10538,GeneID:947965`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3595477-3596403:-; feature_type=gene
