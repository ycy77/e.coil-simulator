---
entity_id: "gene.b0114"
entity_type: "gene"
name: "aceE"
source_database: "NCBI RefSeq"
source_id: "gene-b0114"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0114"
  - "aceE"
---

# aceE

`gene.b0114`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0114`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aceE (gene.b0114) is a gene entity. It encodes aceE (protein.P0AFG8). Encoded protein function: FUNCTION: Component of the pyruvate dehydrogenase (PDH) complex, that catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2). EcoCyc product frame: E1P-MONOMER. Genomic coordinates: 123017-125680.

## Biological Role

Repressed by fnr (protein.P0A9E5), pdhR (protein.P0ACL9), cra (protein.P0ACP1), btsR (protein.P0AFT5). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AFG8|protein.P0AFG8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=aceE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aceE; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=aceE; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aceE; function=-+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=aceE; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=aceE; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=aceE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000397,ECOCYC:EG10024,GeneID:944834`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:123017-125680:+; feature_type=gene
