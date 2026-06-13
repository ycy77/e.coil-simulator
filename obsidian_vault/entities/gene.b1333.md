---
entity_id: "gene.b1333"
entity_type: "gene"
name: "uspE"
source_database: "NCBI RefSeq"
source_id: "gene-b1333"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1333"
  - "uspE"
---

# uspE

`gene.b1333`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1333`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uspE (gene.b1333) is a gene entity. It encodes uspE (protein.P0AAC0). Encoded protein function: FUNCTION: Required for resistance to DNA-damaging agents. {ECO:0000269|PubMed:11849540}. EcoCyc product frame: EG11246-MONOMER. EcoCyc synonyms: ydaA. Genomic coordinates: 1397672-1398622. EcoCyc protein note: UspC, UspD, and UspE play nonredundant and probably sequential roles in a pathway involved in resistance to UV irradiation . The UspE protein promotes cell motility at the expense of adhesion . UspE consists of two tandemly arranged Usp domains. A crystal structure of the protein from E. coli O157:H7, whose sequence is 100% identical to that of E. coli K-12 MG1655, has been solved at 3.2 Å resolution . The crystal structure shows an unidentified ligand bound in a hydrophobic pocket, and the protein was shown to bind Cd2+ . uspE deletion mutants shows decreased resistance to UV irradiation , lack flagella, are unable to aggregate , and show increased biofilm formation . Expression of uspE is induced in stationary phase and by a variety of stress conditions including oxidative stress and requires ppGpp . UspE: "universal stress protein E" Reviews:

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAC0|protein.P0AAC0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=uspE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004472,ECOCYC:EG11246,GeneID:945904`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1397672-1398622:-; feature_type=gene
