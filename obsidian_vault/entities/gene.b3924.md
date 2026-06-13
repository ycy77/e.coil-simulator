---
entity_id: "gene.b3924"
entity_type: "gene"
name: "fpr"
source_database: "NCBI RefSeq"
source_id: "gene-b3924"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3924"
  - "fpr"
---

# fpr

`gene.b3924`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3924`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fpr (gene.b3924) is a gene entity. It encodes fpr (protein.P28861). Encoded protein function: FUNCTION: Transports electrons between flavodoxin or ferredoxin and NADPH (PubMed:12234497, PubMed:21306142, PubMed:8449868, PubMed:9839946). Reduces flavodoxin 1, flavodoxin 2 and ferredoxin, ferredoxin being the kinetically and thermodynamically preferred partner (PubMed:12234497). Required for the activation of several enzymes such as pyruvate formate-lyase, anaerobic ribonucleotide reductase and cobalamin-dependent methionine synthase (PubMed:7042345, PubMed:8267617). {ECO:0000269|PubMed:12234497, ECO:0000269|PubMed:21306142, ECO:0000269|PubMed:7042345, ECO:0000269|PubMed:8267617, ECO:0000269|PubMed:8449868, ECO:0000269|PubMed:9839946}. EcoCyc product frame: FLAVONADPREDUCT-MONOMER. EcoCyc synonyms: flxR, mvrA. Genomic coordinates: 4113726-4114472. EcoCyc protein note: Flavodoxin/ferredoxin-NADP+ reductase (Fpr) participates in chains of redox reactions; it contains a noncovalently bound FAD cofactor that facilitates the reversible electron transfer between NADP(H) and ferredoxins or flavodoxins. Fpr is involved in the activation of anaerobic ribonucleoside reductase , pyruvate-formate lyase (PFL) , methionine synthase and biotin synthase . Ferredoxin can not substitute for flavodoxin as an electron donor for activation of PFL and methionine synthase...

## Biological Role

Activated by soxS (protein.P0A9E2), marA (protein.P0ACH5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P28861|protein.P28861]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=fpr; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=fpr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012818,ECOCYC:EG10628,GeneID:948414`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4113726-4114472:-; feature_type=gene
