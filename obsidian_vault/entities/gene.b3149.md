---
entity_id: "gene.b3149"
entity_type: "gene"
name: "diaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3149"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3149"
  - "diaA"
---

# diaA

`gene.b3149`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3149`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

diaA (gene.b3149) is a gene entity. It encodes diaA (protein.P66817). Encoded protein function: FUNCTION: Required for the timely initiation of chromosomal replication via direct interactions with the DnaA initiator protein. {ECO:0000269|PubMed:15326179, ECO:0000269|PubMed:17699754}. EcoCyc product frame: YRAO-MONOMER. EcoCyc synonyms: yraO. Genomic coordinates: 3295809-3296399. EcoCyc protein note: Proper amounts of DiaA are required for the timely initiation of chromosomal replication. DiaA interacts directly with the N-terminal domains I-II of PD03831 DnaA in a DNA-independent manner and stimulates the assembly of DnaA on G0-10506 oriC, conformational changes in the initiation complex, and unwinding of oriC . Both DnaA binding and homotetramerization of DiaA are required for stimulation of replication . A crystal structure of DiaA has been solved at 1.8 Å resolution, showing that DiaA forms a homotetramer . Residues required for tetramerization or DnaA binding were identified by mutagenesis . DnaA F46 is the crucial residue that is required for interaction with DiaA as well as DnaB . Timing of replication initiation is disrupted in both a diaA mutant and a DiaA overexpression strain . DiaA: "DnaA initiator-associating factor A" Reviews:

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P66817|protein.P66817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010348,ECOCYC:EG12780,GeneID:947661`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3295809-3296399:+; feature_type=gene
