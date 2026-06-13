---
entity_id: "gene.b0343"
entity_type: "gene"
name: "lacY"
source_database: "NCBI RefSeq"
source_id: "gene-b0343"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0343"
  - "lacY"
---

# lacY

`gene.b0343`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0343`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lacY (gene.b0343) is a gene entity. It encodes lacY (protein.P02920). Encoded protein function: FUNCTION: Responsible for transport of beta-galactosides into the cell, with the concomitant import of a proton (symport system). Can transport lactose, melibiose, the synthetic disaccharide lactulose or the analog methyl-1-thio-beta,D-galactopyranoside (TMG), but not sucrose or fructose (PubMed:18177889, PubMed:1848449, PubMed:22106930, PubMed:7000781, PubMed:7028742). The substrate specificity is directed toward the galactopyranosyl moiety of the substrate (PubMed:22106930). {ECO:0000269|PubMed:18177889, ECO:0000269|PubMed:1848449, ECO:0000269|PubMed:22106930, ECO:0000269|PubMed:7000781, ECO:0000269|PubMed:7028742}. EcoCyc product frame: LACY-MONOMER. Genomic coordinates: 361926-363179. EcoCyc protein note: The lactose permease LacY is a galactoside:proton symporter, responsible for the uptake of lactose and other galactosides. LacY is a member of the major facilitator superfamily (MFS) of transporters and is probably the best characterised secondary transporter. β-galactoside transport was first described in the mid twentieth century (reviewed in and studies of lactose transport were instrumental in elucidating and confirming the chemiosmotic theory for energy transfer in cells . The lacY gene was the first transporter gene to be cloned and sequenced...

## Biological Role

Repressed by lacI (protein.P03023), hns (protein.P0ACF8), marA (protein.P0ACH5), crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02920|protein.P02920]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lacY; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=lacY; function=-+
- `represses` <-- [[protein.P03023|protein.P03023]] `RegulonDB` `C` - regulator=LacI; target=lacY; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=lacY; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=lacY; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=lacY; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0001181,ECOCYC:EG10526,GeneID:949083`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:361926-363179:-; feature_type=gene
