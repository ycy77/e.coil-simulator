---
entity_id: "gene.b0613"
entity_type: "gene"
name: "citG"
source_database: "NCBI RefSeq"
source_id: "gene-b0613"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0613"
  - "citG"
---

# citG

`gene.b0613`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0613`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

citG (gene.b0613) is a gene entity. It encodes citG (protein.P77231). Encoded protein function: FUNCTION: Catalyzes the formation of 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A, the precursor of the prosthetic group of the holo-acyl carrier protein (gamma chain) of citrate lyase, from ATP and dephospho-CoA. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}. EcoCyc product frame: G6339-MONOMER. EcoCyc synonyms: ybdT. Genomic coordinates: 646631-647509. EcoCyc protein note: CitG catalyzes the synthesis of the citrate lyase prosthetic group precursor, 2'-(5''-triphosphoribosyl)-3'-dephospho-CoA, from dephospho-CoA and ATP. The enzyme does not catalyze the conversion of AMP-ACP to holo-ACP . Overexpression of citG from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Biological Role

Activated by dpiA (protein.P0AEF4).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77231|protein.P77231]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEF4|protein.P0AEF4]] `RegulonDB` `S` - regulator=DpiA; target=citG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002114,ECOCYC:G6339,GeneID:946395`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:646631-647509:-; feature_type=gene
