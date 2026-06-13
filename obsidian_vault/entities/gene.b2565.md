---
entity_id: "gene.b2565"
entity_type: "gene"
name: "recO"
source_database: "NCBI RefSeq"
source_id: "gene-b2565"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2565"
  - "recO"
---

# recO

`gene.b2565`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2565`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

recO (gene.b2565) is a gene entity. It encodes recO (protein.P0A7H3). Encoded protein function: FUNCTION: Involved in DNA repair and RecF pathway recombination. EcoCyc product frame: EG10832-MONOMER. Genomic coordinates: 2701741-2702469. EcoCyc protein note: RecO is a recombination mediator protein in the RecF pathway for the homology-directed repair of post-replicative single-stranded DNA (ssDNA) gaps. recO mutations confer UV sensitivity and a Rec- (recombination deficient) phenotype in strains which lack the major RECBCD RecBC pathway of recombination; RecO, CPLX0-8596 RecF, and EG10834-MONOMER RecR belong to the same epistastic group . RecO, CPLX0-8596 RecF, and EG10834-MONOMER RecR are implicated in DNA daughter-strand gap repair and may function together as a complex . RecF, RecO, and RecR function at an early stage of recombinational repair and affect the interaction of EG10823-MONOMER RecA, CPLX0-8165 SSB, and ssDNA (also ). The RecF, RecO, and RecR proteins mediate the loading of RecA protein onto SSB-coated gapped DNA (and further ). Purified RecO binds non-specifically to both ssDNA and double-stranded DNA (dsDNA) and promotes the ATP-independent renaturation of two complementary ssDNA molecules...

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7H3|protein.P0A7H3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008438,ECOCYC:EG10832,GeneID:947038`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2701741-2702469:-; feature_type=gene
