---
entity_id: "gene.b2388"
entity_type: "gene"
name: "glk"
source_database: "NCBI RefSeq"
source_id: "gene-b2388"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2388"
  - "glk"
---

# glk

`gene.b2388`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2388`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glk (gene.b2388) is a gene entity. It encodes glk (protein.P0A6V8). Encoded protein function: FUNCTION: An ATP-dependent kinase that phosphorylates glucose to make glucose-6-phosphate, not active on fructose, galactose or mannose. Not highly important in wild-type E.coli as glucose is transported into the cell by the PTS system as glucose 6-phosphate. {ECO:0000269|PubMed:9023215}. EcoCyc product frame: GLUCOKIN-MONOMER. Genomic coordinates: 2508461-2509426. EcoCyc protein note: The cytoplasmic glucokinase is not required for growth on glucose as the carbon source, because glucose is phosphorylated during transport by the PTS system. Glucokinase phosphorylates glucose which is produced by amylomaltase. Growth on glucose reduces the expression of glk by 50%. Growth on other carbon sources does not appear to affect glk expression . Overexpression of foreign proteins appears to induce expression of glk as well . A crystal structure of the enzyme from E. coli O157:H7 has been reported . Evolutionary relationships between glucose kinases based on their tertiary structures have been discussed . A periplasmic glucokinase whose expression is induced during overexpression of foreign proteins has been reported, but it does not appear to be the product of the glk gene . A role for cytoplasmic glucose and Glk in the complex regulation of maltose and maltodextrin utilization by E...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), cra (protein.P0ACP1), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00521` Streptomycin biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6V8|protein.P0A6V8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glk; function=+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=glk; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glk; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=glk; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007875,ECOCYC:EG12957,GeneID:946858`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2508461-2509426:-; feature_type=gene
