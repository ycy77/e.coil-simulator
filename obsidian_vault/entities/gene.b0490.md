---
entity_id: "gene.b0490"
entity_type: "gene"
name: "fetA"
source_database: "NCBI RefSeq"
source_id: "gene-b0490"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0490"
  - "fetA"
---

# fetA

`gene.b0490`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0490`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fetA (gene.b0490) is a gene entity. It encodes fetA (protein.P77279). Encoded protein function: FUNCTION: Part of the ABC transporter complex FetAB, which is probably involved in iron export and enhances resistance to H(2)O(2)-mediated oxidative stress. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:24038693}. EcoCyc product frame: YBBL-MONOMER. EcoCyc synonyms: ybbL. Genomic coordinates: 515919-516596. EcoCyc protein note: FetA is the predicted ATP-binding subunit of a putative ABC family transporter which has a role in iron homeostasis. Overexpression of fetAB increases resistance to H2O2 induced stress in the presence of Fe2+. Overexpression of fetAB decreases the intracellular iron levels of an E. coli K-12 Δfur strain. An E. coli K-12 ΔfetA strain has increased sensitivity to H2O2 compared to wild-type. Overexpression of fetAB from a plasmid abrogates the H2O2 sensitivity of the fetA knockout strain. Sequence analysis suggests that fetA is the ATP-binding subunit of an ABC-type transporter . fet: Fe transport

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77279|protein.P77279]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001703,ECOCYC:G6266,GeneID:946990`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:515919-516596:+; feature_type=gene
