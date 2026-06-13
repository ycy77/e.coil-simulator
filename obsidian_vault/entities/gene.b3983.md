---
entity_id: "gene.b3983"
entity_type: "gene"
name: "rplK"
source_database: "NCBI RefSeq"
source_id: "gene-b3983"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3983"
  - "rplK"
---

# rplK

`gene.b3983`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3983`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplK (gene.b3983) is a gene entity. It encodes rplK (protein.P0A7J7). Encoded protein function: FUNCTION: Forms part of the ribosomal stalk which helps the ribosome interact with GTP-bound translation factors. EcoCyc product frame: EG10872-MONOMER. EcoCyc synonyms: relC. Genomic coordinates: 4178447-4178875. EcoCyc protein note: The L11 protein is a component of the 50S subunit of the ribosome. L11 is posttranslationally modified by methylation . The N-terminal alanine residue is methylated to N-trimethylalanine , and two lysine residues are methylated to Nε, Nε, Nε-trimethyllysine . Methylation of L11 does not appear to be essential for its function . L11 is a target for the EG10443-MONOMER . L11 participates in joining the 30S initiation complex to the 50S subunit . Ribosome core particles lacking L11 do not display EF-G-dependent GTPase activity . The N-terminal domain of L11 participates in the formation of the arc-like connection between EF-G and L7/L12 during tRNA translocation . The universally conserved Pro22 residue undergoes a cis-trans isomerization. Molecular dynamics simulations showed that the cis configuration of Pro22 enables interaction of the N-terminal domain of L11 with the C-terminal domain of L12 . Site-directed mutagenesis of conserved residues in L11 and L12 elucidated their role in the interactions between L11, L12, and ribosome-associated GTPases...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7J7|protein.P0A7J7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013029,ECOCYC:EG10872,GeneID:948484`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4178447-4178875:+; feature_type=gene
