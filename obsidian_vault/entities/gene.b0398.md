---
entity_id: "gene.b0398"
entity_type: "gene"
name: "sbcD"
source_database: "NCBI RefSeq"
source_id: "gene-b0398"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0398"
  - "sbcD"
---

# sbcD

`gene.b0398`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0398`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbcD (gene.b0398) is a gene entity. It encodes sbcD (protein.P0AG76). Encoded protein function: FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can inhibit DNA replication and are intermediates in certain DNA recombination reactions. The complex acts as a 3'->5' double strand exonuclease that can open hairpins. It also has a 5' single-strand endonuclease activity. EcoCyc product frame: EG11094-MONOMER. EcoCyc synonyms: yajA. Genomic coordinates: 415750-416952. EcoCyc protein note: An sbcD mutation (sbcD::kan) permits the stable propagation of bacteriophage containing a long palindromic nucleotide sequence; sbcD and sbcC form an operon in E. coli K-12 . SbcD belongs to a subgroup of phosphoesterases that are associated with recombination and DNA repair .

## Biological Role

Repressed by phoB (protein.P0AFJ5), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG76|protein.P0AG76]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `C` - regulator=PhoB; target=sbcD; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=sbcD; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001383,ECOCYC:EG11094,GeneID:945049`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:415750-416952:-; feature_type=gene
