---
entity_id: "gene.b1041"
entity_type: "gene"
name: "csgB"
source_database: "NCBI RefSeq"
source_id: "gene-b1041"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1041"
  - "csgB"
---

# csgB

`gene.b1041`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1041`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgB (gene.b1041) is a gene entity. It encodes csgB (protein.P0ABK7). Encoded protein function: FUNCTION: Curlin is the structural subunit of the curli fimbriae. Curli are coiled surface structures that assemble preferentially at growth temperatures below 37 degrees Celsius. Curli can bind to fibronectin. The minor subunit is the nucleation component of curlin monomers. Coexpression of cellulose and thin aggregative fimbriae (curli fimbrae or fibers) leads to a hydrophobic network with tightly packed cells embedded in a highly inert matrix that confers cohesion, elasticity and tissue-like properties to colonies (PubMed:24097954). {ECO:0000269|PubMed:24097954}. EcoCyc product frame: G6547-MONOMER. Genomic coordinates: 1103951-1104406. EcoCyc protein note: CsgB is the minor curlin subunit, which functions as a nucleator, triggering the polymerization of CsgA to form curli fibers on the cell surface . CsgB is located on the cell surface and is a minor component of wild-type curli . The mature CsgB protein contains an unstructured 22 amino acid N-terminal region plus a second domain consisting of 5 repeating units (r1 to r5) of imperfect homology. Each repeating unit is predicted to form 2 β strands . A non-polar csgB mutation abolishes curli production without affecting production of EG11489-MONOMER "CsgA" - the major curlin subunit...

## Biological Role

Repressed by btsR (protein.P0AFT5). Activated by rpoD (protein.P00579), rpoS (protein.P13445), csgD (protein.P52106).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABK7|protein.P0ABK7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=csgB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=csgB; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgB; function=+
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003534,ECOCYC:G6547,GeneID:947391`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1103951-1104406:+; feature_type=gene
