---
entity_id: "gene.b2133"
entity_type: "gene"
name: "dld"
source_database: "NCBI RefSeq"
source_id: "gene-b2133"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2133"
  - "dld"
---

# dld

`gene.b2133`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2133`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dld (gene.b2133) is a gene entity. It encodes dld (protein.P06149). Encoded protein function: FUNCTION: Catalyzes the oxidation of D-lactate to pyruvate. Electrons derived from D-lactate oxidation are transferred to the ubiquinone/cytochrome electron transfer chain, where they may be used to provide energy for the active transport of a variety of amino acids and sugars across the membrane. {ECO:0000269|PubMed:2185834, ECO:0000269|PubMed:3013300, ECO:0000269|PubMed:4575624, ECO:0000269|PubMed:4582730, ECO:0000269|PubMed:7578233}. EcoCyc product frame: DLACTDEHYDROGFAD-MONOMER. EcoCyc synonyms: ldh. Genomic coordinates: 2222185-2223900. EcoCyc protein note: D-lactate dehydrogenase (Dld) is a FAD-dependent peripheral membrane dehydrogenase catalysing the oxidation of D-lactate to pyruvate. Dld is a respiratory enzyme; electrons derived from D-lactate oxidation are transferred to the membrane soluble quinone pool . D-lactate dehydrogenase functions as a primary dehydrogenase in aerobic and anaerobic respiratory chains in vitro. Electron transfer from D-lactate to oxygen under aerobic conditions and electron transfer from D-lactate to nitrate under anaerobic conditions depends on the presence of a quinone . Anaerobic β-galactoside transport in whole cells and membrane vesicles can be coupled to the oxidation of D-lactate with fumarate as a terminal acceptor...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06149|protein.P06149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dld; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007048,ECOCYC:EG10231,GeneID:946653`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2222185-2223900:+; feature_type=gene
