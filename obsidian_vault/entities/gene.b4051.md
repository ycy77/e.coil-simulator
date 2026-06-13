---
entity_id: "gene.b4051"
entity_type: "gene"
name: "qorA"
source_database: "NCBI RefSeq"
source_id: "gene-b4051"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4051"
  - "qorA"
---

# qorA

`gene.b4051`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4051`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

qorA (gene.b4051) is a gene entity. It encodes qorA (protein.P28304). Encoded protein function: Quinone oxidoreductase 1 (EC 1.6.5.5) (NADPH:quinone reductase 1) (Zeta-crystallin homolog protein) EcoCyc product frame: QOR-MONOMER. EcoCyc synonyms: hzc, hcz, qor. Genomic coordinates: 4263248-4264231. EcoCyc protein note: QorA is a putative NADPH-dependent quinone oxidoreductase that is structurally similar to Thermoplasma acidophilum glucose dehydrogenase and horse liver alcohol dehydrogenase . The enzyme has not been biochemically characterized. A crystal structure of the enzyme has been solved at 2.2 Å resolution . QorA may have physiologically relevant G7276 yffO mRNA binding activity .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28304|protein.P28304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0013262,ECOCYC:EG11492,GeneID:948556`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4263248-4264231:-; feature_type=gene
