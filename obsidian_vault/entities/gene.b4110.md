---
entity_id: "gene.b4110"
entity_type: "gene"
name: "rdcB"
source_database: "NCBI RefSeq"
source_id: "gene-b4110"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4110"
  - "rdcB"
---

# rdcB

`gene.b4110`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4110`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rdcB (gene.b4110) is a gene entity. It encodes rdcB (protein.P39267). Encoded protein function: FUNCTION: Regulatory protein that, together with its partner protein RdcA, activates the diguanylate cyclase E (DgcE) to control CsgD and biofilm matrix production (PubMed:31022167). RdcB acts as an accessory component, forming a complex with RdcA and contributing to the activation of DgcE, but it does not directly interact with DgcE (PubMed:31022167). {ECO:0000269|PubMed:31022167}. EcoCyc product frame: G7823-MONOMER. EcoCyc synonyms: yjcZ. Genomic coordinates: 4329360-4330238. EcoCyc protein note: Together with RdcA, RdcB controls the activity of the DgcE diguanylate cyclase . RdcB physically interacts with RdcA, which is able to interact with DgcE and regulate its activity . The mRNA of rdcB appears to interact with the small regulatory RNA GlnZ, but it is not known how it regulates such mRNA . A mutation in rdcB partially suppresses the motility defect of a ΔpdeH mutant . A ΔrdcB mutant shows a defect in biofilm formation . RdcB: "regulator of a diguanylate cyclase B"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39267|protein.P39267]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013459,ECOCYC:G7823,GeneID:948633`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4329360-4330238:+; feature_type=gene
