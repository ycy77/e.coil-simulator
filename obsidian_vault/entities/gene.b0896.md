---
entity_id: "gene.b0896"
entity_type: "gene"
name: "dmsC"
source_database: "NCBI RefSeq"
source_id: "gene-b0896"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0896"
  - "dmsC"
---

# dmsC

`gene.b0896`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0896`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dmsC (gene.b0896) is a gene entity. It encodes dmsC (protein.P18777). Encoded protein function: FUNCTION: Terminal reductase during anaerobic growth on various sulfoxide and N-oxide compounds. DmsC anchors the DmsAB dimer to the membrane and stabilizes it. EcoCyc product frame: DMSC-MONOMER. Genomic coordinates: 944033-944896. EcoCyc protein note: DmsC is the integral membrane subunit of the DMSO reductase complex. It is predicted to have 8 transmembrane helices with the N and C termini located in the periplasm . This subunit anchors and stabilizes the catalytic subunits DmsA and DmsB . A glutamate residue, E87, is important for menaquinol binding and oxidation .

## Biological Role

Repressed by modE (protein.P0A9G8), narL (protein.P0AF28). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), fnr (protein.P0A9E5).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P18777|protein.P18777]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dmsC; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=dmsC; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=dmsC; function=+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=dmsC; function=-
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dmsC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003048,ECOCYC:EG10234,GeneID:945502`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:944033-944896:+; feature_type=gene
