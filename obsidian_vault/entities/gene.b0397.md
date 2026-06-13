---
entity_id: "gene.b0397"
entity_type: "gene"
name: "sbcC"
source_database: "NCBI RefSeq"
source_id: "gene-b0397"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0397"
  - "sbcC"
---

# sbcC

`gene.b0397`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0397`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbcC (gene.b0397) is a gene entity. It encodes sbcC (protein.P13458). Encoded protein function: FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity. EcoCyc product frame: EG10927-MONOMER. Genomic coordinates: 412607-415753. EcoCyc protein note: An sbcC mutation (sbcC201) overcomes the inviability of long palindromic nucleotide sequences . sbcC and sbcD form an operon in E. coli K-12 . SbcC is a member of the SMC (structural maintenance of chromosomes) family and contains conserved ATP binding motifs at each terminus and an internal coiled-coil domain interrupted by a central spacer which contains a half zinc-finger motif .

## Biological Role

Repressed by phoB (protein.P0AFJ5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13458|protein.P13458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=sbcC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001381,ECOCYC:EG10927,GeneID:949076`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:412607-415753:-; feature_type=gene
