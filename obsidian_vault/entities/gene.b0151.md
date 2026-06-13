---
entity_id: "gene.b0151"
entity_type: "gene"
name: "fhuC"
source_database: "NCBI RefSeq"
source_id: "gene-b0151"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0151"
  - "fhuC"
---

# fhuC

`gene.b0151`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0151`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fhuC (gene.b0151) is a gene entity. It encodes fhuC (protein.P07821). Encoded protein function: FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Responsible for energy coupling to the transport system. {ECO:0000269|PubMed:1551849, ECO:0000269|PubMed:34887516}. EcoCyc product frame: FHUC-MONOMER. Genomic coordinates: 169778-170575. EcoCyc protein note: FhuC is the predicted ATP-binding subunit of a high-affinity transport system for the uptake of iron (III)-hydroxamate compounds such as ferrichrome and ferric coprogen. FhuC contains signature motifs conserved in ATP-binding cassette (ABC) domains .

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07821|protein.P07821]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fhuC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000522,ECOCYC:EG10304,GeneID:945250`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:169778-170575:+; feature_type=gene
