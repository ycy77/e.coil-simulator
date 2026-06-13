---
entity_id: "gene.b2925"
entity_type: "gene"
name: "fbaA"
source_database: "NCBI RefSeq"
source_id: "gene-b2925"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2925"
  - "fbaA"
---

# fbaA

`gene.b2925`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2925`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fbaA (gene.b2925) is a gene entity. It encodes fbaA (protein.P0AB71). Encoded protein function: FUNCTION: Catalyzes the aldol condensation of dihydroxyacetone phosphate (DHAP or glycerone-phosphate) with glyceraldehyde 3-phosphate (G3P) to form fructose 1,6-bisphosphate (FBP) in gluconeogenesis and the reverse reaction in glycolysis (PubMed:10712619). In addition, is involved in the utilization of D-sedoheptulose 7-phosphate, an intermediate of the pentose phosphate pathway, via the sedoheptulose bisphosphate bypass pathway (PubMed:19756045). Catalyzes the cleavage of D-sedoheptulose 1,7-bisphosphate to glyceraldehyde 3-phosphate and erythrose 4-phosphate (PubMed:19756045). {ECO:0000269|PubMed:10712619, ECO:0000269|PubMed:19756045}. EcoCyc product frame: FRUCTBISALD-CLASSII-MONOMER. EcoCyc synonyms: ald, fba, fda. Genomic coordinates: 3070165-3071244.

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00030` Pentose phosphate pathway (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB71|protein.P0AB71]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fbaA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=fbaA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=fbaA; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=fbaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009600,ECOCYC:EG10282,GeneID:947415`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3070165-3071244:-; feature_type=gene
