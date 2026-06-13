---
entity_id: "gene.b1590"
entity_type: "gene"
name: "ynfH"
source_database: "NCBI RefSeq"
source_id: "gene-b1590"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1590"
  - "ynfH"
---

# ynfH

`gene.b1590`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1590`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ynfH (gene.b1590) is a gene entity. It encodes ynfH (protein.P76173). Encoded protein function: FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. The C subunit anchors the other two subunits to the membrane and stabilize the catalytic subunits (By similarity). {ECO:0000250}. EcoCyc product frame: G6848-MONOMER. Genomic coordinates: 1663609-1664463. EcoCyc protein note: YnfH contains eight potential transmembrane helices and is similar to DmsC, the membrane anchor subunit of the dimethyl sulfoxide reductase heterotrimer. When expressed together with DmsA and either DmsB or YnfG in a plasmid expression system, YnfH can form a complex with DmsA and DmsB/YnfG and support growth on DMSO . A ynfH mutant reaches slightly higher cell density in stationary phase than wild type when growing in media with sublethal levels of streptomycin, an aminoglycoside antibiotic .

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76173|protein.P76173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ynfH; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ynfH; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ynfH; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ynfH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005311,ECOCYC:G6848,GeneID:945822`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1663609-1664463:+; feature_type=gene
