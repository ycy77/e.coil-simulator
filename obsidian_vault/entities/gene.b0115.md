---
entity_id: "gene.b0115"
entity_type: "gene"
name: "aceF"
source_database: "NCBI RefSeq"
source_id: "gene-b0115"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0115"
  - "aceF"
---

# aceF

`gene.b0115`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0115`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aceF (gene.b0115) is a gene entity. It encodes aceF (protein.P06959). Encoded protein function: FUNCTION: The pyruvate dehydrogenase complex catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2). It contains multiple copies of three enzymatic components: pyruvate dehydrogenase (E1), dihydrolipoamide acetyltransferase (E2) and lipoamide dehydrogenase (E3). EcoCyc product frame: ACEF-DIHYDROLIPOATE. Genomic coordinates: 125695-127587. EcoCyc protein note: AceF, the "E2" or "core" component of the pyruvate dehydrogenase multienzyme complex, assembles into a 24-subunit cube . The E1 dimers of the pyruvate dehydrogenase multienzyme complex catalyze acetylation of the lipoate moieties that are attached to the E2 subunits . The E2 subunits (AceF) also exhibit transacetylation . The structure of the pyruvate dehydrogenase multienzyme complex and the spatial distribution of the E2 lipoyl moieties have been studied by scanning transmission electron microscopy . AceF is a soluble cytoplasmic protein that contains an acidic N-terminal lipoyl domain with three roughly 100-residue repeats, each with a lipoyl modification motif and an alanine- and proline-rich segment . A single lipoyl domain suffices with respect to enzyme activity and protein function . The lipoyl domains appear to function independently of each other...

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

- `encodes` --> [[protein.P06959|protein.P06959]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=aceF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aceF; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=aceF; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=aceF; function=-+
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `C` - regulator=PdhR; target=aceF; function=-
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=aceF; function=-
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=aceF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000400,ECOCYC:EG10025,GeneID:944794`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:125695-127587:+; feature_type=gene
