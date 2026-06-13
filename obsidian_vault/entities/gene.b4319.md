---
entity_id: "gene.b4319"
entity_type: "gene"
name: "fimG"
source_database: "NCBI RefSeq"
source_id: "gene-b4319"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4319"
  - "fimG"
---

# fimG

`gene.b4319`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4319`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimG (gene.b4319) is a gene entity. It encodes fimG (protein.P08190). Encoded protein function: FUNCTION: Involved in regulation of length and mediation of adhesion of type 1 fimbriae (but not necessary for the production of fimbriae). Involved in the integration of FimH in the fimbriae. EcoCyc product frame: EG10314-MONOMER. Genomic coordinates: 4548285-4548788. EcoCyc protein note: FimG is a minor component of the type 1 fimbriae in Escherichia coli. Two-dimensional gel electrophoresis indicated that FimG has a molecular weight of 17.0 kDa and exists in a 1:100 ratio with the major fimbrial subunit, FimA . FimF and FimG are subunits of the tip fibrillum which are thought to function as adaptor proteins, linking the helical rod composed of FimA subunits to the the adhesin FimH at the tip of the fibrillum . Transcription of fimG is induced upon biofilm formation . E. coli K-12 contains 12 chaperone-usher fimbrial operons, including fimAICDFGH; a fimbria-lacking mutant - strain WQM026 - created by deleting all 12 operons has been characterised .

## Biological Role

Activated by rpoD (protein.P00579), fis (protein.P0A6R3), hns (protein.P0ACF8), lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08190|protein.P08190]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimG; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fimG; function=+
- `activates` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimG; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `C` - regulator=Lrp; target=fimG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014155,ECOCYC:EG10314,GeneID:948846`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4548285-4548788:+; feature_type=gene
