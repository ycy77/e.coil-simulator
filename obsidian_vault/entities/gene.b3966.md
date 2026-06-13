---
entity_id: "gene.b3966"
entity_type: "gene"
name: "btuB"
source_database: "NCBI RefSeq"
source_id: "gene-b3966"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3966"
  - "btuB"
---

# btuB

`gene.b3966`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3966`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btuB (gene.b3966) is a gene entity. It encodes btuB (protein.P06129). Encoded protein function: FUNCTION: Involved in the active translocation of vitamin B12 (cyanocobalamin) across the outer membrane to the periplasmic space (PubMed:4579869). It derives its energy for transport by interacting with the trans-periplasmic membrane protein TonB. {ECO:0000255|HAMAP-Rule:MF_01531, ECO:0000269|PubMed:10485884, ECO:0000269|PubMed:2687240, ECO:0000269|PubMed:2982793, ECO:0000269|PubMed:4579869}.; FUNCTION: (Microbial infection) Acts as a receptor for bacteriophages BF23 and C1, and for A and E colicins (PubMed:14528295, PubMed:4579869). Cyanocobalamin (CN-B12) in solid medium protects against colicins E1 and E3 (PubMed:4579869). Does not act as the translocon for colicin E3 (ColE3). The translocon is OmpF; trimeric complexes with ColE3, BtuB and OmpF can be cross-linked and immunoprecipitated (PubMed:18636093). {ECO:0000269|PubMed:14528295, ECO:0000269|PubMed:18636093, ECO:0000269|PubMed:4579869}. EcoCyc product frame: EG10126-MONOMER. EcoCyc synonyms: bfe, cer. Genomic coordinates: 4163639-4165483. EcoCyc protein note: btuB mutants, defective in cobalamin (vitamin B12) transport/binding and resistant to E colicins and phage BF23, were originally isolated from a methionine-coenzyme B12 auxotroph (K-12 strain KBT001; see )...

## Biological Role

Repressed by gadX (protein.P37639). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06129|protein.P06129]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=btuB; function=+
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=btuB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012987,ECOCYC:EG10126,GeneID:948468`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4163639-4165483:+; feature_type=gene
