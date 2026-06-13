---
entity_id: "gene.b2426"
entity_type: "gene"
name: "ucpA"
source_database: "NCBI RefSeq"
source_id: "gene-b2426"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2426"
  - "ucpA"
---

# ucpA

`gene.b2426`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2426`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ucpA (gene.b2426) is a gene entity. It encodes ucpA (protein.P37440). Encoded protein function: Oxidoreductase UcpA (EC 1.-.-.-) EcoCyc product frame: EG12133-MONOMER. EcoCyc synonyms: yfeF. Genomic coordinates: 2543832-2544623. EcoCyc protein note: Based on sequence similarity, UcpA was predicted to be an acetoin dehydrogenase (diacetyl reductase) . Recent data show that UcpA is in fact able to reduce diacetyl to acetoin . A range of potential substrates, including diacetyl and acetoin, was previously tested in cell extracts of a strain overexpressing UcpA, and no increased activity compared to control extracts was found . Crp, FruR and IHF are involved in the regulation of ucpA . Expression of ucpA is upregulated by furfural, and overexpression of ucpA increases furan tolerance in an engineered E. coli strain and in the wild-type E. coli W strain . A knockout mutation of ucpA negatively affected conjugation efficiency after 24-48 hrs; UcpA's putative role in fermentation may help restore intracellular pH thus improving conjugation efficiency . UcpA: "upstream of cysP"

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37440|protein.P37440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007996,ECOCYC:EG12133,GeneID:946898`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2543832-2544623:-; feature_type=gene
