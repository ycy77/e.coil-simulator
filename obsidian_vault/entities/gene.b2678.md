---
entity_id: "gene.b2678"
entity_type: "gene"
name: "proW"
source_database: "NCBI RefSeq"
source_id: "gene-b2678"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2678"
  - "proW"
---

# proW

`gene.b2678`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2678`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proW (gene.b2678) is a gene entity. It encodes proW (protein.P14176). Encoded protein function: FUNCTION: Part of the ProU ABC transporter complex involved in glycine betaine and proline betaine uptake (PubMed:23249124, PubMed:3305496, PubMed:7898450). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:23249124, ECO:0000269|PubMed:3305496, ECO:0000269|PubMed:7898450, ECO:0000305}. EcoCyc product frame: PROW-MONOMER. EcoCyc synonyms: osrA, proU. Genomic coordinates: 2806010-2807074. EcoCyc protein note: ProW is the predicted integral membrane subunit of an osmoresponsive ABC transport system that imports compounds such as glycine betaine and proline betaine in response to osmotic upshift. ProW is predicted to contain 7 transmembrane regions and an N-terminal domain that protrudes into the periplasm

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P14176|protein.P14176]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=proW; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=proW; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=proW; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008816,ECOCYC:EG10772,GeneID:947145`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2806010-2807074:+; feature_type=gene
