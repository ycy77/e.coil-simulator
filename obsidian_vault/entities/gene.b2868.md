---
entity_id: "gene.b2868"
entity_type: "gene"
name: "xdhC"
source_database: "NCBI RefSeq"
source_id: "gene-b2868"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2868"
  - "xdhC"
---

# xdhC

`gene.b2868`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2868`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xdhC (gene.b2868) is a gene entity. It encodes xdhC (protein.Q46801). Encoded protein function: FUNCTION: Iron-sulfur subunit of the xanthine dehydrogenase complex. EcoCyc product frame: G7487-MONOMER. EcoCyc synonyms: ygeU. Genomic coordinates: 3003489-3003968. EcoCyc protein note: XdhC has similarity to the iron-binding regions of Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase .

## Biological Role

Activated by rpoN (protein.P24255).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q46801|protein.Q46801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=xdhC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009418,ECOCYC:G7487,GeneID:945148`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3003489-3003968:+; feature_type=gene
