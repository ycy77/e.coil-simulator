---
entity_id: "gene.b3471"
entity_type: "gene"
name: "yhhQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3471"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3471"
  - "yhhQ"
---

# yhhQ

`gene.b3471`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3471`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhhQ (gene.b3471) is a gene entity. It encodes yhhQ (protein.P37619). Encoded protein function: FUNCTION: Involved in the import of queuosine (Q) precursors, required for Q precursor salvage. Transports 7-cyano-7-deazaguanine (preQ(0)) and 7-aminomethyl-7-deazaguanine (preQ(1)), with a preference for preQ(0). {ECO:0000269|PubMed:28208705}. EcoCyc product frame: EG12217-MONOMER. Genomic coordinates: 3609217-3609882. EcoCyc protein note: YhhQ is an inner membrane protein implicated in the uptake of queuosine (Q) precursors - 7-cyano-7-deazaguanine (7-CYANO-7-DEAZAGUANINE "preQ0") and 7-aminomethyl-7-deazaguanine (7-AMINOMETHYL-7-DEAZAGUANINE "preQ1") - for Q salvage. Q-modified tRNA is absent in ΔG7431 "queD" and ΔqueD ΔyhhQ strains grown in minimal media with glycerol; Q-modified tRNA is detected when a ΔqueD strain is grown in minimal media plus 10 nM preQ0 or preQ1 but is absent when a ΔqueD ΔyhhQ strain is grown under these conditions . yhhQ expressed from a plasmid restores the presence of Q-modified tRNA in a ΔqueD ΔyhhQ strain . Cleavage of yhhQ mRNA by CPLX0-3281 appears to accelerate its degradation ; a 5' UTR antisense RNA might be required to show cleavage in vitro . A class I type III pre-Q1 (preQ1-IIII)-sensing riboswitch in the 5' leader region of yhhQ mRNA is implicated in translation control...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37619|protein.P37619]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yhhQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011340,ECOCYC:EG12217,GeneID:947984`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3609217-3609882:+; feature_type=gene
