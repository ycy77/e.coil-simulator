---
entity_id: "gene.b2576"
entity_type: "gene"
name: "srmB"
source_database: "NCBI RefSeq"
source_id: "gene-b2576"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2576"
  - "srmB"
---

# srmB

`gene.b2576`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2576`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srmB (gene.b2576) is a gene entity. It encodes srmB (protein.P21507). Encoded protein function: FUNCTION: DEAD-box RNA helicase involved in the assembly of the 50S ribosomal subunit at low temperature. Exhibits RNA-stimulated ATP hydrolysis and RNA unwinding activity. Acts before DeaD. {ECO:0000255|HAMAP-Rule:MF_00967, ECO:0000269|PubMed:12787353, ECO:0000269|PubMed:15148362, ECO:0000269|PubMed:15196029}. EcoCyc product frame: EG10975-MONOMER. EcoCyc synonyms: rbaB, rhlA. Genomic coordinates: 2712896-2714230. EcoCyc protein note: SrmB is a DEAD-box protein with RNA helicase activity that facilitates an early step in the assembly of the 50S subunit of the ribosome . Recent data suggest that SrmB facilitates ribosome assembly by acting both as an RNA chaperone to resolve misfolded and trapped RNA structures and by stabilizing early ribosomal protein and rRNA binding events . The SrmB protein was found to be associated with a pre-50S ribosomal particle and forms a complex with ribosomal proteins L4, L24, and the region of 23S rRNA that interacts with L4 and L24 . The site of SrmB action is different from its binding site; models for SrmB activity during 50S ribosomal subunit assembly are presented...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21507|protein.P21507]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008478,ECOCYC:EG10975,GeneID:947055`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2712896-2714230:+; feature_type=gene
