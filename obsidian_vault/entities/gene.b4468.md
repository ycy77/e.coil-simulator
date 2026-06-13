---
entity_id: "gene.b4468"
entity_type: "gene"
name: "glcE"
source_database: "NCBI RefSeq"
source_id: "gene-b4468"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4468"
  - "glcE"
---

# glcE

`gene.b4468`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4468`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glcE (gene.b4468) is a gene entity. It encodes glcE (protein.P52073). Encoded protein function: FUNCTION: Component of a complex that catalyzes the oxidation of glycolate to glyoxylate (PubMed:4557653, PubMed:8606183). Is required for E.coli to grow on glycolate as a sole source of carbon (PubMed:8606183). Is also able to oxidize D-lactate ((R)-lactate) with a similar rate (PubMed:4557653). Does not link directly to O(2), and 2,6-dichloroindophenol (DCIP) and phenazine methosulfate (PMS) can act as artificial electron acceptors in vitro, but the physiological molecule that functions as a primary electron acceptor during glycolate oxidation is unknown (PubMed:4557653). {ECO:0000269|PubMed:4557653, ECO:0000269|PubMed:8606183}. EcoCyc product frame: G7544-MONOMER. EcoCyc synonyms: yghL, gox, b2978. Genomic coordinates: 3125470-3126522. EcoCyc protein note: GlcE is predicted to contain a flavin-binding domain . A glcE insertion mutant lacks glycolate dehydrogenase activity . GlcE: "glycolate utilization E"

## Biological Role

Repressed by arcA (protein.P0A9Q1), pdhR (protein.P0ACL9). Activated by glcC (protein.P0ACL5).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52073|protein.P52073]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACL5|protein.P0ACL5]] `RegulonDB` `S` - regulator=GlcC; target=glcE; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=glcE; function=-
- `represses` <-- [[protein.P0ACL9|protein.P0ACL9]] `RegulonDB` `S` - regulator=PdhR; target=glcE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0174098,ECOCYC:G7544,GeneID:2847718`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3125470-3126522:-; feature_type=gene
