---
entity_id: "gene.b3374"
entity_type: "gene"
name: "frlD"
source_database: "NCBI RefSeq"
source_id: "gene-b3374"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3374"
  - "frlD"
---

# frlD

`gene.b3374`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3374`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

frlD (gene.b3374) is a gene entity. It encodes frlD (protein.P45543). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of fructoselysine to fructoselysine 6-phosphate (PubMed:12147680). Functions in a fructoselysine degradation pathway that allows E.coli to grow on fructoselysine or psicoselysine (PubMed:12147680, PubMed:14641112). To a much lesser extenst, is also able to phosphorylate psicoselysine (PubMed:14641112). {ECO:0000269|PubMed:12147680, ECO:0000269|PubMed:14641112}. EcoCyc product frame: G7726-MONOMER. EcoCyc synonyms: yhfQ. Genomic coordinates: 3503167-3503952. EcoCyc protein note: FrlD is a monomeric fructoselysine 6-kinase . FrlD is a member of the PfkB family of kinases and has similarity to the glucosamine-6-phosphate synthase isomerase domain . A structure model of FrlD was used to identify potential residues involved in substrate recognition, and site-directed mutants were tested for enzymatic activity. Most of the mutants showed significantly decreased activity. A Met220Leu mutant has decreased activity with fructoselysine, but increased activity with fructosevaline as the substrate . Fructoselysine 6-kinase activity is undetectable when cells are grown on glucose; stationary phase extracts of cells grown on fructoselysine or psicoselysine have a kinase activity of 100 nmol/min per mg of protein...

## Biological Role

Repressed by frlR (protein.P45544).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45543|protein.P45543]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P45544|protein.P45544]] `RegulonDB` `C` - regulator=FrlR; target=frlD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011029,ECOCYC:G7726,GeneID:947886`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3503167-3503952:+; feature_type=gene
