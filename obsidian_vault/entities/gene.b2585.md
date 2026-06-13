---
entity_id: "gene.b2585"
entity_type: "gene"
name: "pssA"
source_database: "NCBI RefSeq"
source_id: "gene-b2585"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2585"
  - "pssA"
---

# pssA

`gene.b2585`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2585`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pssA (gene.b2585) is a gene entity. It encodes pssA (protein.P23830). Encoded protein function: FUNCTION: Catalyzes the conversion of cytidine diphosphate diacylglycerol (CDP-DG) and L-serine into phosphatidylserine (PubMed:39693441, PubMed:8824831). Essential for biosynthesis of phosphatidylethanolamine, one of the major membrane phospholipids (PubMed:39693441, PubMed:8824831). Phosphatidylserine is later converted into phosphatidylethanolamine via the action of phosphatidylserine decarboxylase psd (PubMed:39693441, PubMed:8824831). Associates with the bacterial membrane for its role, which depends on the levels of anionic phospholipids in the membrane (PubMed:39693441, PubMed:8824831). {ECO:0000269|PubMed:39693441, ECO:0000269|PubMed:8824831}. EcoCyc product frame: PHOSPHASERSYN-MONOMER. EcoCyc synonyms: pss. Genomic coordinates: 2722727-2724082.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23830|protein.P23830]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pssA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008510,ECOCYC:EG10781,GeneID:947059`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2722727-2724082:+; feature_type=gene
