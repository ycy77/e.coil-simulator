---
entity_id: "gene.b0197"
entity_type: "gene"
name: "metQ"
source_database: "NCBI RefSeq"
source_id: "gene-b0197"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0197"
  - "metQ"
---

# metQ

`gene.b0197`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0197`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metQ (gene.b0197) is a gene entity. It encodes metQ (protein.P28635). Encoded protein function: FUNCTION: This protein is a component of a D-methionine permease, a binding protein-dependent, ATP-driven transport system. {ECO:0000269|PubMed:12169620}. EcoCyc product frame: METQ-MONOMER. EcoCyc synonyms: metD, yaeC. Genomic coordinates: 220113-220928. EcoCyc protein note: MetQ is the substrate binding protein of a high affinity methionine uptake system. MetQ has a predicted signal sequence and a lipoprotein lipid attachment site . MetQ is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). A MetQ mutant (N229A)* with significantly reduced affinity for D-methionine and D-selenomethionine supports the uptake of D-selenomethionine at an increased rate compared to the wild type; a crystal structure of the transporter complex containing the apoMetQ variant (MetNIQN229A) indicates the presence of a substrate access channel through the binding protein to the translocation pathway and suggests that the MetQ binding protein may support the uptake of low-affinity substrates through a non-canonical mechanism whereby substrate binding occurs directly to the MetNIQ complex . * the MetQ mutant characterized by was a soluble variant lacking the lipoprotein signal peptide

## Biological Role

Activated by yjiE (protein.P39376).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28635|protein.P28635]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P39376|protein.P39376]] `RegulonDB` `S` - regulator=HypT; target=metQ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000666,ECOCYC:EG11504,GeneID:944893`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:220113-220928:-; feature_type=gene
