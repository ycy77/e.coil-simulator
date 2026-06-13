---
entity_id: "gene.b3565"
entity_type: "gene"
name: "xylA"
source_database: "NCBI RefSeq"
source_id: "gene-b3565"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3565"
  - "xylA"
---

# xylA

`gene.b3565`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3565`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylA (gene.b3565) is a gene entity. It encodes xylA (protein.P00944). Encoded protein function: Xylose isomerase (EC 5.3.1.5) (D-xylulose keto-isomerase) EcoCyc product frame: XYLISOM-MONOMER. Genomic coordinates: 3729443-3730765. EcoCyc protein note: Xylose isomerase catalyzes the conversion of D-xylose to D-xylulose, the first reaction in the XYLCAT-PWY pathway . Two conserved histidine residues, H101 and H271, were shown to be essential for catalytic activity . The fluorescence of two conserved tryptophan residues, W49 and W188, is quenched during binding of xylose, and W49 was shown to be essential for catalytic activity . The presence of Mg2+, Mn2+ or Co2+ protects the enzyme from thermal denaturation . Expression of xylose isomerase is induced in the presence of xylose and is under catabolite repression . An amber mutation has been generated . Reviews:

## Biological Role

Repressed by araC (protein.P0A9E0). Activated by xylR (protein.P0ACI3).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00944|protein.P00944]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylA; function=+
- `represses` <-- [[protein.P0A9E0|protein.P0A9E0]] `RegulonDB` `S` - regulator=AraC; target=xylA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011639,ECOCYC:EG11074,GeneID:948141`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3729443-3730765:-; feature_type=gene
