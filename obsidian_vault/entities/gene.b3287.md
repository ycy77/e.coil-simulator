---
entity_id: "gene.b3287"
entity_type: "gene"
name: "def"
source_database: "NCBI RefSeq"
source_id: "gene-b3287"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3287"
  - "def"
---

# def

`gene.b3287`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3287`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

def (gene.b3287) is a gene entity. It encodes def (protein.P0A6K3). Encoded protein function: FUNCTION: Removes the formyl group from the N-terminal Met of newly synthesized proteins (PubMed:7896716). Requires at least a dipeptide for an efficient rate of reaction. N-terminal L-methionine is a prerequisite for activity but the enzyme has broad specificity at other positions. {ECO:0000269|PubMed:7896716, ECO:0000269|PubMed:9610360, ECO:0000305|PubMed:8244948}. EcoCyc product frame: EG11440-MONOMER. EcoCyc synonyms: fms. Genomic coordinates: 3433690-3434199. EcoCyc protein note: Peptide deformylase (PDF) releases the formyl group from the amino terminal methionine residue of most nascent proteins . It interacts directly with the ribosome at the ribosomal exit tunnel and competes with EG10570-MONOMER (MAP) for the same site . PDF is essential in E. coli . A proteome-wide analysis of N termini in the presence and after depletion of PDF has been performed . The specific physiological function of the N-terminal formylated methionine residue (fMet) in proteins is uncertain. It was shown that N-terminal fMet can act as a co-translational degradation signal...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6K3|protein.P0A6K3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=def; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010779,ECOCYC:EG11440,GeneID:947780`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3433690-3434199:+; feature_type=gene
