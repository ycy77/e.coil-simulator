---
entity_id: "gene.b3842"
entity_type: "gene"
name: "rfaH"
source_database: "NCBI RefSeq"
source_id: "gene-b3842"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3842"
  - "rfaH"
---

# rfaH

`gene.b3842`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3842`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rfaH (gene.b3842) is a gene entity. It encodes rfaH (protein.P0AFW0). Encoded protein function: FUNCTION: Enhances distal genes transcription elongation in a specialized subset of operons that encode extracytoplasmic components. RfaH is recruited into a multi-component RNA polymerase complex by the ops element, which is a short conserved DNA sequence located downstream of the main promoter of these operons. Once bound, RfaH suppresses pausing and inhibits Rho-dependent and intrinsic termination at a subset of sites. Termination signals are bypassed, which allows complete synthesis of long RNA chains. Enhances expression of several operons involved in synthesis of lipopolysaccharides, exopolysaccharides, hemolysin, and sex factor. Also negatively controls expression and surface presentation of AG43 and possibly another AG43-independent factor that mediates cell-cell interactions and biofilm formation. {ECO:0000255|HAMAP-Rule:MF_00951, ECO:0000269|PubMed:10660066, ECO:0000269|PubMed:11983161, ECO:0000269|PubMed:12007406, ECO:0000269|PubMed:1584020, ECO:0000269|PubMed:16452414, ECO:0000269|PubMed:8606157, ECO:0000269|PubMed:8951819, ECO:0000269|PubMed:9171395, ECO:0000269|PubMed:9426123}. EcoCyc product frame: EG10839-MONOMER. EcoCyc synonyms: hlyT, sfrB. Genomic coordinates: 4024333-4024821...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFW0|protein.P0AFW0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=rfaH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012553,ECOCYC:EG10839,GeneID:948327`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4024333-4024821:-; feature_type=gene
