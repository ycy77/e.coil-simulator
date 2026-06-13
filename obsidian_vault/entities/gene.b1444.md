---
entity_id: "gene.b1444"
entity_type: "gene"
name: "patD"
source_database: "NCBI RefSeq"
source_id: "gene-b1444"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1444"
  - "patD"
---

# patD

`gene.b1444`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1444`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

patD (gene.b1444) is a gene entity. It encodes patD (protein.P77674). Encoded protein function: FUNCTION: Catalyzes the oxidation 4-aminobutanal (gamma-aminobutyraldehyde) to 4-aminobutanoate (gamma-aminobutyrate or GABA) (PubMed:16023116, PubMed:3510672). This is the second step in one of two pathways for putrescine degradation, where putrescine is converted into 4-aminobutanoate via 4-aminobutanal, which allows E.coli to grow on putrescine as the sole nitrogen source (PubMed:22636776, PubMed:3510672). Also functions as a 5-aminopentanal dehydrogenase in a a L-lysine degradation pathway to succinate that proceeds via cadaverine, glutarate and L-2-hydroxyglutarate (PubMed:30498244). Can also oxidize n-alkyl medium-chain aldehydes, but with a lower catalytic efficiency (PubMed:15381418, PubMed:16023116). {ECO:0000269|PubMed:15381418, ECO:0000269|PubMed:16023116, ECO:0000269|PubMed:22636776, ECO:0000269|PubMed:30498244, ECO:0000269|PubMed:3510672}. EcoCyc product frame: G6755-MONOMER. EcoCyc synonyms: prr, ydcW. Genomic coordinates: 1515578-1517002. EcoCyc protein note: γ-aminobutyraldehyde dehydrogenase (PatD) is the second enzyme in one of two pathways for putrescine degradation (PUTDEG-PWY) . PatD along with ALDHDEHYDROG-MONOMER "PuuC" are two enzymes in E. coli known to carry out γ-aminobutyraldehyde dehydrogenase activity...

## Biological Role

Activated by nac (protein.Q47005).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00410` beta-Alanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77674|protein.P77674]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=patD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0004813,ECOCYC:G6755,GeneID:945876`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1515578-1517002:+; feature_type=gene
