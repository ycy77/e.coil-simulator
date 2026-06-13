---
entity_id: "gene.b4265"
entity_type: "gene"
name: "idnT"
source_database: "NCBI RefSeq"
source_id: "gene-b4265"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4265"
  - "idnT"
---

# idnT

`gene.b4265`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4265`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

idnT (gene.b4265) is a gene entity. It encodes idnT (protein.P39344). Encoded protein function: FUNCTION: Transporter which is probably involved in L-idonate metabolism (PubMed:9658018). Transports L-idonate from the periplasm across the inner membrane (PubMed:9658018). Can also transport D-gluconate and 5-keto-D-gluconate (PubMed:17088549, PubMed:9119199). It has been reported that gluconate uptake probably occurs via a proton-symport mechanism in E.coli (PubMed:4585187). {ECO:0000269|PubMed:17088549, ECO:0000269|PubMed:4585187, ECO:0000269|PubMed:9119199, ECO:0000269|PubMed:9658018}. EcoCyc product frame: YJGT-MONOMER. EcoCyc synonyms: gntW, yjgT. Genomic coordinates: 4491206-4492525. EcoCyc protein note: IdnT is a probable L-idonate and D-gluconate transporter. Originally thought to be a subsidiary gluconate uptake system, the primary role of IdnT appears to be in L-idonate transport. The idnT gene is located in the idnDOTR operon involved in metabolising L-idonate to D-gluconate . Expression of this operon is induced by idonate or by 5-ketogluconate . The cloned idnT gene was shown to confer gluconate transport in a gluconate transport negative mutant in whole cell experiments with IdnT displaying a Km of 60 μM for gluconate . While direct transport of L-idonate has not been shown experimentally, IdnT-mediated gluconate transport is strongly inhibited by idonate...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39344|protein.P39344]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013969,ECOCYC:EG12539,GeneID:948798`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4491206-4492525:-; feature_type=gene
