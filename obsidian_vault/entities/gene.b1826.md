---
entity_id: "gene.b1826"
entity_type: "gene"
name: "mgrB"
source_database: "NCBI RefSeq"
source_id: "gene-b1826"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1826"
  - "mgrB"
---

# mgrB

`gene.b1826`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1826`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgrB (gene.b1826) is a gene entity. It encodes mgrB (protein.P64512). Encoded protein function: FUNCTION: Represses PhoP/PhoQ signaling, possibly by binding to the periplasmic domain of PhoQ, altering its activity and that of downstream effector PhoP. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway; the 2 periplasmic Cys residues of MgrB are required for its action on PhoQ, and thus PhoP. {ECO:0000269|PubMed:20041203, ECO:0000269|PubMed:22267510}. EcoCyc product frame: G7002-MONOMER. EcoCyc synonyms: yobG. Genomic coordinates: 1908623-1908766. EcoCyc protein note: MgrB is a small, inner membrane protein that mediates a negative feedback loop in the PhoQP two component system. MgrB negatively regulates the activity of the PHOQ-MONOMER . PhoQ is involved in sensing external magnesium concentrations and then activating PHOP-MONOMER. Thus, by negatively regulating PhoQ activity, MgrB downregulates PhoP activity and the transcription of a wide range of genes whose expression is controlled by PhoP regulation. This set of genes includes mgrB itself...

## Biological Role

Activated by phoP (protein.P23836).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64512|protein.P64512]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=mgrB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006078,ECOCYC:G7002,GeneID:946351`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1908623-1908766:-; feature_type=gene
