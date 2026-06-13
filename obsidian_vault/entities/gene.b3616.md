---
entity_id: "gene.b3616"
entity_type: "gene"
name: "tdh"
source_database: "NCBI RefSeq"
source_id: "gene-b3616"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3616"
  - "tdh"
---

# tdh

`gene.b3616`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3616`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tdh (gene.b3616) is a gene entity. It encodes tdh (protein.P07913). Encoded protein function: FUNCTION: Catalyzes the NAD(+)-dependent oxidation of L-threonine to 2-amino-3-ketobutyrate. To a lesser extent, also catalyzes the oxidation of D-allo-threonine and L-threonine amide, but not that of D-threonine and L-allothreonine. Cannot utilize NADP(+) instead of NAD(+). {ECO:0000269|PubMed:6780553}. EcoCyc product frame: THREODEHYD-MONOMER. Genomic coordinates: 3790320-3791345.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07913|protein.P07913]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=tdh; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011830,ECOCYC:EG10993,GeneID:948139`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3790320-3791345:-; feature_type=gene
