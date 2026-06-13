---
entity_id: "gene.b0199"
entity_type: "gene"
name: "metN"
source_database: "NCBI RefSeq"
source_id: "gene-b0199"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0199"
  - "metN"
---

# metN

`gene.b0199`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0199`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metN (gene.b0199) is a gene entity. It encodes metN (protein.P30750). Encoded protein function: FUNCTION: Part of the ABC transporter complex MetNIQ involved in methionine import (PubMed:12169620, PubMed:12218041, PubMed:12819857, PubMed:18621668, PubMed:30352853). Responsible for energy coupling to the transport system (PubMed:18621668, PubMed:25678706). It has also been shown to be involved in formyl-L-methionine transport (PubMed:12819857). {ECO:0000269|PubMed:12169620, ECO:0000269|PubMed:12218041, ECO:0000269|PubMed:12819857, ECO:0000269|PubMed:18621668, ECO:0000269|PubMed:25678706, ECO:0000269|PubMed:30352853}. EcoCyc product frame: ABC-MONOMER. EcoCyc synonyms: metD, abc. Genomic coordinates: 221614-222645. EcoCyc protein note: MetN is the ATP-binding component of a high affinity methionine ABC transporter. MetN contains a conserved nucleotide binding domain (NBD) linked to a C-terminal C2-domain; the C-2 domain binds selenomethionine and is implicated in the allosteric regulation of transporter activity; methionine binding to the C2-domain stabilizes an ATPase inactive conformation of the transporter . Overexpression of metN from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . abc: ATP-binding cassette

## Biological Role

Activated by yjiE (protein.P39376).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30750|protein.P30750]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P39376|protein.P39376]] `RegulonDB` `S` - regulator=HypT; target=metN; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000671,ECOCYC:EG11621,GeneID:944896`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:221614-222645:-; feature_type=gene
