---
entity_id: "gene.b0708"
entity_type: "gene"
name: "phr"
source_database: "NCBI RefSeq"
source_id: "gene-b0708"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0708"
  - "phr"
---

# phr

`gene.b0708`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0708`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phr (gene.b0708) is a gene entity. It encodes phrB (protein.P00914). Encoded protein function: FUNCTION: Involved in repair of UV radiation-induced DNA damage. Catalyzes the light-dependent monomerization (300-600 nm) of cyclobutyl pyrimidine dimers (in cis-syn configuration), which are formed between adjacent bases on the same DNA strand upon exposure to ultraviolet radiation. EcoCyc product frame: EG10736-MONOMER. EcoCyc synonyms: phrB. Genomic coordinates: 739507-740925. EcoCyc protein note: phr encodes the DNA repair enzyme, deoxyribodipyrimidine photolyase (DNA photolyase; photoreactivating enzyme or PRE). DNA photolyase mediates blue-light dependent repair of cyclobutane pyrimidine dimers (CPDs; most commonly Thy<>Thy) which are produced by exposure of cells to UV radiation at 200-300nm. Early studies on photoreactivation (PR) were conducted using E. coli B strains (see for example ). phr has been cloned and its protein product purified. The active, purified enzyme is a monomer and repairs UV-irradiated DNA (UV-pBR322) in a light dependent reaction; the enzyme contains two prosthetic groups - a light harvesting cofactor or antenna pigment, 5,10-methenyltetrahydrofolate polyglutamate (see 5-10-METHENYL-THF-GLU-N), and a catalytic flavin adenine dinucleotide (FAD) cofactor (active in the FADH- form in vivo)...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00914|protein.P00914]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=phr; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002417,ECOCYC:EG10736,GeneID:947005`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:739507-740925:+; feature_type=gene
