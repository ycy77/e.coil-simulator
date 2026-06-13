---
entity_id: "gene.b4239"
entity_type: "gene"
name: "treC"
source_database: "NCBI RefSeq"
source_id: "gene-b4239"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4239"
  - "treC"
---

# treC

`gene.b4239`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4239`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

treC (gene.b4239) is a gene entity. It encodes treC (protein.P28904). Encoded protein function: FUNCTION: Hydrolyzes trehalose-6-phosphate to glucose and glucose 6-phosphate. Can also very effectively hydrolyze p-nitrophenyl-alpha-D-glucopyranoside, but it does not recognize trehalose, sucrose, maltose, isomaltose, or maltodextrins. {ECO:0000269|PubMed:8083158}. EcoCyc product frame: TRE6PHYDRO-MONOMER. EcoCyc synonyms: treE, olgH. Genomic coordinates: 4463054-4464709. EcoCyc protein note: E. coli can utilize trehalose as the sole source of carbon. Under low-osmolarity conditions, trehalose is imported into the cytoplasm by the trehalose-specific PTS transporter, converting it into trehalose-6-phoshate. Trehalose-6-phosphate hydrolase (TreC) then hydrolyzes trehalose-6-phosphate into glucose and glucose-6-phosphate . TreC may be able to catalyze the conversion of maltose to maltose-1-phosphate, which may act as an inducer of malK expression . Expression of TreC is induced by trehalose, but only under low-osmolarity conditions .

## Biological Role

Repressed by treR (protein.P36673).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28904|protein.P28904]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P36673|protein.P36673]] `RegulonDB` `S` - regulator=TreR; target=treC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013870,ECOCYC:EG11402,GeneID:948762`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4463054-4464709:-; feature_type=gene
