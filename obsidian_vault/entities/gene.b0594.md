---
entity_id: "gene.b0594"
entity_type: "gene"
name: "entE"
source_database: "NCBI RefSeq"
source_id: "gene-b0594"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0594"
  - "entE"
---

# entE

`gene.b0594`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0594`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

entE (gene.b0594) is a gene entity. It encodes entE (protein.P10378). Encoded protein function: FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (enterochelin), which is a macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine. The serine trilactone serves as a scaffolding for the three catechol functionalities that provide hexadentate coordination for the tightly ligated iron(2+) atoms. EntE processes via a two-step adenylation-ligation reaction (bi-uni-uni-bi ping-pong mechanism). First, it catalyzes the activation of the carboxylate group of 2,3-dihydroxy-benzoate (DHB), via a reversible ATP-dependent pyrophosphate exchange reactions to yield the acyladenylate intermediate 2,3-dihydroxybenzoyl-AMP. It can also transfer AMP to salicylate, 2,4-dihydroxybenzoate, gentisate and 2,3,4-trihydroxybenzoate. In the second step, DHB is transferred from 2,3-dihydroxybenzoyl-AMP onto the phosphopantetheinylated EntB (holo-EntB) to form DHB-holo-EntB. Then this product will serve in the formation of the amide bond between 2,3-dihydroxybenzoate (DHB) and L-serine. It can also transfer adenylated salicylate to holo-EntB...

## Biological Role

Repressed by fur (protein.P0A9A9).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10378|protein.P10378]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=entE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002049,ECOCYC:EG10263,GeneID:947426`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:626070-627680:+; feature_type=gene
