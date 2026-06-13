---
entity_id: "gene.b1734"
entity_type: "gene"
name: "chbF"
source_database: "NCBI RefSeq"
source_id: "gene-b1734"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1734"
  - "chbF"
---

# chbF

`gene.b1734`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1734`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

chbF (gene.b1734) is a gene entity. It encodes chbF (protein.P17411). Encoded protein function: FUNCTION: Hydrolyzes a wide variety of P-beta-glucosides including cellobiose-6P, salicin-6P, arbutin-6P, gentiobiose-6P, methyl-beta-glucoside-6P and p-nitrophenyl-beta-D-glucopyranoside-6P. Is also able to hydrolyze phospho-N,N'-diacetylchitobiose. {ECO:0000269|PubMed:10572139, ECO:0000269|PubMed:10913117}. EcoCyc product frame: EG10144-MONOMER. EcoCyc synonyms: ydjD, celF. Genomic coordinates: 1817148-1818500. EcoCyc protein note: ChbF is a monoacetylchitobiose-6-phosphate hydrolase encoded as part of the chb operon, which encodes enzymes involved in growth on CHITOBIOSE as the sole source of carbon and energy . ChbF belongs to family 4 of the glycosylhydrolase superfamily . ChbF hdrolyzes the reaction product of ChbG to glucosamine-6-phosphate and N-acetylglucosamine and also cleaves diacetylchitotriose-phosphate to diacetyl-chitobiose and glucosamine-6-phosphate. ChbF is unable to utilize diacetylchitobiose-phosphate, the product of the ChbBCA PTS transporter . Substrate specificity of the enzyme was investigated by ; unfortunately, chitobiose derivatives were not among the tested substrates. A ΔchbF strain is unable to grow on diacetylchitobiose as the sole source of carbon and energy . ChbF: "N,N'-diacetylchitobiose F"

## Biological Role

Repressed by nagC (protein.P0AF20), chbR (protein.P17410). Activated by crp (protein.P0ACJ8), chbR (protein.P17410).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17411|protein.P17411]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=chbF; function=+
- `activates` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbF; function=-+
- `represses` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=chbF; function=-
- `represses` <-- [[protein.P17410|protein.P17410]] `RegulonDB` `S` - regulator=ChbR; target=chbF; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0005785,ECOCYC:EG10144,GeneID:946266`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1817148-1818500:-; feature_type=gene
