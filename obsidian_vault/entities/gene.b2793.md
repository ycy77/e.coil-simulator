---
entity_id: "gene.b2793"
entity_type: "gene"
name: "syd"
source_database: "NCBI RefSeq"
source_id: "gene-b2793"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2793"
  - "syd"
---

# syd

`gene.b2793`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2793`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

syd (gene.b2793) is a gene entity. It encodes syd (protein.P0A8U0). Encoded protein function: FUNCTION: Interacts with the SecY protein in vivo. May bind preferentially to an uncomplexed state of SecY, thus functioning either as a chelating agent for excess SecY in the cell or as a regulatory factor that negatively controls the translocase function. EcoCyc product frame: G7451-MONOMER. EcoCyc synonyms: ydr. Genomic coordinates: 2924735-2925280. EcoCyc protein note: The Syd protein may serve as a quality control system for assembly of the SecY secretion channel . Syd interacts with the cytosolic C4 and C5 loops of SecY, a membrane-embedded subunit of protein translocase . Purified Syd protein inhibits the ATPase activity of SecA and the protein translocation activity of a secY24 mutant and is able to destabilize SecYEG dimers in vitro . Syd is loosely associated with the cytoplasmic surface of the inner membrane . A crystal structure of Syd has been solved at 2 Å resolution. In solution, Syd is monomeric and forms a 1:1 complex with the SecYEG complex . Overexpression of syd suppresses the phenotype of the secY-d1 mutation . Deletion of syd causes no obvious phenotype . Syd: "suppressor of secY dominance"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8U0|protein.P0A8U0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0009154,ECOCYC:G7451,GeneID:947271`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2924735-2925280:-; feature_type=gene
