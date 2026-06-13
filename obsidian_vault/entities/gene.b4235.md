---
entity_id: "gene.b4235"
entity_type: "gene"
name: "tldE"
source_database: "NCBI RefSeq"
source_id: "gene-b4235"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4235"
  - "tldE"
---

# tldE

`gene.b4235`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4235`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tldE (gene.b4235) is a gene entity. It encodes pmbA (protein.P0AFK0). Encoded protein function: FUNCTION: Metalloprotease involved in CcdA degradation. Suppresses the inhibitory activity of the carbon storage regulator (CsrA). {ECO:0000269|PubMed:12029038}. EcoCyc product frame: EG10741-MONOMER. EcoCyc synonyms: mcb, pmbA. Genomic coordinates: 4457959-4459311. EcoCyc protein note: TldD and TldE form a stable heterodimeric complex with protease activity . tldE mutants harboring the pMccB17 plasmid show impaired production of Microcin B17 ; a deletion mutant accumulates the unprocessed Microcin B17 precursor protein, in contrast to wild type, which processes and exports Microcin B17 from the cell . A tldE mutant exhibits resistance to the F plasmid-encoded LetD DNA gyrase inhibitor , but only in the presence of the LetD inhibitor LetA . A csrA mutation suppresses the Tld phenotype of a tldE mutant . PmbA: "production of Microcin B17, locus A" TldE: "tolerant for letD expression E" Reviews:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFK0|protein.P0AFK0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013854,ECOCYC:EG10741,GeneID:948750`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4457959-4459311:+; feature_type=gene
