---
entity_id: "gene.b0778"
entity_type: "gene"
name: "bioD"
source_database: "NCBI RefSeq"
source_id: "gene-b0778"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0778"
  - "bioD"
---

# bioD

`gene.b0778`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0778`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

bioD (gene.b0778) is a gene entity. It encodes bioD1 (protein.P13000). Encoded protein function: FUNCTION: Catalyzes a mechanistically unusual reaction, the ATP-dependent insertion of CO2 between the N7 and N8 nitrogen atoms of 7,8-diaminopelargonic acid (DAPA, also called 7,8-diammoniononanoate) to form a ureido ring. Only CTP can partially replace ATP while diaminobiotin is only 37% as effective as 7,8-diaminopelargonic acid (PubMed:4892372, PubMed:4921568). In another study both CTP and GTP (but not ITP, TTP or UTP) can partially replace ATP (PubMed:25801336). {ECO:0000269|PubMed:25801336, ECO:0000269|PubMed:4892372, ECO:0000269|PubMed:4921568}. EcoCyc product frame: DETHIOBIOTIN-SYN-MONOMER. Genomic coordinates: 812270-812947.

## Biological Role

Repressed by birA (protein.P06709).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P13000|protein.P13000]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P06709|protein.P06709]] `RegulonDB` `S` - regulator=BirA; target=bioD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002650,ECOCYC:EG10120,GeneID:945387`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:812270-812947:+; feature_type=gene
