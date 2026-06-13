---
entity_id: "gene.b3296"
entity_type: "gene"
name: "rpsD"
source_database: "NCBI RefSeq"
source_id: "gene-b3296"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3296"
  - "rpsD"
---

# rpsD

`gene.b3296`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3296`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsD (gene.b3296) is a gene entity. It encodes rpsD (protein.P0A7V8). Encoded protein function: FUNCTION: One of two assembly initiator proteins for the 30S subunit, it binds directly to 16S rRNA where it nucleates assembly of the body of the 30S subunit. {ECO:0000269|PubMed:2461734}.; FUNCTION: With S5 and S12 plays an important role in translational accuracy; many suppressors of streptomycin-dependent mutants of protein S12 are found in this protein, some but not all of which decrease translational accuracy (ram, ribosomal ambiguity mutations).; FUNCTION: Plays a role in mRNA unwinding by the ribosome, possibly by forming part of a processivity clamp. {ECO:0000269|PubMed:15652481}.; FUNCTION: Protein S4 is also a translational repressor protein, it controls the translation of the alpha-operon (which codes for S13, S11, S4, RNA polymerase alpha subunit, and L17) by binding to its mRNA. {ECO:0000269|PubMed:3309351}.; FUNCTION: Also functions as a rho-dependent antiterminator of rRNA transcription, increasing the synthesis of rRNA under conditions of excess protein, allowing a more rapid return to homeostasis. Binds directly to RNA polymerase. {ECO:0000269|PubMed:11447122}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP)...

## Biological Role

Repressed by rpsD (protein.P0A7V8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7V8|protein.P0A7V8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpsD; function=+
- `represses` <-- [[protein.P0A7V8|protein.P0A7V8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0010805,ECOCYC:EG10903,GeneID:947793`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3441055-3441675:-; feature_type=gene
