---
entity_id: "gene.b1350"
entity_type: "gene"
name: "recE"
source_database: "NCBI RefSeq"
source_id: "gene-b1350"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1350"
  - "recE"
---

# recE

`gene.b1350`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1350`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recE (gene.b1350) is a gene entity. It encodes recE (protein.P15032). Encoded protein function: FUNCTION: Is involved in the RecE pathway of recombination. Catalyzes the degradation of double-stranded DNA. Acts progressively in a 5' to 3' direction, releasing 5'-phosphomononucleotides. Has a strong preference for linear duplex substrate DNA and appears to be unable to initiate degradation from single-stranded breaks in DNA. EcoCyc product frame: EG10827-MONOMER. EcoCyc synonyms: rmuB, rac, sbcA. Genomic coordinates: 1414786-1417386. EcoCyc protein note: DNA damage can occur due to a variety of environmental assaults including UV irradiation and chemical agents. Escherichia coli has a number of complex enzymatic pathways for the repair of DNA damage. Most DNA damage involves lesions to one strand of DNA, but in some cases damage can occur to both strands. Double strand breaks (DSBs) cannot be repaired via excision repair pathways because by their nature they lack an intact strand to be used as a template. Repair of DSBs utilize the RecA pathway of homologous recombination with a separate, intact, homologous region of DNA. The RecE (also known as exonuclease VIII) pathway is an alternative pathway for the initiation of homologous recombination in Escherichia coli. The RecE pathway is activated in recB, recC sbcA (suppressors of recB and recC) mutants...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15032|protein.P15032]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0004531,ECOCYC:EG10827,GeneID:945918`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1414786-1417386:-; feature_type=gene
