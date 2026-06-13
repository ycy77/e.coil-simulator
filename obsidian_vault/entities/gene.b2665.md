---
entity_id: "gene.b2665"
entity_type: "gene"
name: "kbp"
source_database: "NCBI RefSeq"
source_id: "gene-b2665"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2665"
  - "kbp"
---

# kbp

`gene.b2665`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2665`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kbp (gene.b2665) is a gene entity. It encodes kbp (protein.P0ADE6). Encoded protein function: FUNCTION: Highly specific potassium binding protein that is required for normal growth in the presence of high levels of external K(+). May act as a sensor of cytoplasmic K(+) concentration. Binds a single K(+) ion, which induces a large conformational change. Can also bind the larger alkali metal ions Rb(+) and Cs(+), and NH(4)(+) (PubMed:27112601). May be involved in the regulation of peptidoglycan cross-linking (PubMed:25422305). {ECO:0000269|PubMed:25422305, ECO:0000269|PubMed:27112601}. EcoCyc product frame: G7395-MONOMER. EcoCyc synonyms: yzzM, ygaU. Genomic coordinates: 2796337-2796786. EcoCyc protein note: Kbp is a potassium-binding protein that is required for normal growth in the presence of high external concentrations of potassium and under salt-induced osmotic stress conditions. Upon association with K+, Kbp undergoes a conformational change that results in compaction of the tertiary structure . Kbp contains a BON domain that is thought to function as a membrane-binding domain, and a LysM domain that is associated with bacterial cell wall degradation . The BON domain is required for K+ binding, while the LysM domain appears to stabilize the K+-bound complex . A solution structure of K+-bound Kbp has been determined...

## Biological Role

Activated by cpxR (protein.P0AE88).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADE6|protein.P0ADE6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=kbp; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008767,ECOCYC:G7395,GeneID:947144`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2796337-2796786:-; feature_type=gene
