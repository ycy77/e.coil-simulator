---
entity_id: "gene.b3234"
entity_type: "gene"
name: "degQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3234"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3234"
  - "degQ"
---

# degQ

`gene.b3234`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3234`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

degQ (gene.b3234) is a gene entity. It encodes degQ (protein.P39099). Encoded protein function: FUNCTION: DegQ could degrade transiently denatured and unfolded proteins which accumulate in the periplasm following stress conditions. DegQ is efficient with Val-Xaa and Ile-Xaa peptide bonds, suggesting a preference for a beta-branched side chain amino acids. Only unfolded proteins devoid of disulfide bonds appear capable to be cleaved, thereby preventing non-specific proteolysis of folded proteins. DegQ can substitute for the periplasmic protease DegP. {ECO:0000269|PubMed:8576051, ECO:0000269|PubMed:8830688}. EcoCyc product frame: G7682-MONOMER. EcoCyc synonyms: hhoA. Genomic coordinates: 3380743-3382110.

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39099|protein.P39099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=degQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010609,ECOCYC:G7682,GeneID:947812`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3380743-3382110:+; feature_type=gene
