---
entity_id: "gene.b2314"
entity_type: "gene"
name: "dedD"
source_database: "NCBI RefSeq"
source_id: "gene-b2314"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2314"
  - "dedD"
---

# dedD

`gene.b2314`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2314`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dedD (gene.b2314) is a gene entity. It encodes dedD (protein.P09549). Encoded protein function: FUNCTION: Non-essential cell division protein that could be required for efficient cell constriction. {ECO:0000255|HAMAP-Rule:MF_02022, ECO:0000269|PubMed:19684127}. EcoCyc product frame: EG10218-MONOMER. Genomic coordinates: 2431022-2431684. EcoCyc protein note: DedD is a cell division protein; it contains a C-terminal SPOR domain which targets the protein to the septal ring . SPOR domains localize to the division site by preferentially binding to a-denuded-peptidoglycan denuded glycans, which are enriched in septal peptidoglycan . A model for the function of DedD, where both FtsN and DedD act in parallel to stimulate cell constriction, has been proposed . DedD interacts with both EG10748-MONOMER PBP1A and EG10605-MONOMER PBP1B and stimulates the glycosyltransferase activity of both enzymes . DedD is predicted to be a bitopic inner membrane protein ; residues within the transmembrane domain that are required for DedD function have been identified . A solution structure of the periplasmic portion of DedD shows a disordered region followed by a canonical SPOR domain . dedD mutant cells have a mild cell division defect, showing a chaining phenotype...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09549|protein.P09549]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0007643,ECOCYC:EG10218,GeneID:944971`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2431022-2431684:-; feature_type=gene
