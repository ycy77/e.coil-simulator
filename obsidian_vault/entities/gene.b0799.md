---
entity_id: "gene.b0799"
entity_type: "gene"
name: "dinG"
source_database: "NCBI RefSeq"
source_id: "gene-b0799"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0799"
  - "dinG"
---

# dinG

`gene.b0799`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0799`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dinG (gene.b0799) is a gene entity. It encodes dinG (protein.P27296). Encoded protein function: FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase (PubMed:12748189, PubMed:17416902, PubMed:25059658, PubMed:37537265). Can also unwind DNA:RNA hybrid duplexes (PubMed:17416902). Is active on D-loops, R-loops, and on forked structures (PubMed:17416902, PubMed:37537265). Unwinds G-quadruplex DNA in a 5'-3' direction; unwinding efficiency differs on different substrates (PubMed:25059658, PubMed:37537265). Does not appear to unwind replication forks or Holliday junctions (PubMed:25059658). Translocates on single-stranded (ss)DNA with a 5'-3' polarity (PubMed:25059658). In vitro at high concentrations also unwinds in a 3'-5' direction (PubMed:25059658). May be involved in recombinational DNA repair and the resumption of replication after DNA damage (PubMed:17416902). The [4Fe-4S] cluster is redox active at cellular potentials and is involved in DNA-mediated charge-transport signaling between DNA repair proteins from distinct pathways (PubMed:24738733). DinG cooperates at long-range with endonuclease III, a base excision repair enzyme, using DNA charge transport to redistribute to regions of DNA damage (PubMed:24738733). Binds 10-11 nucleotides of ssDNA in a positively-charged groove across the helicase domains (PubMed:30520735)...

## Biological Role

Repressed by lexA (protein.P0A7C2).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27296|protein.P27296]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=dinG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002732,ECOCYC:EG11357,GeneID:945431`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:833070-835220:+; feature_type=gene
