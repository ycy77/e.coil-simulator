---
entity_id: "gene.b2660"
entity_type: "gene"
name: "lhgD"
source_database: "NCBI RefSeq"
source_id: "gene-b2660"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2660"
  - "lhgD"
---

# lhgD

`gene.b2660`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2660`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lhgD (gene.b2660) is a gene entity. It encodes lhgD (protein.P37339). Encoded protein function: FUNCTION: Catalyzes the dehydrogenation of L-2-hydroxyglutarate (L2HG) to alpha-ketoglutarate and couples to the respiratory chain by feeding electrons from the reaction into the membrane quinone pool. Functions in a L-lysine degradation pathway that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate. {ECO:0000269|PubMed:30498244}. EcoCyc product frame: EG12387-MONOMER. EcoCyc synonyms: ygaF, lhgO. Genomic coordinates: 2789982-2791250. EcoCyc protein note: L-2-hydroxyglutarate dehydrogenase (LhgD) is an electron transport chain-coupled dehydrogenase that feeds electrons from the reaction into the membrane quinone pool . LhgD contains an FAD cofactor which is not covalently attached, and whose reduction potential is relatively high at -25 mV . LhgD was initially thought to be an oxidase, i.e. using molecular oxygen for oxidation of L-2-hydroxyglutarate and producing hydrogen peroxide . LhgD is associated with the cytoplasmic membrane , and its activity is only found in the membrane fraction . lhgD is part of an operon whose expression is induced upon carbon starvation and in stationary phase . Review: LhgO: "L-2-hydroxyglutarate oxidase" LhgD: "L-2-hydroxyglutarate dehydrogenase

## Biological Role

Repressed by glaR (protein.P37338), nac (protein.Q47005). Activated by lrp (protein.P0ACJ0), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37339|protein.P37339]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=lhgD; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=lhgD; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=lhgD; function=-+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `C` - regulator=GlaR; target=lhgD; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=lhgD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0008756,ECOCYC:EG12387,GeneID:948069`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2789982-2791250:+; feature_type=gene
