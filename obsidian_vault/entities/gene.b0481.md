---
entity_id: "gene.b0481"
entity_type: "gene"
name: "ybaK"
source_database: "NCBI RefSeq"
source_id: "gene-b0481"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0481"
  - "ybaK"
---

# ybaK

`gene.b0481`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0481`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaK (gene.b0481) is a gene entity. It encodes ybaK (protein.P0AAR3). Encoded protein function: FUNCTION: Functions in trans to edit the amino acid from incorrectly charged Cys-tRNA(Pro) via a Cys-tRNA(Pro) deacylase activity. May compensate for the lack of Cys-tRNA(Pro) editing by ProRS. Is also able to deacylate Cys-tRNA(Cys), and displays weak deacylase activity in vitro against Gly-tRNA(Gly), as well as, at higher concentrations, some other correctly charged tRNAs. Unlike some of its orthologs it is not able to remove the amino acid moiety from incorrectly charged Ala-tRNA(Pro). {ECO:0000269|PubMed:15886196, ECO:0000269|PubMed:23185990}. EcoCyc product frame: EG12454-MONOMER. Genomic coordinates: 506603-507082. EcoCyc protein note: YbaK hydrolyzes both incorrectly charged Cys-tRNAPro and correctly charged Cys-tRNACys in vitro . YbaK does not appear to recognize specific tRNAs . However, YbaK interacts with PROS-CPLX ProRS in vivo, and this interaction enhances YbaK's Cys-tRNAPro deacylation activity. The interaction with ProRS appears to provide specificity for hydrolysis of mischarged Cys-tRNAPro . YbaK has similarity to the editing active site (INS domain) of ProRS, which is able to edit mischarged Ala-tRNAPro...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAR3|protein.P0AAR3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001670,ECOCYC:EG12454,GeneID:947083`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:506603-507082:-; feature_type=gene
