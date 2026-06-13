---
entity_id: "gene.b0732"
entity_type: "gene"
name: "mngB"
source_database: "NCBI RefSeq"
source_id: "gene-b0732"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0732"
  - "mngB"
---

# mngB

`gene.b0732`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0732`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mngB (gene.b0732) is a gene entity. It encodes mngB (protein.P54746). Encoded protein function: FUNCTION: May hydrolyze 6-phospho-mannosyl-D-glycerate to mannose-6-phosphate and glycerate. {ECO:0000269|PubMed:14645248}. EcoCyc product frame: EG13236-MONOMER. EcoCyc synonyms: ybgG. Genomic coordinates: 767978-770611. EcoCyc protein note: MngB is an α-mannosidase that appears to be responsible for the conversion of 2-O-(6-phospho-α-mannosyl)-D-glycerate (MG-P) to mannose-6-phosphate and glycerate in the PWY0-1300 pathway . The enzyme has not yet been purified and assayed in vitro. Expression of mngAB is repressed by MngR and induced when cells are grown in 2-O-α-mannosyl-D-glycerate (MG). mngB mutants are unable to grow in medium containing high levels of MG (without secondary mutations in mngA), likely due to the toxicity of accumulating MG-P within the cells . MngB: "mannosylglycerate catabolism B"

## Biological Role

Repressed by mngR (protein.P13669). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P54746|protein.P54746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mngB; function=+
- `represses` <-- [[protein.P13669|protein.P13669]] `RegulonDB` `S` - regulator=MngR; target=mngB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002495,ECOCYC:EG13236,GeneID:945359`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:767978-770611:+; feature_type=gene
