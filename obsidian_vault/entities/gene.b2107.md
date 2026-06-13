---
entity_id: "gene.b2107"
entity_type: "gene"
name: "rcnB"
source_database: "NCBI RefSeq"
source_id: "gene-b2107"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2107"
  - "rcnB"
---

# rcnB

`gene.b2107`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2107`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rcnB (gene.b2107) is a gene entity. It encodes rcnB (protein.P64534). Encoded protein function: FUNCTION: Influences nickel and cobalt homeostasis. May act by modulating RcnA-mediated export of these ions to avoid excess efflux. Not involved in nickel import and does not bind nickel or cobalt ions directly. {ECO:0000269|PubMed:21665978}. EcoCyc product frame: G7139-MONOMER. EcoCyc synonyms: yohN. Genomic coordinates: 2186960-2187298. EcoCyc protein note: Deletion of rcnB in the K-12 derived strain W3110, results in increased resistance to nickel and cobalt and ΔrcnB mutants show reduced intracellular levels of nickel and cobalt; a ΔrcnB strain has increased rates of nickel efflux compared to wild type . RcnB may act to regulate RcnA mediated nickel efflux . RcnB is located in the periplasm; purified RcnB does not bind nickel or cobalt . RcnB binds copper in vitro and in vivo; purified RcnB binds one atom of Cu per monomer with micromolar affinity . rcnB is not induced by copper and does not appear to be involved in copper homeostasis . Disruption of a conserved potential copper binding motif renders the RcnAB efflux system ineffective with respect to nickel and cobalt resistance which suggests that copper binding by RcnB is essential for function...

## Biological Role

Repressed by rcnR (protein.P64530).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64534|protein.P64534]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P64530|protein.P64530]] `RegulonDB` `S` - regulator=RcnR; target=rcnB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006970,ECOCYC:G7139,GeneID:949080`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2186960-2187298:+; feature_type=gene
