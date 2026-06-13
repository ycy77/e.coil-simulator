---
entity_id: "gene.b0514"
entity_type: "gene"
name: "glxK"
source_database: "NCBI RefSeq"
source_id: "gene-b0514"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0514"
  - "glxK"
---

# glxK

`gene.b0514`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0514`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glxK (gene.b0514) is a gene entity. It encodes glxK (protein.P77364). Encoded protein function: Glycerate 3-kinase (EC 2.7.1.31) (D-Glycerate-3-kinase) (Glycerate kinase 2) (GK2) EcoCyc product frame: GLY3KIN-MONOMER. EcoCyc synonyms: glxB5, ybbZ. Genomic coordinates: 541888-543033. EcoCyc protein note: Glycerate kinase II (GKII), encoded by glxK, catalyzes the phosphorylation of D-glycerate. The product of the reaction (with the enzyme from E. coli Crooke's strain) was initially identified as 3-phosphoglycerate . More recent biochemical and in vivo metabolic assays showed that the product is in fact 2-phosphoglycerate . There are two glycerate kinases, known as GKI and GKII, in E. coli. GKII is less thermostable and has a narrower pH optimum than GKI . Glycerate kinase II is induced by growth on glycolate as the carbon source . A glxK mutant is unable to utilize glyoxylate . In contrast, state that deletion of glxK does not result in a growth defect with glycolate, glyoxylate or glycerate as sole carbon sources, although the data are not shown. GlxK was shown to allosterically activate CPLX-64, an enzyme that otherwise has low affinity for its substrate, in the presence of GLYOX. Activation by GlxK leads to increased affinity for allantoin...

## Biological Role

Repressed by allR (protein.P0ACN4), nac (protein.Q47005).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77364|protein.P77364]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=glxK; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=glxK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001773,ECOCYC:G6283,GeneID:945129`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:541888-543033:+; feature_type=gene
