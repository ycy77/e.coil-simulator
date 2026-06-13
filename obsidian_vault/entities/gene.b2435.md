---
entity_id: "gene.b2435"
entity_type: "gene"
name: "amiA"
source_database: "NCBI RefSeq"
source_id: "gene-b2435"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2435"
  - "amiA"
---

# amiA

`gene.b2435`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2435`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

amiA (gene.b2435) is a gene entity. It encodes amiA (protein.P36548). Encoded protein function: FUNCTION: Cell-wall hydrolase involved in septum cleavage during cell division. Can also act as powerful autolysin in the presence of murein synthesis inhibitors. {ECO:0000269|PubMed:11454209, ECO:0000269|PubMed:18390656}. EcoCyc product frame: NACMURLALAAMI1-MONOMER. EcoCyc synonyms: yfeE. Genomic coordinates: 2552352-2553221. EcoCyc protein note: amiA encodes a protein with N-acetylmuramoyl-L-alanine amidase activity. AmiA cleaves the N-acetylmuramoyl → L-alanine bond present in bacterial peptidoglycan; when incubated with isolated murein sacculi, AmiA action results in the appearance of Ala-Glu-A2pm-Ala tetrapeptide and Ala-Glu-A2pm tripeptide . Murein amidase activity produces stemless or a-denuded-peptidoglycan denuded glycans. AmiA is a zinc dependent enzyme . AmiA requires at least a tetrasaccharide as substrate; AmiA does not cleave the peptide from C6 "lipid II" amiA deletion mutants show increased chaining (5-10% chains, 3-4 cells per chain). AmiA, along with NACMURLALAAMI2-MONOMER "AmiB" and G7458-MONOMER "AmiC" plays a role in septum cleavage during cell division; a triple amiA amiB amiC deletion mutant shows 90-100% chains with up to 24 cells per chain; septa in the triple mutant are formed but not cleaved...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36548|protein.P36548]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=amiA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008032,ECOCYC:EG11823,GeneID:946916`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2552352-2553221:+; feature_type=gene
