---
entity_id: "gene.b2371"
entity_type: "gene"
name: "yfdE"
source_database: "NCBI RefSeq"
source_id: "gene-b2371"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2371"
  - "yfdE"
---

# yfdE

`gene.b2371`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2371`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfdE (gene.b2371) is a gene entity. It encodes yfdE (protein.P76518). Encoded protein function: FUNCTION: Involved in the catabolism of oxalate and in the adapatation to low pH. ACOCT serves to prime the oxalate-induced acid tolerance response (ATR) cycle by producing substrate for oxalyl-CoA decarboxylase (OXC) and formyl-coenzyme A transferase (FCOCT). Catalyzes the reversible conversion of acetyl-CoA and oxalate to oxalyl-CoA and acetate. It can also use formyl-CoA and oxalate to produce oxalyl-CoA and formate with significantly reduced specific activity. {ECO:0000269|PubMed:23935849}. EcoCyc product frame: G7234-MONOMER. Genomic coordinates: 2488023-2489168.

## Biological Role

Repressed by nac (protein.Q47005). Activated by evgA (protein.P0ACZ4).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76518|protein.P76518]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=yfdE; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yfdE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007821,ECOCYC:G7234,GeneID:946432`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2488023-2489168:-; feature_type=gene
