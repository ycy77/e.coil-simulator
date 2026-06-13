---
entity_id: "gene.b4166"
entity_type: "gene"
name: "queG"
source_database: "NCBI RefSeq"
source_id: "gene-b4166"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4166"
  - "queG"
---

# queG

`gene.b4166`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4166`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

queG (gene.b4166) is a gene entity. It encodes queG (protein.P39288). Encoded protein function: FUNCTION: Catalyzes the conversion of epoxyqueuosine (oQ) to queuosine (Q), which is a hypermodified base found in the wobble positions of tRNA(Asp), tRNA(Asn), tRNA(His) and tRNA(Tyr). {ECO:0000255|HAMAP-Rule:MF_00916}. EcoCyc product frame: G7843-MONOMER. EcoCyc synonyms: yjeS. Genomic coordinates: 4392928-4394067. EcoCyc protein note: Epoxyqueuosine reductase catalyzes the final step in the de novo synthesis of queuosine, the anticodon loop modification found in tRNA(Asp), tRNA(Asn), tRNA(His), and tRNA(Tyr) . The enzyme was identified by screening the Keio collection of single-gene knockouts for the presence of epoxyqueuosine (oQ) and lack of queuosine (Q) in tRNAs by tandem UV-visible spectrophotometry and mass spectroscopy .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39288|protein.P39288]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013641,ECOCYC:G7843,GeneID:948686`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4392928-4394067:-; feature_type=gene
