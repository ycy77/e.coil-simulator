---
entity_id: "gene.b2222"
entity_type: "gene"
name: "atoA"
source_database: "NCBI RefSeq"
source_id: "gene-b2222"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2222"
  - "atoA"
---

# atoA

`gene.b2222`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2222`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoA (gene.b2222) is a gene entity. It encodes atoA (protein.P76459). Encoded protein function: FUNCTION: Coenzyme A transferase which is involved in short-chain fatty acid degradation and catalyzes the activation of short-chain fatty acids to their respective CoA thiolesters (PubMed:1103739, PubMed:3025185). During acetoacetate degradation, catalyzes the transfer of CoA from acetyl-CoA to acetoacetate by a mechanism involving a covalent enzyme-CoA compound as a reaction intermediate (PubMed:1103741). Utilizes a variety of short chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates (PubMed:1103739). {ECO:0000269|PubMed:1103739, ECO:0000269|PubMed:1103741, ECO:0000269|PubMed:3025185}. EcoCyc product frame: ATOA-MONOMER. Genomic coordinates: 2324109-2324759. EcoCyc protein note: Based on sequence similarity, AtoA is predicted to be an acetate CoA-transferase . AtoA: "acetoacetate"

## Biological Role

Activated by atoC (protein.Q06065).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00627` Aminobenzoate degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76459|protein.P76459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q06065|protein.Q06065]] `RegulonDB` `C` - regulator=AtoC; target=atoA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007349,ECOCYC:EG11670,GeneID:946719`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2324109-2324759:+; feature_type=gene
