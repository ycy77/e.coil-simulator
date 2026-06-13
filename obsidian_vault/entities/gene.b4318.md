---
entity_id: "gene.b4318"
entity_type: "gene"
name: "fimF"
source_database: "NCBI RefSeq"
source_id: "gene-b4318"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4318"
  - "fimF"
---

# fimF

`gene.b4318`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4318`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimF (gene.b4318) is a gene entity. It encodes fimF (protein.P08189). Encoded protein function: FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Involved in the integration of FimH in the fimbriae. EcoCyc product frame: EG10313-MONOMER. Genomic coordinates: 4547742-4548272. EcoCyc protein note: FimF is a minor component of the type 1 fimbriae in Escherichia coli. Two-dimensional gel electrophoresis indicated that FimF has a molecular weight of 18.0 kDa and exists in a 1:100 ratio with the major fimbrial subunit, FimA . FimF and FimG are subunits of the tip fibrillum which are thought to function as adaptor proteins, linking the helical rod composed of FimA subunits to the the adhesin FimH at the tip of the fibrillum . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including fimAICDFGH; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08189|protein.P08189]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimF; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimF; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimF; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014153,ECOCYC:EG10313,GeneID:948845`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4547742-4548272:+; feature_type=gene
