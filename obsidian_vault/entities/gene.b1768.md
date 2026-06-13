---
entity_id: "gene.b1768"
entity_type: "gene"
name: "pncA"
source_database: "NCBI RefSeq"
source_id: "gene-b1768"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1768"
  - "pncA"
---

# pncA

`gene.b1768`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1768`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pncA (gene.b1768) is a gene entity. It encodes pncA (protein.P21369). Encoded protein function: FUNCTION: Catalyzes the deamidation of nicotinamide (NAM) into nicotinate (PubMed:4399474, PubMed:8726014). Likely functions in the cyclical salvage pathway for production of NAD from nicotinamide (PubMed:4399474). {ECO:0000269|PubMed:4399474, ECO:0000305|PubMed:8726014}.; FUNCTION: Is also able to hydrolyze the first-line antituberculous drug pyrazinamide (PZA) into pyrazinoic acid in vitro, but this reaction is not considered to be physiologically relevant. {ECO:0000305|PubMed:8726014}. EcoCyc product frame: NICOTINAMID-MONOMER. EcoCyc synonyms: nam, ydjB. Genomic coordinates: 1851887-1852528. EcoCyc protein note: pncA encodes a nicotinamidase (a member of the isochorismatase superfamily) that is active in the cyclical salvage pathway for production of NAD+ from nicotinamide (see pathway PYRIDNUCSAL-PWY). Homologs of PncA are found in other bacteria, archaea, and some eukaryotes, but not in vertebrates (reviewed in ). Early work established this salvage pathway in E. coli and a role for nicotinamidase . Exogenous nicotinamide appears to be passively taken up by E. coli . The pncA-encoded nicotinamidase also has pyrazinamidase activity...

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21369|protein.P21369]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005891,ECOCYC:EG11135,GeneID:946276`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1851887-1852528:+; feature_type=gene
