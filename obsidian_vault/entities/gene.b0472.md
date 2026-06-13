---
entity_id: "gene.b0472"
entity_type: "gene"
name: "recR"
source_database: "NCBI RefSeq"
source_id: "gene-b0472"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0472"
  - "recR"
---

# recR

`gene.b0472`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0472`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recR (gene.b0472) is a gene entity. It encodes recR (protein.P0A7H6). Encoded protein function: FUNCTION: May play a role in DNA repair. It seems to be involved in an RecBC-independent recombinational process of DNA repair. It may act with RecF and RecO. EcoCyc product frame: EG10834-MONOMER. Genomic coordinates: 494405-495010. EcoCyc protein note: RecR is a recombination mediator protein in the RecF pathway for the homology-directed repair of post-replicative single-stranded DNA gaps. recR mutations confer UV sensitivity and a Rec- (recombination deficient) phenotype in strains which lack the major RECBCD RecBC pathway of recombination; RecR, CPLX0-8596 RecF, and EG10832-MONOMER RecO beong to the same epistastic group (also ). RecR, CPLX0-8596 RecF, and EG10832-MONOMER RecO are implicated in DNA daughter-strand gap repair and may function together as a complex . RecF, RecO, and RecR function at an early stage of recombinational repair and affect the interaction of EG10823-MONOMER RecA, CPLX0-8165 SSB, and ssDNA (also ). The RecF, RecO, and RecR proteins mediate the loading of RecA protein onto SSB-coated gapped DNA (and further ). RecFOR and RecOR may define two distinct RecA loading pathways in TAX-562...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7H6|protein.P0A7H6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=recR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001638,ECOCYC:EG10834,GeneID:945100`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:494405-495010:+; feature_type=gene
