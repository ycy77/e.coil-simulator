---
entity_id: "gene.b1051"
entity_type: "gene"
name: "msyB"
source_database: "NCBI RefSeq"
source_id: "gene-b1051"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1051"
  - "msyB"
---

# msyB

`gene.b1051`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1051`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

msyB (gene.b1051) is a gene entity. It encodes msyB (protein.P25738). Encoded protein function: FUNCTION: Could participate in the normal pathway of protein export. EcoCyc product frame: EG11338-MONOMER. Genomic coordinates: 1113807-1114181. EcoCyc protein note: The msyB gene is a multicopy suppressor of heat sensitivity of a secY24 mutant . NMR resonance assignments for MsyB are available . MsyB is rich in acidic amino acids, which may cause abnormal migration in SDS gels . As a fusion partner for overexpression of heterologous proteins in E. coli, MsyB improves solubility . MsyB: "multicopy suppressor of secY24 B"

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25738|protein.P25738]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=msyB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003567,ECOCYC:EG11338,GeneID:945612`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1113807-1114181:-; feature_type=gene
