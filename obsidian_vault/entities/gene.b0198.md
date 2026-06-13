---
entity_id: "gene.b0198"
entity_type: "gene"
name: "metI"
source_database: "NCBI RefSeq"
source_id: "gene-b0198"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0198"
  - "metI"
---

# metI

`gene.b0198`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0198`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metI (gene.b0198) is a gene entity. It encodes metI (protein.P31547). Encoded protein function: FUNCTION: Part of the binding-protein-dependent transport system for D-methionine and the toxic methionine analog alpha-methyl-methionine. Probably responsible for the translocation of the substrate across the membrane. {ECO:0000269|PubMed:12169620}.; FUNCTION: (Microbial infection) Probably transports the toxic C-terminal region of CdiA from E.coli strain MHI813 across the inner membrane to the cytoplasm, where CdiA has a toxic effect. Toxin transport is strain-specific, mutations in this gene do not confer resistance to several other tested CdiA toxins. {ECO:0000269|PubMed:26305955}. EcoCyc product frame: METI-MONOMER. EcoCyc synonyms: metD, yaeE. Genomic coordinates: 220968-221621. EcoCyc protein note: MetI is the integral membrane subunit of a high affinity methionine ABC transporter...

## Biological Role

Activated by yjiE (protein.P39376).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31547|protein.P31547]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P39376|protein.P39376]] `RegulonDB` `S` - regulator=HypT; target=metI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000668,ECOCYC:EG11737,GeneID:944894`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:220968-221621:-; feature_type=gene
