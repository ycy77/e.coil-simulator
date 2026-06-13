---
entity_id: "gene.b4262"
entity_type: "gene"
name: "lptG"
source_database: "NCBI RefSeq"
source_id: "gene-b4262"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4262"
  - "lptG"
---

# lptG

`gene.b4262`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4262`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptG (gene.b4262) is a gene entity. It encodes lptG (protein.P0ADC6). Encoded protein function: FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. {ECO:0000269|PubMed:18375759}. EcoCyc product frame: G7889-MONOMER. EcoCyc synonyms: yjgQ. Genomic coordinates: 4487318-4488400. EcoCyc protein note: LptG is an inner membrane component of the Lpt lipopolysaccharide transport system. LptG contains six predicted transmembrane domains and its C-terminus is located in the cytoplasm . lptG is essential in E.coli . Depletion of LptG results in increased outer membrane permeability and lipopolysaccharides do not reach the outer leaflet of the outer membrane . LptG forms a complex with LptF, LptB and LptC . LptG and LptF each contain a coupling helix which mediates their interaction with LptB; the LptFG coupling helices likely coordinate ATPase activity with LPS extraction from the inner membrane but each appears to have a distinct role (see further ). An LPS binding domain in LptG (which includes residues K34, D37, Q38, K40 and K41) has been identified .

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADC6|protein.P0ADC6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013960,ECOCYC:G7889,GeneID:945324`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4487318-4488400:+; feature_type=gene
