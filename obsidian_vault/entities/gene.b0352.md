---
entity_id: "gene.b0352"
entity_type: "gene"
name: "mhpE"
source_database: "NCBI RefSeq"
source_id: "gene-b0352"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0352"
  - "mhpE"
---

# mhpE

`gene.b0352`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0352`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mhpE (gene.b0352) is a gene entity. It encodes mhpE (protein.P51020). Encoded protein function: FUNCTION: Catalyzes the retro-aldol cleavage of 4-hydroxy-2-oxopentanoate to pyruvate and acetaldehyde. Is involved in the meta-cleavage pathway for the degradation of 3-phenylpropanoate. {ECO:0000269|PubMed:9758851}. EcoCyc product frame: MHPELY-MONOMER. Genomic coordinates: 373868-374881. EcoCyc protein note: 4-hydroxy-2-ketopentanoate aldolase (MhpE) is a stereospecific class I aldolase . The expression of MhpE is translationally coupled to MhpF, and interaction between the two proteins appears to be required for solubility of MhpE . E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving MhpE is used for the catabolism of 3-phenylpropionate . MhpE: "m-hydroxyphenylpropionate"

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), mhpR (protein.P77569).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00362` Benzoate degradation (KEGG)
- `eco00621` Dioxin degradation (KEGG)
- `eco00622` Xylene degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P51020|protein.P51020]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mhpE; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=mhpE; function=+
- `activates` <-- [[protein.P77569|protein.P77569]] `RegulonDB` `C` - regulator=MhpR; target=mhpE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001209,ECOCYC:G6205,GeneID:945012`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:373868-374881:+; feature_type=gene
