---
entity_id: "gene.b3068"
entity_type: "gene"
name: "mug"
source_database: "NCBI RefSeq"
source_id: "gene-b3068"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3068"
  - "mug"
---

# mug

`gene.b3068`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3068`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mug (gene.b3068) is a gene entity. It encodes mug (protein.P0A9H1). Encoded protein function: FUNCTION: Excises ethenocytosine and uracil, which can arise by alkylation or deamination of cytosine, respectively, from the corresponding mispairs with guanine in ds-DNA. It is capable of hydrolyzing the carbon-nitrogen bond between the sugar-phosphate backbone of the DNA and the mispaired base. The complementary strand guanine functions in substrate recognition. Required for DNA damage lesion repair in stationary-phase cells. {ECO:0000269|PubMed:12668677, ECO:0000269|PubMed:8878487}. EcoCyc product frame: EG12717-MONOMER. EcoCyc synonyms: ygjF. Genomic coordinates: 3214967-3215473. EcoCyc protein note: Mug is a glycosylase that acts in DNA repair . Mug shows activity toward G:U and G:T base mismatches . Mug also shows activity toward epsilonC (3,N4-ethenocytosine) , 8-HM-epsilondC (8-(hydroxymethyl)-3,N4-etheno-2'-deoxycytidine) , 1,N(2)-epsilonG (1,N(2)-ethenoguanine) lesions , and 5-formyluracil lesions. Structural models for the specificity of the enzyme for G:U and G:T base mispairings and for the G:U preference of the enzyme are presented. The substrate specificity of the enzyme is discussed in detail . Mug activity reduces mutation during stationary phase , whereas it does not play a large role in DNA repair during cell growth...

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9H1|protein.P0A9H1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010073,ECOCYC:EG12717,GeneID:947560`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3214967-3215473:-; feature_type=gene
