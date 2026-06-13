---
entity_id: "gene.b0729"
entity_type: "gene"
name: "sucD"
source_database: "NCBI RefSeq"
source_id: "gene-b0729"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0729"
  - "sucD"
---

# sucD

`gene.b0729`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0729`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sucD (gene.b0729) is a gene entity. It encodes sucD (protein.P0AGE9). Encoded protein function: FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The alpha subunit of the enzyme binds the substrates coenzyme A and phosphate, while succinate binding and nucleotide specificity is provided by the beta subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_01988, ECO:0000269|PubMed:10353839}. EcoCyc product frame: SUCCCOASYN-ALPHA. Genomic coordinates: 764180-765049. EcoCyc protein note: SucD is the α subunit of succinyl-CoA synthetase. His246 is the phosphorylated residue of the reaction intermediate. A His246Asp mutant can not autophosphorylate and has no catalytic activity . A His142 mutant is catalytically inactive for the overall reaction, but the enzyme can be phosphorylated with ATP and dephosphorylated with succinate . Glu208 is essential for phosphorylation and dephosphorylation of His246...

## Biological Role

Repressed by ryhB (gene.b4451), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco00660` C5-Branched dibasic acid metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGE9|protein.P0AGE9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sucD; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sucD; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucD; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sucD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sucD; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=sucD; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002485,ECOCYC:EG10982,GeneID:945314`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:764180-765049:+; feature_type=gene
