---
entity_id: "gene.b3564"
entity_type: "gene"
name: "xylB"
source_database: "NCBI RefSeq"
source_id: "gene-b3564"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3564"
  - "xylB"
---

# xylB

`gene.b3564`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3564`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylB (gene.b3564) is a gene entity. It encodes xylB (protein.P09099). Encoded protein function: FUNCTION: Catalyzes the phosphorylation of D-xylulose to D-xylulose 5-phosphate (PubMed:17123542). Also catalyzes the phosphorylation of 1-deoxy-D-xylulose to 1-deoxy-D-xylulose 5-phosphate, with lower efficiency (PubMed:11168365). Can also use D-ribulose, xylitol and D-arabitol, but D-xylulose is preferred over the other substrates (PubMed:17123542). Has a weak substrate-independent Mg-ATP-hydrolyzing activity (PubMed:17123542). {ECO:0000269|PubMed:11168365, ECO:0000269|PubMed:17123542}. EcoCyc product frame: XYLULOKIN-MONOMER. Genomic coordinates: 3727917-3729371. EcoCyc protein note: Xylulokinase catalyzes the phosphorylation of D-xylulose, the second step in the xylose degradation pathway, producing D-xylulose-5-phosphate, an intermediate of the pentose phosphate pathway. In the absence of substrate, xylulokinase has weak ATPase activity . Xylulokinase can also catalyze the phosphorylation of 1-deoxy-D-xylulose. This would allow a potential salvage pathway for generating 1-deoxy-D-xylulose 5-phosphate for use in the biosynthesis of terpenoids, thiamine and pyridoxal . The kinetic mechanism of the enzyme has been studied, suggesting a predominantly ordered reaction mechanism. The enzyme undergoes significant conformational changes upon binding of the substrate and of ATP...

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by xylR (protein.P0ACI3).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09099|protein.P09099]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylB; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=xylB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011637,ECOCYC:EG11075,GeneID:948133`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3727917-3729371:-; feature_type=gene
