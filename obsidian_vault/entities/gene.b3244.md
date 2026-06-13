---
entity_id: "gene.b3244"
entity_type: "gene"
name: "tldD"
source_database: "NCBI RefSeq"
source_id: "gene-b3244"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3244"
  - "tldD"
---

# tldD

`gene.b3244`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3244`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tldD (gene.b3244) is a gene entity. It encodes tldD (protein.P0AGG8). Encoded protein function: FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}. EcoCyc product frame: G7689-MONOMER. EcoCyc synonyms: yhdO. Genomic coordinates: 3390583-3392028. EcoCyc protein note: TldD and TldE form a stable heterodimeric complex with protease activity. TldD contains a metalloprotease-like HExxxH motif; the two His residues were shown to coordinate a metal ion in the crystal structure. A His262Ala mutant in the HExxxH motif lacks activity . A ΔtldD mutant harboring the pMccB17 plasmid accumulates the unprocessed Microcin B17 precursor protein, in contrast to wild type, which processes and exports Microcin B17 from the cell . A tldD mutant exhibits resistance to the F plasmid-encoded LetD DNA gyrase inhibitor , but only in the presence of the LetD inhibitor LetA . A csrA mutation suppresses the Tld phenotype of a tldD mutant . TldD: "tolerant for letD expression D" Reviews:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGG8|protein.P0AGG8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010642,ECOCYC:G7689,GeneID:947749`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3390583-3392028:-; feature_type=gene
