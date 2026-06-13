---
entity_id: "gene.b3167"
entity_type: "gene"
name: "rbfA"
source_database: "NCBI RefSeq"
source_id: "gene-b3167"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3167"
  - "rbfA"
---

# rbfA

`gene.b3167`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3167`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rbfA (gene.b3167) is a gene entity. It encodes rbfA (protein.P0A7G2). Encoded protein function: FUNCTION: One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late maturation steps of the functional core of the 30S subunit. Essential for efficient processing of pre-16S rRNA (PubMed:12628255, PubMed:12963368, PubMed:9422595). Probably part of the 30S subunit prior to or during the final step in the processing of 16S free 30S ribosomal subunits. Probably interacts with the 5'-terminal helix region of 16S rRNA (PubMed:7535280). Has affinity for free ribosomal 30S subunits but not for 70S ribosomes (PubMed:12963368, PubMed:7535280). Overexpression suppresses a cold-sensitive C23U 16S rRNA mutation (PubMed:7535280). Overexpression decreases the lag time following cold-shock by about half, leading to faster adaptation and increased protein synthesis (PubMed:8898389). Overexpression also partially suppresses a rimM deletion mutant and partially rescues its 16S rRNA processing deficiency (PubMed:9422595). Its function overlaps that of Era in ribosome biogenesis (PubMed:16825789). A number of RbfA mutants suppress RsgA/YjeQ deletions, in all cases less RbfA is bound to the 30S ribosome (PubMed:21102555). Released from 30S ribosomes by RsgA; stimulates the ribosome-associated GTPase activity of RsgA (PubMed:21102555)...

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7G2|protein.P0A7G2]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rbfA; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=rbfA; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=rbfA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010406,ECOCYC:EG11178,GeneID:947685`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3312777-3313178:-; feature_type=gene
