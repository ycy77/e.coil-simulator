---
entity_id: "gene.b3885"
entity_type: "gene"
name: "yihX"
source_database: "NCBI RefSeq"
source_id: "gene-b3885"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3885"
  - "yihX"
---

# yihX

`gene.b3885`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3885`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yihX (gene.b3885) is a gene entity. It encodes yihX (protein.P0A8Y3). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of alpha-D-glucose 1-phosphate (Glc1P) and, to a lesser extent, of other sugar phosphates (PubMed:16990279, PubMed:25484615). Has no activity with the beta form of Glc1P. In addition, YihX has significant phosphatase activity against pyridoxal phosphate (PLP) and low beta-phosphoglucomutase activity (PubMed:16990279). {ECO:0000269|PubMed:16990279, ECO:0000269|PubMed:25484615}. EcoCyc product frame: EG11850-MONOMER. Genomic coordinates: 4075553-4076152. EcoCyc protein note: YihX is a phosphatase belonging to the superfamily of haloacid dehalogenase (HAD)-like hydrolases. It selectively hydrolyzes α-D-glucose-1-phosphate and has no activity with the β form or D-glucose-6-phosphate . In addition, YihX has significant phosphatase activity against pyridoxal phosphate and low β-phosphoglucomutase activity . The phosphatase activity of YihX was first discovered in a high-throughput screen of purified proteins . No measurable sorbitol-6-phosphate phosphatase activity was detected .

## Biological Role

Activated by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A8Y3|protein.P0A8Y3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=yihX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012686,ECOCYC:EG11850,GeneID:948380`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4075553-4076152:+; feature_type=gene
