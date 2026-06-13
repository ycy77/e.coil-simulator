---
entity_id: "gene.b2028"
entity_type: "gene"
name: "ugd"
source_database: "NCBI RefSeq"
source_id: "gene-b2028"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2028"
  - "ugd"
---

# ugd

`gene.b2028`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2028`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ugd (gene.b2028) is a gene entity. It encodes ugd (protein.P76373). Encoded protein function: UDP-glucose 6-dehydrogenase (UDP-Glc dehydrogenase) (UDP-GlcDH) (UDPGDH) (EC 1.1.1.22) EcoCyc product frame: UGD-MONOMER. EcoCyc synonyms: yefA, udg, UDG8, pmrE. Genomic coordinates: 2098447-2099613.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76373|protein.P76373]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ugd; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006734,ECOCYC:G7091,GeneID:946571`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2098447-2099613:-; feature_type=gene
