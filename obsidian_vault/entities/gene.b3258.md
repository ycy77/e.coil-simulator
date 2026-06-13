---
entity_id: "gene.b3258"
entity_type: "gene"
name: "panF"
source_database: "NCBI RefSeq"
source_id: "gene-b3258"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3258"
  - "panF"
---

# panF

`gene.b3258`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3258`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

panF (gene.b3258) is a gene entity. It encodes panF (protein.P16256). Encoded protein function: FUNCTION: Catalyzes the sodium-dependent uptake of extracellular pantothenate. {ECO:0000269|PubMed:2193919, ECO:0000269|PubMed:3888959}. EcoCyc product frame: PANF-MONOMER. Genomic coordinates: 3407607-3409058. EcoCyc protein note: PanF is a pantothenate transporter which probably functions as a pantothenate/cation symporter. Whole cell transport assays have shown that the cloned panF gene can complement panF mutants with pantothenate transport defects . Overexpression of panF lead to increased pantothenate accumulation. Whole cell transport experiments have shown that PanF mediates high affinity pantothenate transport with a Km of approx 0.4 μM and pantothenate uptake was stimulated by the presence of sodium ions . PanF is a member of the SSS family of sodium/solute symporters, supporting the notion that it functions as a sodium/pantothenate symporter . Imported pantothenate is phosphorylated by pantothenate kinase, a key step in Coenzyme A synthesis.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16256|protein.P16256]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=panF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010695,ECOCYC:EG10685,GeneID:947752`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3407607-3409058:+; feature_type=gene
