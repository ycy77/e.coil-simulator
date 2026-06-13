---
entity_id: "gene.b0127"
entity_type: "gene"
name: "yadG"
source_database: "NCBI RefSeq"
source_id: "gene-b0127"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0127"
  - "yadG"
---

# yadG

`gene.b0127`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0127`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yadG (gene.b0127) is a gene entity. It encodes yadG (protein.P36879). Encoded protein function: Uncharacterized ABC transporter ATP-binding protein YadG EcoCyc product frame: YADG-MONOMER. Genomic coordinates: 142779-143705. EcoCyc protein note: YadG is the predicted ATP-binding subunit of a putative ATP-binding cassette (ABC) exporter complex . yadG transcription increases specifically in response to CPD-9138 and its indicator compounds 1,3-DNB, 2,4-DNT, and 2,6-DNT; the response was utilized for construction of an E. coli biosensor strain . A yadG deletion mutant is 2 fold more sensitive to X-radiation than wild type . This minimally characterized enzyme in E. coli was found to interact with the ENOLASE-MONOMER enzyme in glycolysis in a large assessment of protein-protein interactions (PPIs) . This protein was also shown to interact with the enzyme GLUTDECARBOXB-MONOMER in a protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions. This PEI may have a metabolic regulatory role in the PWY0-1305 pathway, in part because the PEI is conserved across many other bacterial taxa .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36879|protein.P36879]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000447,ECOCYC:EG12320,GeneID:944833`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:142779-143705:+; feature_type=gene
