---
entity_id: "gene.b1535"
entity_type: "gene"
name: "dgcZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1535"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1535"
  - "dgcZ"
---

# dgcZ

`gene.b1535`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1535`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dgcZ (gene.b1535) is a gene entity. It encodes dgcZ (protein.P31129). Encoded protein function: FUNCTION: Catalyzes the synthesis of cyclic-di-GMP (c-di-GMP) via the condensation of 2 GTP molecules (PubMed:18713317, PubMed:19460094, PubMed:20582742). May act as a zinc sensor that controls, via c-di-GMP, post-translational events (PubMed:23769666). Overexpression leads to a strong repression of swimming; swimming returnes to normal when residues 206-207 are both mutated to Ala. Overexpression also leads to a reduction in flagellar abundance and a 20-fold increase in c-di-GMP levels in vivo. Required for aminoglycoside-mediated induction of biofilm formation, it also plays a lesser role in biofilm production in response to other classes of translation inhibitors. The c-di-GMP produced by this enzyme up-regulates poly-GlcNAc production as well as the biofilm synthesis protein PgaD, although c-di-GMP is probably not the main inducing principle. C-di-GMP is a second messenger which controls cell surface-associated traits in bacteria (PubMed:19460094). {ECO:0000269|PubMed:19460094, ECO:0000269|PubMed:20582742, ECO:0000269|PubMed:23769666, ECO:0000305|PubMed:18713317}. EcoCyc product frame: EG11643-MONOMER. EcoCyc synonyms: ydeG, ydeH. Genomic coordinates: 1622960-1623850.

## Biological Role

Repressed by hns (protein.P0ACF8), csrA (protein.P69913). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31129|protein.P31129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dgcZ; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=dgcZ; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=dgcZ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005123,ECOCYC:EG11643,GeneID:946075`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1622960-1623850:-; feature_type=gene
