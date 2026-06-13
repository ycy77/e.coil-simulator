---
entity_id: "gene.b3430"
entity_type: "gene"
name: "glgC"
source_database: "NCBI RefSeq"
source_id: "gene-b3430"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3430"
  - "glgC"
---

# glgC

`gene.b3430`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3430`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgC (gene.b3430) is a gene entity. It encodes glgC (protein.P0A6V1). Encoded protein function: FUNCTION: Involved in the biosynthesis of ADP-glucose, a building block required for the elongation reactions to produce glycogen. Catalyzes the reaction between ATP and alpha-D-glucose 1-phosphate (G1P) to produce pyrophosphate and ADP-Glc. {ECO:0000269|PubMed:1648099}. EcoCyc product frame: GLUC1PADENYLTRANS-MONOMER. Genomic coordinates: 3568033-3569328. EcoCyc protein note: Glucose-1-phosphate adenylyltransferase (GlgC) catalyzes the rate-limiting first step in the biosynthesis of glycogen. The enzyme is allosterically activated by the glycolytic intermediate fructose-1,6-bisphosphate (FBP) and inhibited by AMP and pyrophosphate, thus responding to the energy state of the cell. GlgC consists of an N-terminal glycosyltransferase A-like domain and a C-terminal regulatory domain . Various mutants and truncated forms of the enzyme have been studied . Co-expression of separately encoded N- and C-terminal domain polypeptides yields an active enzyme. The two domains interact strongly . The Asp142 residue is important for catalytic activity . Homology modelling and site-directed mutagenesis allowed the identification of residues that play a role in binding of glucose-1-phosphate...

## Biological Role

Repressed by lrp (protein.P0ACJ0), csrA (protein.P69913). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6V1|protein.P0A6V1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glgC; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=glgC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=glgC; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=carbon storage regulator CsrA; target=glgC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011204,ECOCYC:EG10379,GeneID:947942`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3568033-3569328:-; feature_type=gene
