---
entity_id: "gene.b4219"
entity_type: "gene"
name: "msrA"
source_database: "NCBI RefSeq"
source_id: "gene-b4219"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4219"
  - "msrA"
---

# msrA

`gene.b4219`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4219`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msrA (gene.b4219) is a gene entity. It encodes msrA (protein.P0A744). Encoded protein function: FUNCTION: Could have an important function as a repair enzyme for proteins that have been inactivated by oxidation. Catalyzes the reversible oxidation-reduction of methionine sulfoxide in proteins to methionine. {ECO:0000269|PubMed:10964927}. EcoCyc product frame: EG11433-MONOMER. EcoCyc synonyms: pms, pmsR. Genomic coordinates: 4441538-4442176. EcoCyc protein note: MsrA is one of several methionine sulfoxide reductases in E. coli . Methionine residues in proteins, including the N-terminal methionine, can be damaged by oxidation and can be repaired (reduced) by methionine sulfoxide reductases . Modification of chemically oxidized N-terminal methionines by formylation or acetylation significantly increases the catalytic efficiency of reduction by MsrA and EG12394-MONOMER MsrB in redox kinetic studies in vitro . MsrA and MsrB are also important for keeping EG10823-MONOMER RecA active under oxidative stress conditions . Conversely, the transcription factor G7924 HypT is activated by methionine oxidation and inactivated by MsrA/MsrB activity . MsrA appears to use RED-THIOREDOXIN-MONOMER thioredoxin 1 (Trx1) as the electron donor in vivo . Overexpressed RED-THIOREDOXIN2-MONOMER thioredoxin 2 (Trx2) can substitute for Trx1 . Cys51, Cys198, and Cys206 are involved in catalysis...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A744|protein.P0A744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=msrA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013804,ECOCYC:EG11433,GeneID:948734`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4441538-4442176:-; feature_type=gene
