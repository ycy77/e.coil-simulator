---
entity_id: "gene.b0878"
entity_type: "gene"
name: "macA"
source_database: "NCBI RefSeq"
source_id: "gene-b0878"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0878"
  - "macA"
---

# macA

`gene.b0878`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0878`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

macA (gene.b0878) is a gene entity. It encodes macA (protein.P75830). Encoded protein function: FUNCTION: Part of the tripartite efflux system MacAB-TolC (PubMed:11544226, PubMed:17214741, PubMed:18955484, PubMed:21696464, PubMed:28504659, PubMed:40083904, PubMed:40461577). MacA stimulates the ATPase activity of MacB by promoting the closed ATP-bound state of MacB, increases the capacity of MacB to bind macrolides such as erythromycin, and provides a physical link between MacB and TolC (PubMed:17214741, PubMed:18955484, PubMed:21696464). When overexpressed, the system confers resistance against macrolides composed of 14- and 15-membered lactones but no or weak resistance against 16-membered ones; also confers resistance against bacitracin and colistin (PubMed:11544226, PubMed:18955484). In addition, MacA binds tightly rough-core lipopolysaccharide (R-LPS), suggesting that the system could also transport R-LPS or a similar glycolipid (PubMed:23974027). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). {ECO:0000269|PubMed:11544226, ECO:0000269|PubMed:17214741, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:21696464, ECO:0000269|PubMed:23974027, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577}...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75830|protein.P75830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=macA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002986,ECOCYC:G6461,GeneID:947322`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:919235-920350:+; feature_type=gene
