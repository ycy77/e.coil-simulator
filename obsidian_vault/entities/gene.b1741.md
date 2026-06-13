---
entity_id: "gene.b1741"
entity_type: "gene"
name: "cho"
source_database: "NCBI RefSeq"
source_id: "gene-b1741"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1741"
  - "cho"
---

# cho

`gene.b1741`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1741`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cho (gene.b1741) is a gene entity. It encodes cho (protein.P76213). Encoded protein function: FUNCTION: Incises the DNA at the 3' side of a lesion during nucleotide excision repair. Incises the DNA farther away from the lesion than UvrC. Not able to incise the 5' site of a lesion. In vitro, the incision activity of Cho is UvrA and UvrB dependent. When a lesion remains because UvrC is not able to induce the 3' incision, Cho incises the DNA. Then UvrC makes the 5' incision. The combined action of Cho and UvrC broadens the substrate range of nucleotide excision repair. {ECO:0000269|PubMed:11818552}. EcoCyc product frame: G6937-MONOMER. EcoCyc synonyms: ydjQ. Genomic coordinates: 1823515-1824402. EcoCyc protein note: Cho is a UvrAB dependent endonuclease which may contribute to the excision repair of DNA lesions that are poorly incised by EG11063-MONOMER "UvrC". Purified Cho has UvrAB dependent endonuclease activity in vitro; unlike UvrC which incises at the 3' and 5' side of a DNA lesion, Cho is only capable of a damage-dependent 3' incision; the efficiency of Cho incision is affected by the type of damaged substrate . Cho and UvrC exhibit distinct sites of incision relative to the position of the DNA lesion and distinct sites of binding to UvrB; damaged DNA that is incised by Cho at the 3' side can be further processed by incision at the 5' side by the UvrC protein...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76213|protein.P76213]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=cho; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005807,ECOCYC:G6937,GeneID:948996`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1823515-1824402:+; feature_type=gene
