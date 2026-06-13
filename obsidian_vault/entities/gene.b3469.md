---
entity_id: "gene.b3469"
entity_type: "gene"
name: "zntA"
source_database: "NCBI RefSeq"
source_id: "gene-b3469"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3469"
  - "zntA"
---

# zntA

`gene.b3469`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3469`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zntA (gene.b3469) is a gene entity. It encodes zntA (protein.P37617). Encoded protein function: FUNCTION: Confers resistance to zinc, cadmium and lead (PubMed:10660539, PubMed:17326661, PubMed:9364914, PubMed:9405611, PubMed:9830000). Couples the hydrolysis of ATP with the export of zinc, cadmium or lead, with highest activity when the metals are present as metal-thiolate complexes (PubMed:10660539, PubMed:17326661, PubMed:9405611). Can also bind nickel, copper, cobalt and mercury (PubMed:10660539, PubMed:17326661). {ECO:0000269|PubMed:10660539, ECO:0000269|PubMed:17326661, ECO:0000269|PubMed:9364914, ECO:0000269|PubMed:9405611, ECO:0000269|PubMed:9830000}. EcoCyc product frame: YHHO-MONOMER. EcoCyc synonyms: yhhO. Genomic coordinates: 3606451-3608649. EcoCyc protein note: zntA encodes a P-type ATPase that mediates export of the divalent metal ions Zn2+, Cd2+ and Pb2+ . ZntA mediated metal ion export contributes to Zn2+ homeostasis and confers resistance to Cd2+ and Pb2+ (see ). The enzyme has low activity with Ni2+, Co2+, and Cu2+ in vitro but these metal ions are not physiologically relevant substrates . Purified ZntA has metal (Pb2+, Zn2+, Cd2+)-induced ATPase activity; metal-thiolates may be the true substrate in vivo . In the solution NMR structure of a ZntA fragment (ZntA26-118) reported by mononunuclear Zn is bound through Cys-59, Cys-62 and Asp-58 side-chains...

## Biological Role

Repressed by zntR (protein.P0ACS5). Activated by rpoD (protein.P00579), zntR (protein.P0ACS5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37617|protein.P37617]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=zntA; function=+
- `activates` <-- [[protein.P0ACS5|protein.P0ACS5]] `RegulonDB` `C` - regulator=ZntR; target=zntA; function=-+
- `represses` <-- [[protein.P0ACS5|protein.P0ACS5]] `RegulonDB` `C` - regulator=ZntR; target=zntA; function=-+

## External IDs

- `Dbxref:ECOCYC:EG12215,GeneID:947972`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3606451-3608649:+; feature_type=gene
