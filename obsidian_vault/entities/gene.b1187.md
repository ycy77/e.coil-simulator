---
entity_id: "gene.b1187"
entity_type: "gene"
name: "fadR"
source_database: "NCBI RefSeq"
source_id: "gene-b1187"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1187"
  - "fadR"
---

# fadR

`gene.b1187`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1187`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadR (gene.b1187) is a gene entity. It encodes fadR (protein.P0A8V6). Encoded protein function: FUNCTION: Multifunctional regulator of fatty acid metabolism (PubMed:11859088, PubMed:1569108, PubMed:19854834, PubMed:21276098, PubMed:8446033, PubMed:9388199). Represses transcription of at least eight genes required for fatty acid transport and beta-oxidation including fadA, fadB, fadD, fadL and fadE (PubMed:9388199). Activates transcription of at least three genes required for unsaturated fatty acid biosynthesis: fabA, fabB and iclR, the gene encoding the transcriptional regulator of the aceBAK operon encoding the glyoxylate shunt enzymes (PubMed:9388199). {ECO:0000269|PubMed:11859088, ECO:0000269|PubMed:1569108, ECO:0000269|PubMed:19854834, ECO:0000269|PubMed:21276098, ECO:0000269|PubMed:7836365, ECO:0000269|PubMed:8446033, ECO:0000269|PubMed:9388199}. EcoCyc product frame: PD01520. EcoCyc synonyms: dec, ole, oleR, thdB. Genomic coordinates: 1234938-1235657. EcoCyc protein note: FadR, Fatty acid degradation Regulon , is a multifunctional dual regulator that exerts negative control over the fatty acid degradative regulon and acetate metabolism , whereas it is responsible for maximal expression of unsaturated fatty acid biosynthesis . FadR coordinately regulates fatty acid biosynthesis and fatty acid degradation at the level of transcription...

## Biological Role

Repressed by C0293 (gene.b4806).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8V6|protein.P0A8V6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[gene.b4806|gene.b4806]] `RegulonDB` `S` - regulator=C0293; target=fadR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003988,ECOCYC:EG10281,GeneID:948652`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1234938-1235657:+; feature_type=gene
