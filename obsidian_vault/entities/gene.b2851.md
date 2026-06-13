---
entity_id: "gene.b2851"
entity_type: "gene"
name: "ygeG"
source_database: "NCBI RefSeq"
source_id: "gene-b2851"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2851"
  - "ygeG"
---

# ygeG

`gene.b2851`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2851`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygeG (gene.b2851) is a gene entity. It encodes ygeG (protein.Q46787). Encoded protein function: Uncharacterized protein YgeG EcoCyc product frame: G7471-MONOMER. Genomic coordinates: 2991268-2991759. EcoCyc protein note: ygeG is located within a remnant of an ETT2 (type III secretion system) pathogenicity island that is fully present in pathogenic strains such as E. coli O157:H7 and at least partially present in most sequenced E. coli and Shigella strains . ETT2 has been shown to contribute to pathogenesis .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46787|protein.Q46787]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ygeG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009364,ECOCYC:G7471,GeneID:946986`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2991268-2991759:+; feature_type=gene
