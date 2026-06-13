---
entity_id: "gene.b3053"
entity_type: "gene"
name: "glnE"
source_database: "NCBI RefSeq"
source_id: "gene-b3053"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3053"
  - "glnE"
---

# glnE

`gene.b3053`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3053`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glnE (gene.b3053) is a gene entity. It encodes glnE (protein.P30870). Encoded protein function: FUNCTION: Involved in the regulation of glutamine synthetase GlnA, a key enzyme in the process to assimilate ammonia (PubMed:8412694). When cellular nitrogen levels are high, the C-terminal adenylyl transferase inactivates GlnA by covalent transfer of an adenylyl group from ATP to 'Tyr-398' of GlnA, thus reducing its activity (PubMed:4920894, PubMed:9312015). Conversely, when nitrogen levels are low, the N-terminal adenylyl removase (AR) activates GlnA by removing the adenylyl group by phosphorolysis, increasing its activity (PubMed:14766310, PubMed:4893578, PubMed:4920873, PubMed:4934180, PubMed:9312015). The regulatory region of GlnE binds the signal transduction protein PII (GlnB) which indicates the nitrogen status of the cell (PubMed:8412694). {ECO:0000269|PubMed:14766310, ECO:0000269|PubMed:4867671, ECO:0000269|PubMed:4893578, ECO:0000269|PubMed:4920873, ECO:0000269|PubMed:4920894, ECO:0000269|PubMed:4934180, ECO:0000269|PubMed:8412694, ECO:0000269|PubMed:9312015}. EcoCyc product frame: GLNE-MONOMER. Genomic coordinates: 3196801-3199641. EcoCyc protein note: glnE encodes a bifunctional polypeptide having both glutamine synthetase adenylyltransferase (ATase) activity and glutamine synthetase deadenylase activity (ATd)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30870|protein.P30870]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010018,ECOCYC:EG11602,GeneID:947552`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3196801-3199641:-; feature_type=gene
