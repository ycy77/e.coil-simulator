---
entity_id: "gene.b0333"
entity_type: "gene"
name: "prpC"
source_database: "NCBI RefSeq"
source_id: "gene-b0333"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0333"
  - "prpC"
---

# prpC

`gene.b0333`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0333`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prpC (gene.b0333) is a gene entity. It encodes prpC (protein.P31660). Encoded protein function: FUNCTION: Involved in the catabolism of short chain fatty acids (SCFA) via the tricarboxylic acid (TCA)(acetyl degradation route) and via the 2-methylcitrate cycle I (propionate degradation route). Catalyzes the Claisen condensation of propionyl-CoA and oxaloacetate (OAA) to yield 2-methylcitrate (2-MC) and CoA. Also catalyzes the condensation of oxaloacetate with acetyl-CoA to yield citrate but with a lower specificity. {ECO:0000269|PubMed:12473114, ECO:0000269|PubMed:28956599, ECO:0000269|PubMed:8508809, ECO:0000269|PubMed:9325432, ECO:0000269|PubMed:9579066}. EcoCyc product frame: G6198-MONOMER. EcoCyc synonyms: yzzD, yahS. Genomic coordinates: 350012-351181. EcoCyc protein note: 2-Methylcitrate synthase (PrpC) catalyzes the Claisen condensation of propionyl-CoA with oxaloacetate, a reaction in propionate catabolism via the methylcitrate cycle . Production of the enzyme is induced by growth on propionate, but not acetate or glucose . Expression of prpBCDE is regulated by PrpR and catabolite repression and is downregulated in the presence of a variety of sugars . A revertant of a gltA mutant strain produces an enzyme with citrate synthase activity that was later found to be identical to PrpC . The mutation causing the revertant phenotype is unknown...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31660|protein.P31660]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=prpC; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=prpC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001148,ECOCYC:G6198,GeneID:947528`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:350012-351181:+; feature_type=gene
