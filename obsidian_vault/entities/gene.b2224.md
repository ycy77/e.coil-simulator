---
entity_id: "gene.b2224"
entity_type: "gene"
name: "atoB"
source_database: "NCBI RefSeq"
source_id: "gene-b2224"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2224"
  - "atoB"
---

# atoB

`gene.b2224`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2224`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atoB (gene.b2224) is a gene entity. It encodes atoB (protein.P76461). Encoded protein function: Acetyl-CoA acetyltransferase (EC 2.3.1.9) (Acetoacetyl-CoA thiolase) EcoCyc product frame: ACETYL-COA-ACETYLTRANSFER-MONOMER. Genomic coordinates: 2326109-2327293. EcoCyc protein note: AtoB is one of two 3-ketoacyl-CoA thiolases in E. coli. While FADA-MONOMER FadA has broad substrate specificity, AtoB is strictly specific for acetoacetyl-CoA . Crystal structures of AtoB alone and in a complex with CoA have been solved; the structure can be described as a loosely interacting dimer of tight dimers . The gene for this study was cloned from E. coli BL21 (DE3), but the sequence is identical to that of the K-12 protein. AtoB expression is induced by growth on acetoacetate . AtoB is used for metabolic engineering of 1-butanol and medium-chain fuel production. AtoB: "acetoacetate"

## Biological Role

Activated by atoC (protein.Q06065).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)
- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00310` Lysine degradation (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco00900` Terpenoid backbone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76461|protein.P76461]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q06065|protein.Q06065]] `RegulonDB` `C` - regulator=AtoC; target=atoB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007355,ECOCYC:EG11672,GeneID:946727`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2326109-2327293:+; feature_type=gene
