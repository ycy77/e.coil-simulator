---
entity_id: "gene.b0260"
entity_type: "gene"
name: "mmuP"
source_database: "NCBI RefSeq"
source_id: "gene-b0260"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0260"
  - "mmuP"
---

# mmuP

`gene.b0260`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0260`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mmuP (gene.b0260) is a gene entity. It encodes mmuP (protein.Q47689). Encoded protein function: FUNCTION: Transporter for the intake of S-methylmethionine. EcoCyc product frame: B0260-MONOMER. EcoCyc synonyms: ykfD. Genomic coordinates: 275325-276728. EcoCyc protein note: MmuP belongs to the APC superfamily of amino acid transporters and is a putative S-methylmethionine transporter . A mutant with a non-polar in-frame deletion in mmuP is unable to utilize S-methylmethionine as a source of methionine in a metE metH mutant background . MmuP does not contribute to the uptake of L- or D-methionine . mmuP forms a putative operon with mmuM (encoding a homocysteine S-methyltransferase); mmuPM expression is regulated by methionine; the synthesis of MmuM is significantly reduced when high concentrations of L-methionine are present in the culture media . MmuP: "S-methylmethionine utilization"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47689|protein.Q47689]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0000893,ECOCYC:G6135,GeneID:946284`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:275325-276728:+; feature_type=gene
