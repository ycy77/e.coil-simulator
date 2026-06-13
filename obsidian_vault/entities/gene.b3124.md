---
entity_id: "gene.b3124"
entity_type: "gene"
name: "garK"
source_database: "NCBI RefSeq"
source_id: "gene-b3124"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3124"
  - "garK"
---

# garK

`gene.b3124`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3124`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

garK (gene.b3124) is a gene entity. It encodes garK (protein.P23524). Encoded protein function: FUNCTION: Catalyzes the transfer of the phosphate group from adenosine triphosphate (ATP) to (R)-glycerate to form (2R)-2-phosphoglycerate, an enzymatic step in (L)-glucarate/galactarate catabolic pathway. {ECO:0000269|PubMed:9772162}. EcoCyc product frame: GKI-MONOMER. EcoCyc synonyms: yhaD. Genomic coordinates: 3270625-3271770. EcoCyc protein note: Glycerate kinase I (GKI), encoded by garK, catalyzes the formation of 2-phosphoglycerate from D-glycerate . Recent in vivo metabolic assays also showed that the product is 2-phosphoglycerate . There are two glycerate kinases, known as GKI and GKII, in E. coli. GKI is more thermostable and has a broader pH optimum than GKII, and GKII activity is only induced by growth on glycolate . Glycerate kinase I is induced by growth on glycolate, glucarate, glycerate, and galactarate as the carbon source and is not sensitive to catabolite repression .

## Biological Role

Repressed by fur (protein.P0A9A9).

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

- `encodes` --> [[protein.P23524|protein.P23524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=garK; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010271,ECOCYC:EG11175,GeneID:947632`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3270625-3271770:-; feature_type=gene
