---
entity_id: "gene.b2221"
entity_type: "gene"
name: "atoD"
source_database: "NCBI RefSeq"
source_id: "gene-b2221"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2221"
  - "atoD"
---

# atoD

`gene.b2221`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2221`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoD (gene.b2221) is a gene entity. It encodes atoD (protein.P76458). Encoded protein function: FUNCTION: Coenzyme A transferase which is involved in short-chain fatty acid degradation and catalyzes the activation of short-chain fatty acids to their respective CoA thiolesters (PubMed:1103739, PubMed:3025185). During acetoacetate degradation, catalyzes the transfer of CoA from acetyl-CoA to acetoacetate by a mechanism involving a covalent enzyme-CoA compound as a reaction intermediate (PubMed:1103741). Utilizes a variety of short chain acyl-CoA and carboxylic acid substrates but exhibits maximal activity with normal and 3-keto substrates (PubMed:1103739). {ECO:0000269|PubMed:1103739, ECO:0000269|PubMed:1103741, ECO:0000269|PubMed:3025185}. EcoCyc product frame: ATOD-MONOMER. Genomic coordinates: 2323447-2324109. EcoCyc protein note: Based on sequence similarity, AtoD is predicted to be an acetate CoA-transferase . AtoD: "acetoacetate"

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

- `encodes` --> [[protein.P76458|protein.P76458]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q06065|protein.Q06065]] `RegulonDB` `C` - regulator=AtoC; target=atoD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007347,ECOCYC:EG11669,GeneID:947525`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2323447-2324109:+; feature_type=gene
