---
entity_id: "gene.b1259"
entity_type: "gene"
name: "yciG"
source_database: "NCBI RefSeq"
source_id: "gene-b1259"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1259"
  - "yciG"
---

# yciG

`gene.b1259`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1259`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yciG (gene.b1259) is a gene entity. It encodes yciG (protein.P21361). Encoded protein function: Uncharacterized protein YciG EcoCyc product frame: EG11127-MONOMER. Genomic coordinates: 1315856-1316035. EcoCyc protein note: This EG11127 gene and its paralog, G0-10443, is homologous to gene STM14_1829 in TAX-90371 14028s that belongs to a family of proteins involved in motility . These two genes also show homology to gene PA2146 in TAX-208964, shown to contribute to both biofilm formation and susceptibility to a variety of antimicrobial agents . Both of these genes are small, intrinsically disordered proteins and have KGG-containing domains (called stress-induced bacterial acidophilic repeat motif) associated with proteins expressed under stressful conditions. yciF contains a Walker nucleotide binding motif that is absent in ymdF; the functional significance of this difference was not examined . Deletion of both yciG and ymdF together exhibited a slight swimming motility defect . Transcription of yciG is induced by sulfometuron methyl, an herbicide that inhibits acetolactate synthase, by salicylate , and by high salt conditions . The yciG gene is part of the σS regulon . The yciGFE locus is expressed poorly . Transcription of yciG has been used as a reporter for analyzing metabolic shifts in response to substrate perturbations .

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by mcbR (protein.P76114).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P21361|protein.P21361]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P76114|protein.P76114]] `RegulonDB` `S` - regulator=McbR; target=yciG; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=yciG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004229,ECOCYC:EG11127,GeneID:947489`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1315856-1316035:-; feature_type=gene
