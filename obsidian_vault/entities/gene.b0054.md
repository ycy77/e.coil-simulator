---
entity_id: "gene.b0054"
entity_type: "gene"
name: "lptD"
source_database: "NCBI RefSeq"
source_id: "gene-b0054"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0054"
  - "lptD"
---

# lptD

`gene.b0054`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0054`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptD (gene.b0054) is a gene entity. It encodes lptD (protein.P31554). Encoded protein function: FUNCTION: Together with LptE, is involved in the assembly of lipopolysaccharide (LPS) at the surface of the outer membrane. Contributes to n-hexane resistance. {ECO:0000255|HAMAP-Rule:MF_01411, ECO:0000269|PubMed:12207697, ECO:0000269|PubMed:12724388, ECO:0000269|PubMed:16861298, ECO:0000269|PubMed:18424520, ECO:0000269|PubMed:20203010, ECO:0000269|PubMed:21339611, ECO:0000269|PubMed:2547691, ECO:0000269|PubMed:7811102}. EcoCyc product frame: EG11569-MONOMER. EcoCyc synonyms: yabG, ostA, imp. Genomic coordinates: 54755-57109. EcoCyc protein note: The LptD (lipopolysaccharide transport) protein is an essential outer membrane (OM) protein which, in complex with LptE, functions to assemble lipopolysaccharides at the surface of the OM . LptD exhibits β barrel-like characteristics, including a high incidence of aromatic amino acids (13.1%) . Sequence analyses via the algorithm by Shirmer and Cowan and Zhai suggest that LptD is rich in transmembrane β-strands. LptD contains an N-terminal periplasmic domain and a C-terminal β-barrel domain . LptD contains four cysteines which form non-consecutive disulfide bonds (Cys31=Cys724 and Cys173=Cys755) that bridge the N-terminal and C-terminal domains...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31554|protein.P31554]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lptD; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lptD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000183,ECOCYC:EG11569,GeneID:945011`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:54755-57109:-; feature_type=gene
