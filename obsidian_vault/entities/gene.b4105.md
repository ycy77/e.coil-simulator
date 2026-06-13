---
entity_id: "gene.b4105"
entity_type: "gene"
name: "phnD"
source_database: "NCBI RefSeq"
source_id: "gene-b4105"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4105"
  - "phnD"
---

# phnD

`gene.b4105`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4105`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnD (gene.b4105) is a gene entity. It encodes phnD (protein.P16682). Encoded protein function: FUNCTION: Phosphonate binding protein that is part of the phosphonate uptake system. Exhibits high affinity for 2-aminoethylphosphonate, and somewhat less affinity to ethylphosphonate, methylphosphonate, phosphonoacetate and phenylphosphonate. {ECO:0000269|PubMed:16751609}. EcoCyc product frame: PHND-MONOMER. EcoCyc synonyms: phn, psiD. Genomic coordinates: 4323336-4324352. EcoCyc protein note: phnD encodes the periplasmic binding protein of an ATP-dependent phosphonate/phosphate uptake system that is considered to be cryptic in E. coli K-12. Purified PhnD binds the naturally occurring phosphonates, 2-aminoethylphosphonate, ethylphosphonate and methylphosphonate with high affinity (estimated Kds of d of 50µM) . PhnD has been used in the development of a phosphonate biosensor . psiD: phosphate starvation inducible

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16682|protein.P16682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnD; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013442,ECOCYC:EG10714,GeneID:948624`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4323336-4324352:-; feature_type=gene
