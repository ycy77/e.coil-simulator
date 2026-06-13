---
entity_id: "gene.b3201"
entity_type: "gene"
name: "lptB"
source_database: "NCBI RefSeq"
source_id: "gene-b3201"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3201"
  - "lptB"
---

# lptB

`gene.b3201`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3201`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lptB (gene.b3201) is a gene entity. It encodes lptB (protein.P0A9V1). Encoded protein function: FUNCTION: Part of the ABC transporter complex LptBFG involved in the translocation of lipopolysaccharide (LPS) from the inner membrane to the outer membrane. Probably responsible for energy coupling to the transport system. {ECO:0000269|PubMed:16765569, ECO:0000269|PubMed:17056748, ECO:0000269|PubMed:18424520}. EcoCyc product frame: YHBG-MONOMER. EcoCyc synonyms: yhbG. Genomic coordinates: 3343944-3344669. EcoCyc protein note: LptB is a cytoplasmic ATPase that energises the transport and assembly of lipopolysaccharide (LPS) by the Lpt system. Depletion of LptB results in impaired LPS transport and outer membrane biogenesis . LptB forms a complex with LptF, LptG and LptC . Sequence analysis suggests that LptB has an ATP binding fold . Purified LptB has ATPase activity in vitro; purified LptB has a KM for ATP of 0.56 mM; ATP binding to LptB is cooperative . Crystal structures of LptB bound to ADP and a catalytically inactive LptB mutant (LptBE163Q) bound to ATP have been obtained and suggest that ATP hydrolysis induces conformational change in LptB . Purified, crystallised LptB is an L-shaped molecule consisting of an ATPase domain containing the characteristic motifs (Walker A and B, and Q loop) and an α-helical domain...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9V1|protein.P0A9V1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lptB; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=lptB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010512,ECOCYC:EG11680,GeneID:947725`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3343944-3344669:+; feature_type=gene
