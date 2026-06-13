---
entity_id: "gene.b0351"
entity_type: "gene"
name: "mhpF"
source_database: "NCBI RefSeq"
source_id: "gene-b0351"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0351"
  - "mhpF"
---

# mhpF

`gene.b0351`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0351`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpF (gene.b0351) is a gene entity. It encodes mhpF (protein.P77580). Encoded protein function: FUNCTION: Catalyzes the conversion of acetaldehyde to acetyl-CoA, using NAD(+) and coenzyme A. Is the final enzyme in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. Functions as a chaperone protein for folding of MhpE. {ECO:0000269|PubMed:16782065}. EcoCyc product frame: MHPF-MONOMER. Genomic coordinates: 372921-373871. EcoCyc protein note: mhpF encodes an acetylating acetaldehyde dehydrogenase . MhpF is active as a monomer; the rate-limiting step of the reaction appears to be transthioesterification . MhpF is involved in synthesis of n-butanol in an engineered reversal of the β-oxidation pathway . The expression of MhpE is translationally coupled to MhpF, and interaction between the two proteins appears to be required for solubility of MhpE .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), mhpR (protein.P77569).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77580|protein.P77580]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpF; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpF; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001207,ECOCYC:M014,GeneID:945008`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:372921-373871:+; feature_type=gene
