---
entity_id: "gene.b1042"
entity_type: "gene"
name: "csgA"
source_database: "NCBI RefSeq"
source_id: "gene-b1042"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1042"
  - "csgA"
---

# csgA

`gene.b1042`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1042`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgA (gene.b1042) is a gene entity. It encodes csgA (protein.P28307). Encoded protein function: FUNCTION: Curlin is the structural subunit of the curli fimbriae. Curli are coiled surface structures that assemble preferentially at growth temperatures below 37 degrees Celsius. Curli can bind to fibronectin. EcoCyc product frame: EG11489-MONOMER. Genomic coordinates: 1104447-1104902. EcoCyc protein note: csgA encodes curlin - the major subunit protein of curli which are thin, coiled surface structures involved in inert surface colonization, biofilm formation, and bacterial binding to a variety of extracellular matrix and serum proteins . Curli production requires CsgA and the nucleator protein G6547-MONOMER "CsgB"; soluble monomeric curlin is secreted from a csgB- strain and can be polymerized into curli on the surface of a csgA- strain grown in close proximity (see also ). Secretion of CsgA is mediated by the CPLX-3945 "curli secretion and assembly complex" and requires the curli assembly component G6545-MONOMER "CsgE" . The periplasmic chaperone, G6548-MONOMER "CsgC" maintains CsgA in a solule monomeric state . Purified CsgA polymerizes into amyloid fibrils in vitro (see also ). CsgA fibrillation can be modulated in vitro using CsgA-derived peptides...

## Biological Role

Repressed by btsR (protein.P0AFT5). Activated by rpoD (protein.P00579), rpoS (protein.P13445), csgD (protein.P52106).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28307|protein.P28307]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=csgA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=csgA; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgA; function=+
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003537,ECOCYC:EG11489,GeneID:949055`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1104447-1104902:+; feature_type=gene
