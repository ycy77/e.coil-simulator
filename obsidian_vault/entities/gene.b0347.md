---
entity_id: "gene.b0347"
entity_type: "gene"
name: "mhpA"
source_database: "NCBI RefSeq"
source_id: "gene-b0347"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0347"
  - "mhpA"
---

# mhpA

`gene.b0347`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0347`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpA (gene.b0347) is a gene entity. It encodes mhpA (protein.P77397). Encoded protein function: FUNCTION: Catalyzes the insertion of one atom of molecular oxygen into position 2 of the phenyl ring of 3-(3-hydroxyphenyl)propionate (3-HPP) and hydroxycinnamic acid (3HCI). {ECO:0000269|PubMed:9603882}. EcoCyc product frame: MHPHYDROXY-MONOMER. Genomic coordinates: 368611-370275. EcoCyc protein note: E. coli is able to utilize aromatic acids as carbon and energy sources. A meta-cleavage pathway is used for the catabolism of 3-(3-hydroxyphenyl)propionate . mhpA encodes a flavin-type monooxygenase that was purified and biochemically characterized only recently . The C terminus of MhpA does not show similarity to other 3-hydroxyaromatic acid hydroxylases; however, it is required for catalytic activity . A ΔmhpA mutant is unable to grow with 3-(3-hydroxyphenyl)propionate (3HPP, MHP) as the sole source of carbon . Enzyme activity is induced after growth with MHP or hydroxycinnamate (HCA) .

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), mhpR (protein.P77569).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77397|protein.P77397]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpA; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001196,ECOCYC:M010,GeneID:945197`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:368611-370275:+; feature_type=gene
