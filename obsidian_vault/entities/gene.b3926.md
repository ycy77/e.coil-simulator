---
entity_id: "gene.b3926"
entity_type: "gene"
name: "glpK"
source_database: "NCBI RefSeq"
source_id: "gene-b3926"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3926"
  - "glpK"
---

# glpK

`gene.b3926`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3926`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glpK (gene.b3926) is a gene entity. It encodes glpK (protein.P0A6F3). Encoded protein function: FUNCTION: Key enzyme in the regulation of glycerol uptake and metabolism. Catalyzes the phosphorylation of glycerol to yield sn-glycerol 3-phosphate. It also catalyzes the phosphorylation of dihydroxyacetone, L-glyceraldehyde and D-glyceraldehyde. It uses only ATP. {ECO:0000255|HAMAP-Rule:MF_00186, ECO:0000269|PubMed:2826434, ECO:0000269|PubMed:4575199, ECO:0000269|PubMed:5335908}. EcoCyc product frame: GLYCEROL-KIN-MONOMER. Genomic coordinates: 4115714-4117222. EcoCyc protein note: Glycerol kinase (GlpK) is involved in the utilization of the glycerol moiety of phospholipids and triglycerides after their breakdown into usable forms such as glycerophosphodiesters, sn-glycerol-3-phosphate (G3P) or glycerol. GlpK catalyzes the MgATP-dependent phosphorylation of glycerol to yield sn-glycerol 3-phosphate . This reaction is the rate-limiting step in glycerol utilization . GlpK is a member of a superfamily of proteins that share a common ATPase domain . Inhibition studies suggested an ordered catalytic mechanism, with glycerol binding first , but later experiments support a random catalytic mechanism . The crystal structure of a putative productive conformation of the enzyme is consistent with "half-of-the-sites" reactivity and the importance of domain motion for catalytic activity...

## Biological Role

Repressed by glpR (protein.P0ACL0), nac (protein.Q47005). Activated by fur (protein.P0A9A9).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6F3|protein.P0A6F3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=glpK; function=+
- `represses` <-- [[protein.P0ACL0|protein.P0ACL0]] `RegulonDB` `S` - regulator=GlpR; target=glpK; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=glpK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012825,ECOCYC:EG10398,GeneID:948423`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4115714-4117222:-; feature_type=gene
