---
entity_id: "gene.b1782"
entity_type: "gene"
name: "mipA"
source_database: "NCBI RefSeq"
source_id: "gene-b1782"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1782"
  - "mipA"
---

# mipA

`gene.b1782`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1782`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mipA (gene.b1782) is a gene entity. It encodes mipA (protein.P0A908). Encoded protein function: FUNCTION: May serve as a scaffold protein required for the formation of a complex with MrcB/PonB and MltA, this complex could play a role in enlargement and septation of the murein sacculus. EcoCyc product frame: G6968-MONOMER. EcoCyc synonyms: yeaF. Genomic coordinates: 1865726-1866472. EcoCyc protein note: MipA, MltA-interacting protein, is a scaffolding protein that forms a trimer with PBP1B, a murein polymerase, and MltA, a murein hydrolase . MipA is found in the membrane fraction and has been identified as an integral outer membrane protein by 2D electrophoresis and peptide mass fingerprinting . It shares low sequence similarity with the porin-like protein Omp26La of Listonella anguillarum and is predicted to contain β-barrel structure . MipA binds specifically to MltA and PBP1B . Overexpression of mipA results in cell lysis due to compromised membrane integrity . Multicopy expression results in increased σE-dependent expression of degP and rybB . mipA is predicted to be a member of the CRP regulon . Expression of mipA is induced by addition of the conjugative plasmid R1drd19 and decreased upon exposure to acetate .

## Biological Role

Activated by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A908|protein.P0A908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=mipA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005928,ECOCYC:G6968,GeneID:946301`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1865726-1866472:-; feature_type=gene
