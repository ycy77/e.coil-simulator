---
entity_id: "gene.b0728"
entity_type: "gene"
name: "sucC"
source_database: "NCBI RefSeq"
source_id: "gene-b0728"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0728"
  - "sucC"
---

# sucC

`gene.b0728`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0728`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sucC (gene.b0728) is a gene entity. It encodes sucC (protein.P0A836). Encoded protein function: FUNCTION: Succinyl-CoA synthetase functions in the citric acid cycle (TCA), coupling the hydrolysis of succinyl-CoA to the synthesis of either ATP or GTP and thus represents the only step of substrate-level phosphorylation in the TCA. The beta subunit provides nucleotide specificity of the enzyme and binds the substrate succinate, while the binding sites for coenzyme A and phosphate are found in the alpha subunit. Can use either ATP or GTP, but prefers ATP. It can also function in the other direction for anabolic purposes, and this may be particularly important for providing succinyl-CoA during anaerobic growth when the oxidative route from 2-oxoglutarate is severely repressed. {ECO:0000255|HAMAP-Rule:MF_00558, ECO:0000269|PubMed:10353839}. EcoCyc product frame: SUCCCOASYN-BETA. Genomic coordinates: 763014-764180. EcoCyc protein note: SucC is the β subunit of succinyl-CoA synthetase. Trp45 and His50 are required for activity , while Cys47 and Cys325 are not essential. Single mutations of tryptophan residues W43, W76 and W248 have little effect on enzyme activity. W76 and W248 may be part of the CoA binding site . Glu197 is essential for phosphorylation and dephosphorylation of the active site His246 in the α subunit...

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), rpoS (protein.P13445).

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

- `encodes` --> [[protein.P0A836|protein.P0A836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sucC; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sucC; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucC; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sucC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=sucC; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sucC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002483,ECOCYC:EG10981,GeneID:945312`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:763014-764180:+; feature_type=gene
