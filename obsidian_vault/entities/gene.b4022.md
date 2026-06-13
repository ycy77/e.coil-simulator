---
entity_id: "gene.b4022"
entity_type: "gene"
name: "rluF"
source_database: "NCBI RefSeq"
source_id: "gene-b4022"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4022"
  - "rluF"
---

# rluF

`gene.b4022`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4022`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rluF (gene.b4022) is a gene entity. It encodes rluF (protein.P32684). Encoded protein function: FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-2604 in 23S ribosomal RNA and from uracil-35 in the anticodon of tRNA(Tyr) (PubMed:11720289, PubMed:27551044). Can, to a small extent, also react with uracil-2605 (PubMed:11720289). {ECO:0000269|PubMed:11720289, ECO:0000269|PubMed:27551044}. EcoCyc product frame: EG11921-MONOMER. EcoCyc synonyms: yjbC. Genomic coordinates: 4230354-4231226. EcoCyc protein note: RluF is the pseudouridine synthase that catalyzes formation of pseudouridine at position 2604 in 23S rRNA and position 35 within the anticodon of TYR-tRNAs tRNATyr . RluF belongs to the RsuA family of RNA pseudouridine synthases . Pseudouridine modification of tRNATyr appears to increase the translation efficiency of mRNAs rich in Tyr codons . Neither an rluF null mutant nor an rluB rluF double null mutant exhibit an obvious growth defect. The conserved active site residue Asp107 is essential for activity . The crystal structure of RluF bound to the 23S rRNA stem-loop it modifies has been solved at 3.0 Å resolution. The structure shows a conserved binding groove for the RNA stem-loop in the catalytic domain...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32684|protein.P32684]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013150,ECOCYC:EG11921,GeneID:948519`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4230354-4231226:+; feature_type=gene
