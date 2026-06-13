---
entity_id: "gene.b3266"
entity_type: "gene"
name: "acrF"
source_database: "NCBI RefSeq"
source_id: "gene-b3266"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3266"
  - "acrF"
---

# acrF

`gene.b3266`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3266`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

acrF (gene.b3266) is a gene entity. It encodes acrF (protein.P24181). Encoded protein function: FUNCTION: Part of the tripartite efflux system AcrEF-TolC. Involved in the efflux of indole and organic solvents. {ECO:0000269|PubMed:10518736, ECO:0000269|PubMed:11274125}. EcoCyc product frame: ACRF-MONOMER. EcoCyc synonyms: envD. Genomic coordinates: 3415033-3418137. EcoCyc protein note: AcrF shares 77% amino acid sequence identity with ACRB-MONOMER "AcrB" of the AcrAB multidrug efflux system . acrEF is not expressed at significant levels in wild-type K-12 strains (see ) but is expressed upon integration of IS1 or IS2 into the upstream region of the operon or upon deletion of the PD00288 "H-NS repressor protein" ; when expressed AcrF functions in Escherichia coli as part of a drug efflux system with the AcrE membrane fusion protein and the TolC outer membrane protein (see CPLX0-2141 for more details). acrF is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . The acrF Keio collection mutant (BW25113 ΔacrF::kan) shows a significant increase in swimming motility .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24181|protein.P24181]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010724,ECOCYC:EG10267,GeneID:947768`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3415033-3418137:+; feature_type=gene
