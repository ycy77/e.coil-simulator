---
entity_id: "gene.b3403"
entity_type: "gene"
name: "pck"
source_database: "NCBI RefSeq"
source_id: "gene-b3403"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3403"
  - "pck"
---

# pck

`gene.b3403`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3403`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pck (gene.b3403) is a gene entity. It encodes pckA (protein.P22259). Encoded protein function: FUNCTION: Involved in the gluconeogenesis. Catalyzes the conversion of oxaloacetate (OAA) to phosphoenolpyruvate (PEP) through direct phosphoryl transfer between the nucleoside triphosphate and OAA. {ECO:0000255|HAMAP-Rule:MF_00453, ECO:0000269|PubMed:1701430, ECO:0000269|PubMed:6986370, ECO:0000269|PubMed:8226637}. EcoCyc product frame: PEPCARBOXYKIN-MONOMER. EcoCyc synonyms: pckA. Genomic coordinates: 3532818-3534440. EcoCyc protein note: Phosphoenolpyruvate (PEP) carboxykinase (Pck) is an enzyme involved in gluconeogenesis. Growth on succinate as the carbon and energy source is limited by the level of Pck in the cell . PEP carboxykinase is unusual in that it appears to be a monomeric enzyme with an allosteric site . Crystal structures of the enzyme have been solved , providing insight into the mechanistic details of the enzymatic reaction and into the mechanism of activation by Ca2+ . Transcription of pck is regulated by catabolite repression and is induced at the onset of stationary phase and is regulated by CsrA . Overexpression of pck during growth on glucose leads to reduced growth yield and increased excretion of fermentation products such as acetate . Expression of Pck is upregulated when acetate is used as the source of carbon...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by crp (protein.P0ACJ8), cra (protein.P0ACP1).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P22259|protein.P22259]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=pck; function=-+
- `activates` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=pck; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=pck; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011106,ECOCYC:EG10688,GeneID:945667`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3532818-3534440:+; feature_type=gene
